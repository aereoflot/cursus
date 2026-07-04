/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   init_coders.c                                      :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: ancrodri <ancrodri@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/07/04 17:27:37 by ancrodri          #+#    #+#             */
/*   Updated: 2026/07/04 17:27:37 by ancrodri         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "codexion.h"

void	init_coders(t_data *data)
{
	unsigned int	i;

	data->coders = malloc(sizeof(t_coder) * data->number_of_coders);
	if (!data->coders)
		error("Coders allocation failed.");
	i = 0;
	while (i < data->number_of_coders)
	{
		data->coders[i].id = i + 1;
		data->coders[i].compiles_done = 0;
		data->coders[i].last_compile_ms = 0;
		data->coders[i].left = &data->dongles[i];
		data->coders[i].right = &data->dongles[(i + 1)
			% data->number_of_coders];
		data->coders[i].left_idx = i;
		data->coders[i].right_idx = (i + 1) % data->number_of_coders;
		data->coders[i].data = data;
		pthread_mutex_init(&data->coders[i].mutex, NULL);
		i++;
	}
}
