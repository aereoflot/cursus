/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   coder_routine.c                                      :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: angel <angel@student.42.fr>                +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/06/30 00:00:00 by angel             #+#    #+#             */
/*   Updated: 2026/06/30 00:00:00 by angel            ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "codexion.h"

static int	compile_cycle(t_coder *coder, t_data *data)
{
	acquire_dongles(coder, data);
	if (!is_running(data))
		return (0);
	pthread_mutex_lock(&coder->mutex);
	coder->last_compile_ms = get_time_ms();
	pthread_mutex_unlock(&coder->mutex);
	log_action(data, coder->id, "is compiling");
	ft_usleep(data->time_to_compile, data);
	release_dongles(coder);
	pthread_mutex_lock(&coder->mutex);
	coder->compiles_done++;
	pthread_mutex_unlock(&coder->mutex);
	return (1);
}

void	*coder_routine(void *arg)
{
	t_coder	*coder;
	t_data	*data;

	coder = (t_coder *)arg;
	data = coder->data;
	while (is_running(data)
		&& coder->compiles_done < data->number_of_compiles_required)
	{
		if (!compile_cycle(coder, data))
			break ;
		if (!is_running(data))
			break ;
		log_action(data, coder->id, "is debugging");
		ft_usleep(data->time_to_debug, data);
		log_action(data, coder->id, "is refactoring");
		ft_usleep(data->time_to_refactor, data);
	}
	return (NULL);
}
