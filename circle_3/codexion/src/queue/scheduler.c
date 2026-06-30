/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   scheduler.c                                          :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: angel <angel@student.42.fr>                +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/06/30 00:00:00 by angel             #+#    #+#             */
/*   Updated: 2026/06/30 00:00:00 by angel            ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "codexion.h"

int	cmp_fifo(t_request a, t_request b)
{
	if (a.arrival_order < b.arrival_order)
		return (-1);
	if (a.arrival_order > b.arrival_order)
		return (1);
	return (0);
}

int	cmp_edf(t_request a, t_request b)
{
	if (a.deadline < b.deadline)
		return (-1);
	if (a.deadline > b.deadline)
		return (1);
	return (cmp_fifo(a, b));
}
