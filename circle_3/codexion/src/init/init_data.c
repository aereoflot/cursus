/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   init_data.c                                          :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: angel <angel@student.42.fr>                +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/06/30 00:00:00 by angel             #+#    #+#             */
/*   Updated: 2026/06/30 00:00:00 by angel            ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "codexion.h"

void	init_data(t_data *data)
{
	init_dongles(data);
	init_coders(data);
	pthread_mutex_init(&data->log_mutex, NULL);
	pthread_mutex_init(&data->simulation_mutex, NULL);
	pthread_mutex_init(&data->counter_mutex, NULL);
	data->request_counter = 0;
	data->running = 0;
}
