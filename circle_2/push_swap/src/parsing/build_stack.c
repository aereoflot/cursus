/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   build_stack.c                                      :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: ancrodri <ancrodri@student.42madrid.com    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/12/05 19:18:18 by ancrodri          #+#    #+#             */
/*   Updated: 2025/12/05 19:36:25 by ancrodri         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "push_swap.h"

/*
** build_stack -- Creates a linked list from the split array of strings,
** already validated. Converts each string to int and adds it to the end
** of the list. Returns a pointer to the stack.
*/
t_node	*build_stack(char **split)
{
	t_node	*a;
	long	value;
	int		i;

	a = NULL;
	i = 0;
	while (split[i])
	{
		value = ft_atoi(split[i]);
		stack_add_back(&a, stack_new((int)value));
		i++;
	}
	return (a);
}
