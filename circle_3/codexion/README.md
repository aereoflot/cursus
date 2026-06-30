*This project has been created as part of the 42 curriculum by angel.*

## Description

**Codexion** is a concurrent simulation inspired by the Dining Philosophers problem.
Multiple coders sit around a circular co-working hub and compete for USB dongles to
compile quantum code. Each coder needs two adjacent dongles (left and right) to compile,
then debugs and refactors before trying again.

The program models real-world resource contention: mutex-protected dongles, per-dongle
cooldown after release, fair scheduling (FIFO or EDF), and a monitor thread that detects
burnout when a coder fails to start compiling within the allowed deadline.

The simulation ends when every coder has compiled the required number of times, or when
one coder burns out.

## Instructions

### Compilation

```bash
make
```

This builds the `codexion` binary with `cc`, `-Wall -Wextra -Werror`, and `-pthread`.

### Execution

```bash
./codexion <number_of_coders> <time_to_burnout> <time_to_compile> \
  <time_to_debug> <time_to_refactor> <number_of_compiles_required> \
  <dongle_cooldown> <scheduler>
```

| Argument | Description |
|---|---|
| `number_of_coders` | Number of coders and dongles (≥ 1) |
| `time_to_burnout` | Max ms between compile starts before burnout (≥ 1) |
| `time_to_compile` | Compile duration in ms (≥ 1) |
| `time_to_debug` | Debug duration in ms (≥ 1) |
| `time_to_refactor` | Refactor duration in ms (≥ 1) |
| `number_of_compiles_required` | Compiles per coder to finish successfully |
| `dongle_cooldown` | Ms a dongle stays unavailable after release |
| `scheduler` | `fifo` or `edf` |

### Examples

```bash
# Four coders, EDF scheduling, 100 ms dongle cooldown
./codexion 4 1500 200 200 200 5 100 edf

# Two coders, FIFO scheduling
./codexion 2 800 200 200 200 3 50 fifo
```

### Clean

```bash
make clean    # remove object files
make fclean   # remove objects and binary
make re       # rebuild from scratch
```

## Blocking cases handled

- **Deadlock prevention**: Coders always acquire dongles in a fixed order (lower index
  first). This breaks the circular wait condition from Coffman's deadlock criteria.
- **Mutual exclusion**: Each dongle state (`available`, cooldown timestamp, wait heap) is
  guarded by its own `pthread_mutex_t`.
- **Starvation prevention**: FIFO serves requests by arrival order; EDF serves the coder
  with the earliest burnout deadline (`last_compile_start + time_to_burnout`), with
  arrival order as tiebreaker.
- **Cooldown handling**: After release, a dongle records `last_release_ms` and blocks new
  acquisitions until `dongle_cooldown` ms have elapsed, using `pthread_cond_timedwait`.
- **Precise burnout detection**: A dedicated monitor thread polls every 500 µs and prints
  the burnout message within 10 ms of the actual deadline.
- **Log serialization**: All `printf` output goes through `log_mutex` so lines never
  interleave.
- **Single-coder edge case**: When only one dongle exists, the coder acquires it once but
  logs two "has taken a dongle" messages before compiling.

## Thread synchronization mechanisms

| Primitive | Role |
|---|---|
| `pthread_mutex_t` (per dongle) | Protects dongle availability, cooldown, and wait heap |
| `pthread_cond_t` (per dongle) | Blocks waiting coders; `broadcast` on release wakes contenders |
| `pthread_mutex_t` (per coder) | Protects `last_compile_ms` and `compiles_done` |
| `pthread_mutex_t` (`log_mutex`) | Serializes all status messages |
| `pthread_mutex_t` (`simulation_mutex`) | Protects the global `running` flag |
| `pthread_mutex_t` (`counter_mutex`) | Protects the global FIFO arrival counter |

**Coder threads** enqueue a request in the dongle's min-heap, then wait on the dongle
condition variable until they are at the head of the queue, the dongle is available, and
cooldown has expired.

**Monitor thread** reads each coder's `last_compile_ms` under the coder mutex, compares
against `time_to_burnout`, and sets `running = 0` on burnout or when all coders finish.
It then calls `wake_all` to unblock every waiting coder thread.

**Min-heap priority queue** implements FIFO (key = arrival order) and EDF (key = deadline,
then arrival order) scheduling as required by the subject.

## Resources

- [POSIX Threads Programming (LLNL)](https://hpc-tutorials.llnl.gov/posix/)
- [Dining Philosophers Problem (Wikipedia)](https://en.wikipedia.org/wiki/Dining_philosophers_problem)
- [Earliest Deadline First scheduling](https://en.wikipedia.org/wiki/Earliest_deadline_first_scheduling)
- [man 3 pthread_mutex_lock](https://man7.org/linux/man-pages/man3/pthread_mutex_lock.3.html)
- [man 3 pthread_cond_wait](https://man7.org/linux/man-pages/man3/pthread_cond_wait.3.html)
- [man 2 gettimeofday](https://man7.org/linux/man-pages/man2/gettimeofday.2.html)

### AI usage

AI was used to:

- Understand the project subject and map requirements to a modular file structure.
- Draft the initial architecture (dongle mutex + cond var + heap scheduler + monitor).
- Generate the README structure and concurrency documentation sections.

All generated code was reviewed, adapted, and tested. The heap implementation, single-coder
handling, and synchronization logic were written and verified to match the subject rules.
