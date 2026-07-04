/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   heap_utils.c                                       :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: ancrodri <ancrodri@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/07/04 17:28:07 by ancrodri          #+#    #+#             */
/*   Updated: 2026/07/04 17:48:59 by ancrodri         ###   ########.fr       */
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

void	heap_push(t_heap *heap, t_request req)
{
	if (heap->size >= heap->capacity)
		error("Heap overflow.");
	heap->items[heap->size] = req;
	heap_up(heap, heap->size);
	heap->size++;
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
