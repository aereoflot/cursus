/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   is_sorted.c                                        :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: ancrodri <ancrodri@student.42madrid.com    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/12/05 19:20:05 by ancrodri          #+#    #+#             */
/*   Updated: 2025/12/05 19:36:25 by ancrodri         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "push_swap.h"

/*
** is_sorted -- Checks if the stack is already sorted in ascending order.
** Returns 1 if sorted or empty, 0 otherwise.
*/
int	is_sorted(t_node *a)
{
	if (!a)
		return (1);
	while (a->next)
	{
		if (a->value > a->next->value)
			return (0);
		a = a->next;
	}
	return (1);
}

/*
** It's here because it didn't fit in indexing.
** position_of_index -- Returns the position (base 0) of the first node
** whose index matches 'index'. If not found, returns -1.
*/
int	position_of_index(t_node *stack, int index)
{
	int	pos;

	pos = 0;
	while (stack)
	{
		if (stack->index == index)
			return (pos);
		stack = stack->next;
		pos++;
	}
	return (-1);
}
