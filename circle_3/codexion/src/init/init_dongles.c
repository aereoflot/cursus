/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   init_dongles.c                                     :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: ancrodri <ancrodri@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/07/04 17:27:51 by ancrodri          #+#    #+#             */
/*   Updated: 2026/07/04 17:27:51 by ancrodri         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "codexion.h"

void	init_dongles(t_data *data)
{
	unsigned int	i;
	int				(*cmp)(t_request, t_request);

	data->dongles = malloc(sizeof(t_dongle) * data->number_of_coders);
	if (!data->dongles)
		error("Dongles allocation failed.");
	if (data->scheduler == FIFO)
		cmp = cmp_fifo;
	else
		cmp = cmp_edf;
	i = 0;
	while (i < data->number_of_coders)
	{
		pthread_mutex_init(&data->dongles[i].mutex, NULL);
		pthread_cond_init(&data->dongles[i].cond, NULL);
		data->dongles[i].available = 1;
		data->dongles[i].last_release_ms = 0;
		init_heap(&data->dongles[i].wait_heap, data->number_of_coders, cmp);
		i++;
	}
}
