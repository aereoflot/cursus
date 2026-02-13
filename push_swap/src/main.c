/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   main.c                                             :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: ancrodri <ancrodri@student.42madrid.com    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/12/05 19:20:10 by ancrodri          #+#    #+#             */
/*   Updated: 2025/12/05 20:20:07 by ancrodri         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "push_swap.h"

/*
** Entry point of the program. Creates the initial stack from the
** provided arguments, checks data validity and if the list is already
** sorted. If sorting is needed, assigns indexes and executes the main
** algorithm. Finally frees all memory.
*/
int	main(int argc, char **argv)
{
	t_node	*a;
	t_node	*b;

	if (argc < 2)
		return (0);
	a = parse_args(argc, argv);
	if (!a)
		return (0);
	if (has_duplicates(a))
		print_error_and_exit(&a, NULL);
	if (is_sorted(a))
	{
		stack_clear(&a);
		return (0);
	}
	assign_indexes(a);
	b = NULL;
	sort_stack(&a, &b);
	stack_clear(&a);
	stack_clear(&b);
	return (0);
}
