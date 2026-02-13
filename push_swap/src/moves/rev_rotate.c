/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   rev_rotate.c                                       :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: ancrodri <ancrodri@student.42madrid.com    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/12/05 19:18:10 by ancrodri          #+#    #+#             */
/*   Updated: 2025/12/05 19:36:25 by ancrodri         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "push_swap.h"

/*
** reverse_rotate -- Moves the last element of the stack to the beginning.
** Does not print anything by itself. Used by rra, rrb and rrr.
*/
static void	reverse_rotate(t_node **stack)
{
	t_node	*prev;
	t_node	*last;

	if (!stack || !*stack || !(*stack)->next)
		return ;
	prev = NULL;
	last = *stack;
	while (last->next)
	{
		prev = last;
		last = last->next;
	}
	if (prev)
		prev->next = NULL;
	last->next = *stack;
	*stack = last;
}

void	rra(t_node **a, int print)
{
	reverse_rotate(a);
	if (print)
		ft_putendl_fd("rra", 1);
}

void	rrb(t_node **b, int print)
{
	reverse_rotate(b);
	if (print)
		ft_putendl_fd("rrb", 1);
}

void	rrr(t_node **a, t_node **b, int print)
{
	reverse_rotate(a);
	reverse_rotate(b);
	if (print)
		ft_putendl_fd("rrr", 1);
}
