/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   heap.c                                             :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: ancrodri <ancrodri@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/07/04 17:28:07 by ancrodri          #+#    #+#             */
/*   Updated: 2026/07/04 18:15:37 by ancrodri         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "codexion.h"

static void	swap_req(t_request *a, t_request *b)
{
	t_request	tmp;

	tmp = *a;
	*a = *b;
	*b = tmp;
}

static void	heap_down(t_heap *heap, int idx)
{
	int		left;
	int		right;
	int		smallest;

	while (1)
	{
		left = idx * 2 + 1;
		right = left + 1;
		smallest = idx;
		if (left < heap->size
			&& heap->cmp(heap->items[left], heap->items[smallest]) < 0)
			smallest = left;
		if (right < heap->size
			&& heap->cmp(heap->items[right], heap->items[smallest]) < 0)
			smallest = right;
		if (smallest == idx)
			break ;
		swap_req(&heap->items[idx], &heap->items[smallest]);
		idx = smallest;
	}
}

void	init_heap(t_heap *heap, int capacity, int (*cmp)(t_request, t_request))
{
	heap->items = malloc(sizeof(t_request) * capacity);
	if (!heap->items)
		error("Heap allocation failed.");
	heap->size = 0;
	heap->capacity = capacity;
	heap->cmp = cmp;
}

t_request	heap_pop(t_heap *heap)
{
	t_request	top;

	top = heap->items[0];
	heap->size--;
	if (heap->size > 0)
	{
		heap->items[0] = heap->items[heap->size];
		heap_down(heap, 0);
	}
	return (top);
}
