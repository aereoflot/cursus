/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   indexing.c                                         :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: ancrodri <ancrodri@student.42madrid.com    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/12/05 19:20:00 by ancrodri          #+#    #+#             */
/*   Updated: 2025/12/05 19:36:25 by ancrodri         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "push_swap.h"

/*
** stack_to_array -- Copies the values from the stack to an array of ints.
*/
static int	*stack_to_array(t_node *a, int size)
{
	int	*arr;
	int	i;

	arr = (int *)malloc(sizeof(int) * size);
	if (!arr)
		return (NULL);
	i = 0;
	while (a)
	{
		arr[i++] = a->value;
		a = a->next;
	}
	return (arr);
}

/*
** sort_array -- Sorts an array of ints using bubble sort.
** It is sufficient for our size range (<= 500).
*/
static void	sort_array(int *arr, int size)
{
	int	i;
	int	j;
	int	tmp;

	i = 0;
	while (i < size - 1)
	{
		j = 0;
		while (j < size - 1 - i)
		{
			if (arr[j] > arr[j + 1])
			{
				tmp = arr[j];
				arr[j] = arr[j + 1];
				arr[j + 1] = tmp;
			}
			j++;
		}
		i++;
	}
}

/*
** index_of -- Searches for the position of 'value' in the sorted array.
*/
static int	index_of(int *arr, int size, int value)
{
	int	i;

	i = 0;
	while (i < size)
	{
		if (arr[i] == value)
			return (i);
		i++;
	}
	return (-1);
}

/*
** assign_indexes -- Assigns to each node an index from 0 to n-1 according
** to numeric order. This is used to speed up the algorithm.
*/
void	assign_indexes(t_node *a)
{
	int		size;
	int		*arr;
	t_node	*tmp;

	size = stack_size(a);
	arr = stack_to_array(a, size);
	if (!arr)
		print_error_and_exit(&a, NULL);
	sort_array(arr, size);
	tmp = a;
	while (tmp)
	{
		tmp->index = index_of(arr, size, tmp->value);
		tmp = tmp->next;
	}
	free(arr);
}

/*
** find_max_index -- Returns the maximum index present in the stack.
*/
int	find_max_index(t_node *stack)
{
	int	max;

	max = 0;
	while (stack)
	{
		if (stack->index > max)
			max = stack->index;
		stack = stack->next;
	}
	return (max);
}
