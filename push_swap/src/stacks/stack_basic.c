/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   stack_basic.c                                      :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: ancrodri <ancrodri@student.42madrid.com    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/12/05 19:19:42 by ancrodri          #+#    #+#             */
/*   Updated: 2025/12/05 19:36:25 by ancrodri         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "push_swap.h"

/*
** stack_new -- Allocates memory for a new node with the given value
** and returns a pointer to it. Initializes index to -1 and next to NULL.
*/
t_node	*stack_new(int value)
{
	t_node	*node;

	node = (t_node *)malloc(sizeof(t_node));
	if (!node)
		return (NULL);
	node->value = value;
	node->index = -1;
	node->next = NULL;
	return (node);
}

/*
** stack_add_back -- Adds a node to the end of the list. If the list
** is empty, sets the new node as the head.
*/
void	stack_add_back(t_node **stack, t_node *new)
{
	t_node	*last;

	if (!stack || !new)
		return ;
	if (!*stack)
	{
		*stack = new;
		return ;
	}
	last = *stack;
	while (last->next)
		last = last->next;
	last->next = new;
}

/*
** stack_clear -- Frees the entire list, setting the provided pointer
** to NULL.
*/
void	stack_clear(t_node **stack)
{
	t_node	*tmp;

	if (!stack)
		return ;
	while (*stack)
	{
		tmp = (*stack)->next;
		free(*stack);
		*stack = tmp;
	}
}

/*
** stack_last -- Returns the last node of the list. If the list is
** empty, returns NULL.
*/
t_node	*stack_last(t_node *stack)
{
	if (!stack)
		return (NULL);
	while (stack->next)
		stack = stack->next;
	return (stack);
}
