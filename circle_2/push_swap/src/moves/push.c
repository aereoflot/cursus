/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   push.c                                             :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: ancrodri <ancrodri@student.42madrid.com    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/12/05 19:18:08 by ancrodri          #+#    #+#             */
/*   Updated: 2025/12/05 19:36:25 by ancrodri         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "push_swap.h"

/*
** push -- Takes the first element from the 'from' stack and places it at
** the beginning of the 'to' stack. Used by pa and pb.
*/
static void	push(t_node **from, t_node **to)
{
	t_node	*tmp;

	if (!from || !*from)
		return ;
	tmp = *from;
	*from = (*from)->next;
	tmp->next = *to;
	*to = tmp;
}

void	pa(t_node **a, t_node **b, int print)
{
	push(b, a);
	if (print)
		ft_putendl_fd("pa", 1);
}

void	pb(t_node **a, t_node **b, int print)
{
	push(a, b);
	if (print)
		ft_putendl_fd("pb", 1);
}
