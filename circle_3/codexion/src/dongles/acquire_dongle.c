/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   acquire_dongle.c                                   :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: ancrodri <ancrodri@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/07/04 17:17:52 by ancrodri          #+#    #+#             */
/*   Updated: 2026/07/04 17:27:03 by ancrodri         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "codexion.h"

static int	can_take(t_dongle *dongle, unsigned int coder_id,
			t_data *data)
{
	t_request	top;

	if (dongle->wait_heap.size == 0)
		return (0);
	top = heap_peek(&dongle->wait_heap);
	if (top.coder_id != coder_id)
		return (0);
	if (!dongle->available)
		return (0);
	if (dongle->last_release_ms != 0
		&& get_time_ms() - dongle->last_release_ms < data->dongle_cooldown)
		return (0);
	return (1);
}

static void	wait_cooldown(t_dongle *dongle, t_data *data)
{
	struct timeval	v;
	struct timespec	ts;
	unsigned long	elapsed;
	unsigned long	remaining;

	elapsed = get_time_ms() - dongle->last_release_ms;
	if (elapsed >= data->dongle_cooldown)
		return ;
	remaining = data->dongle_cooldown - elapsed;
	gettimeofday(&v, NULL);
	ts.tv_sec = v.tv_sec + (v.tv_usec / 1000 + remaining) / 1000;
	ts.tv_nsec = ((v.tv_usec / 1000 + remaining) % 1000) * 1000000;
	pthread_cond_timedwait(&dongle->cond, &dongle->mutex, &ts);
}

static void	acquire_dongle(t_coder *coder, t_data *data, t_dongle *dongle)
{
	t_request	req;

	req.coder_id = coder->id;
	pthread_mutex_lock(&coder->mutex);
	req.deadline = coder->last_compile_ms + data->time_to_burnout;
	pthread_mutex_unlock(&coder->mutex);
	pthread_mutex_lock(&data->counter_mutex);
	req.arrival_order = data->request_counter++;
	pthread_mutex_unlock(&data->counter_mutex);
	pthread_mutex_lock(&dongle->mutex);
	heap_push(&dongle->wait_heap, req);
	while (is_running(data) && !can_take(dongle, coder->id, data))
	{
		if (dongle->last_release_ms != 0
			&& get_time_ms() - dongle->last_release_ms < data->dongle_cooldown)
			wait_cooldown(dongle, data);
		else
			pthread_cond_wait(&dongle->cond, &dongle->mutex);
	}
	if (is_running(data))
	{
		heap_pop(&dongle->wait_heap);
		dongle->available = 0;
	}
	pthread_mutex_unlock(&dongle->mutex);
}

static void	take_pair_dongles(t_coder *coder, t_data *data,
			t_dongle *first, t_dongle *second)
{
	acquire_dongle(coder, data, first);
	if (!is_running(data))
	{
		release_one_dongle(first);
		return ;
	}
	log_action(data, coder->id, "has taken a dongle");
	acquire_dongle(coder, data, second);
	if (!is_running(data))
	{
		release_one_dongle(first);
		return ;
	}
	log_action(data, coder->id, "has taken a dongle");
}

void	acquire_dongles(t_coder *coder, t_data *data)
{
	t_dongle	*first;
	t_dongle	*second;

	get_dongle_order(coder, &first, &second);
	if (first == second)
	{
		acquire_dongle(coder, data, first);
		if (!is_running(data))
		{
			release_one_dongle(first);
			return ;
		}
		log_action(data, coder->id, "has taken a dongle");
		log_action(data, coder->id, "has taken a dongle");
		return ;
	}
	take_pair_dongles(coder, data, first, second);
}
