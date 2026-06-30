/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   cleanup.c                                            :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: angel <angel@student.42.fr>                +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/06/30 00:00:00 by angel             #+#    #+#             */
/*   Updated: 2026/06/30 00:00:00 by angel            ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "codexion.h"

static void	cleanup_dongles(t_data *data)
{
	unsigned int	i;

	if (!data->dongles)
		return ;
	i = 0;
	while (i < data->number_of_coders)
	{
		pthread_mutex_destroy(&data->dongles[i].mutex);
		pthread_cond_destroy(&data->dongles[i].cond);
		destroy_heap(&data->dongles[i].wait_heap);
		i++;
	}
	free(data->dongles);
	data->dongles = NULL;
}

static void	cleanup_mutexes(t_data *data)
{
	unsigned int	i;

	i = 0;
	while (i < data->number_of_coders)
	{
		pthread_mutex_destroy(&data->coders[i].mutex);
		i++;
	}
	pthread_mutex_destroy(&data->log_mutex);
	pthread_mutex_destroy(&data->simulation_mutex);
	pthread_mutex_destroy(&data->counter_mutex);
}

void	cleanup(t_data *data)
{
	if (!data)
		return ;
	cleanup_dongles(data);
	cleanup_mutexes(data);
	if (data->coders)
	{
		free(data->coders);
		data->coders = NULL;
	}
}
