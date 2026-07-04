/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   init_data.c                                        :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: ancrodri <ancrodri@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/07/04 17:27:45 by ancrodri          #+#    #+#             */
/*   Updated: 2026/07/04 17:27:45 by ancrodri         ###   ########.fr       */
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
