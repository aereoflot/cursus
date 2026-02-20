/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   swap.c                                             :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: ancrodri <ancrodri@student.42madrid.com    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/12/05 19:18:14 by ancrodri          #+#    #+#             */
/*   Updated: 2025/12/05 19:36:25 by ancrodri         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "push_swap.h"

/*
** swap -- Swaps the first two nodes of the given stack. Does not
** print anything by itself; printing is done in the public functions
** if print=1 is passed.
*/
static void	swap(t_node **stack)
{
	t_node	*first;
	t_node	*second;

	if (!stack || !*stack || !(*stack)->next)
		return ;
	first = *stack;
	second = first->next;
	first->next = second->next;
	second->next = first;
	*stack = second;
}

void	sa(t_node **a, int print)
{
	swap(a);
	if (print)
		ft_putendl_fd("sa", 1);
}

void	sb(t_node **b, int print)
{
	swap(b);
	if (print)
		ft_putendl_fd("sb", 1);
}

void	ss(t_node **a, t_node **b, int print)
{
	swap(a);
	swap(b);
	if (print)
		ft_putendl_fd("ss", 1);
}
