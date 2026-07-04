/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   struct.h                                           :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: ancrodri <ancrodri@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/06/30 00:00:00 by angel             #+#    #+#             */
/*   Updated: 2026/07/04 18:15:09 by ancrodri         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#ifndef STRUCT_H
# define STRUCT_H

# include <pthread.h>

typedef enum e_scheduler
{
	FIFO,
	EDF
}	t_scheduler;

typedef t_scheduler		t_sched;

typedef struct s_request
{
	unsigned int	coder_id;
	long			deadline;
	unsigned long	arrival_order;
}	t_request;

typedef unsigned int	t_uint;
typedef size_t			t_size;
typedef t_request		t_req;

typedef int				(*t_cmp)(t_request, t_request);

typedef unsigned long	t_ms;

typedef struct s_heap
{
	t_request		*items;
	int				size;
	int				capacity;
	t_cmp			cmp;
}	t_heap;

typedef struct s_dongle
{
	pthread_mutex_t	mutex;
	int				available;
	long			last_release_ms;
	t_heap			wait_heap;
	pthread_cond_t	cond;
}	t_dongle;

typedef struct s_coder
{
	unsigned int		id;
	unsigned int		compiles_done;
	long				last_compile_ms;
	t_dongle			*left;
	t_dongle			*right;
	int					left_idx;
	int					right_idx;
	pthread_t			thread;
	pthread_mutex_t		mutex;
	struct s_data		*data;
}	t_coder;

typedef struct s_data
{
	unsigned int		number_of_coders;
	unsigned int		time_to_burnout;
	unsigned int		time_to_compile;
	unsigned int		time_to_debug;
	unsigned int		time_to_refactor;
	unsigned int		number_of_compiles_required;
	unsigned int		dongle_cooldown;
	t_scheduler			scheduler;
	t_coder				*coders;
	t_dongle			*dongles;
	pthread_mutex_t		log_mutex;
	pthread_mutex_t		simulation_mutex;
	int					running;
	unsigned long		start_time;
	unsigned long		request_counter;
	pthread_mutex_t		counter_mutex;
	pthread_t			monitor_thread;
}	t_data;

#endif