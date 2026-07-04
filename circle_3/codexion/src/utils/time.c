/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   time.c                                             :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: ancrodri <ancrodri@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/07/04 17:29:18 by ancrodri          #+#    #+#             */
/*   Updated: 2026/07/04 17:29:18 by ancrodri         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "codexion.h"

t_ms	get_time_ms(void)
{
	struct timeval	tv;

	gettimeofday(&tv, NULL);
	return ((tv.tv_sec * 1000UL) + (tv.tv_usec / 1000UL));
}

void	ft_usleep(unsigned long ms, t_data *data)
{
	unsigned long	start;

	start = get_time_ms();
	while (get_time_ms() - start < ms)
	{
		if (!is_running(data))
			break ;
		usleep(500);
	}
}
