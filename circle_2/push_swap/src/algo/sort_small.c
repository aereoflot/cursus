/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   sort_small.c                                       :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: ancrodri <ancrodri@student.42madrid.com    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/12/05 19:18:05 by ancrodri          #+#    #+#             */
/*   Updated: 2025/12/05 19:36:25 by ancrodri         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "push_swap.h"

/*
** sort_two -- Trivial case of 2 elements. If they are reversed,
** execute sa.
*/
static void	sort_two(t_node **a)
{
	if ((*a)->value > (*a)->next->value)
		sa(a, 1);
}

/*
** sort_three -- Sorts three elements using a minimal set
** of operations. Identifies five disorder patterns.
*/
void	sort_three(t_node **a)
{
	int	x;
	int	y;
	int	z;

	x = (*a)->value;
	y = (*a)->next->value;
	z = (*a)->next->next->value;
	if (x > y && y < z && x < z)
		sa(a, 1);
	else if (x > y && y > z)
	{
		sa(a, 1);
		rra(a, 1);
	}
	else if (x > y && y < z && x > z)
		ra(a, 1);
	else if (x < y && y > z && x < z)
	{
		sa(a, 1);
		ra(a, 1);
	}
	else if (x < y && y > z && x > z)
		rra(a, 1);
}

/*
** find_min_pos -- Returns the position of the node with the minimum value
** in the stack. Used to push the minimums to B in sort_five.
*/
static int	find_min_pos(t_node *a)
{
	int	pos;
	int	min_pos;
	int	min_val;

	pos = 0;
	min_pos = 0;
	min_val = a->value;
	while (a)
	{
		if (a->value < min_val)
		{
			min_val = a->value;
			min_pos = pos;
		}
		pos++;
		a = a->next;
	}
	return (min_pos);
}

/*
** sort_five -- Sorts stacks of size 4 or 5. Sends the minimum
** elements to B until 3 remain in A. Then those 3 are sorted
** and finally everything is returned to A.
*/
void	sort_five(t_node **a, t_node **b)
{
	int	size;
	int	min_pos;

	size = stack_size(*a);
	while (size > 3)
	{
		min_pos = find_min_pos(*a);
		if (min_pos <= size / 2)
			while (min_pos-- > 0)
				ra(a, 1);
		else
			while (min_pos++ < size)
				rra(a, 1);
		pb(a, b, 1);
		size = stack_size(*a);
	}
	sort_three(a);
	while (*b)
		pa(a, b, 1);
}

/*
** sort_stack -- Selects the appropriate algorithm based on the
** size of the initial stack. 2, 3, 4 or 5 are handled with
** dedicated algorithms. For larger sizes sort_big is called.
*/
void	sort_stack(t_node **a, t_node **b)
{
	int	size;

	size = stack_size(*a);
	if (size == 2)
		sort_two(a);
	else if (size == 3)
		sort_three(a);
	else if (size <= 5)
		sort_five(a, b);
	else
		sort_big(a, b);
}
