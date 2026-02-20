/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   error.c                                            :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: ancrodri <ancrodri@student.42madrid.com    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/12/05 19:19:55 by ancrodri          #+#    #+#             */
/*   Updated: 2025/12/05 19:36:25 by ancrodri         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "push_swap.h"

/*
** print_error_and_exit -- Frees the provided stacks, prints
** "Error" to stderr and terminates the program with EXIT_FAILURE.
** Used for any error case during parsing or execution.
*/
void	print_error_and_exit(t_node **a, t_node **b)
{
	if (a && *a)
		stack_clear(a);
	if (b && *b)
		stack_clear(b);
	ft_putendl_fd("Error", 2);
	exit(EXIT_FAILURE);
}
