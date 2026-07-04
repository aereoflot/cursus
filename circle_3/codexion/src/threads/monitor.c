/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   monitor.c                                          :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: ancrodri <ancrodri@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/07/04 17:28:35 by ancrodri          #+#    #+#             */
/*   Updated: 2026/07/04 17:28:35 by ancrodri         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "codexion.h"

static void	handle_burnout(t_data *data, unsigned int idx, unsigned long now)
{
	pthread_mutex_lock(&data->log_mutex);
	printf("%lu %u burned out\n",
		now - data->start_time, data->coders[idx].id);
	pthread_mutex_lock(&data->simulation_mutex);
	data->running = 0;
	pthread_mutex_unlock(&data->simulation_mutex);
	pthread_mutex_unlock(&data->log_mutex);
	wake_all(data);
}

static void	check_burnout(t_data *data)
{
	unsigned int	i;
	unsigned long	now;

	i = 0;
	while (i < data->number_of_coders)
	{
		pthread_mutex_lock(&data->coders[i].mutex);
		if (data->coders[i].compiles_done
			>= data->number_of_compiles_required)
		{
			pthread_mutex_unlock(&data->coders[i].mutex);
			i++;
			continue ;
		}
		now = get_time_ms();
		if (now - data->coders[i].last_compile_ms >= data->time_to_burnout)
		{
			pthread_mutex_unlock(&data->coders[i].mutex);
			handle_burnout(data, i, now);
			return ;
		}
		pthread_mutex_unlock(&data->coders[i].mutex);
		i++;
	}
}

static void	check_all_done(t_data *data)
{
	unsigned int	i;

	i = 0;
	while (i < data->number_of_coders)
	{
		pthread_mutex_lock(&data->coders[i].mutex);
		if (data->coders[i].compiles_done
			< data->number_of_compiles_required)
		{
			pthread_mutex_unlock(&data->coders[i].mutex);
			return ;
		}
		pthread_mutex_unlock(&data->coders[i].mutex);
		i++;
	}
	pthread_mutex_lock(&data->simulation_mutex);
	data->running = 0;
	pthread_mutex_unlock(&data->simulation_mutex);
	wake_all(data);
}

void	*monitor_routine(void *arg)
{
	t_data	*data;

	data = (t_data *)arg;
	while (is_running(data))
	{
		check_burnout(data);
		if (!is_running(data))
			break ;
		check_all_done(data);
		usleep(500);
	}
	return (NULL);
}
