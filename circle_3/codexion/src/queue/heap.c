/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   heap.c                                               :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: angel <angel@student.42.fr>                +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/06/30 00:00:00 by angel             #+#    #+#             */
/*   Updated: 2026/06/30 00:00:00 by angel            ###   ########.fr       */
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

static void	heap_up(t_heap *heap, int idx)
{
	int	parent;

	while (idx > 0)
	{
		parent = (idx - 1) / 2;
		if (heap->cmp(heap->items[idx], heap->items[parent]) >= 0)
			break ;
		swap_req(&heap->items[idx], &heap->items[parent]);
		idx = parent;
	}
}

static void	heap_down(t_heap *heap, int idx)
{
	int	left;
	int	right;
	int	smallest;

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

void	heap_push(t_heap *heap, t_request req)
{
	if (heap->size >= heap->capacity)
		error("Heap overflow.");
	heap->items[heap->size] = req;
	heap_up(heap, heap->size);
	heap->size++;
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

t_request	heap_peek(t_heap *heap)
{
	return (heap->items[0]);
}

void	destroy_heap(t_heap *heap)
{
	free(heap->items);
	heap->items = NULL;
	heap->size = 0;
	heap->capacity = 0;
}
