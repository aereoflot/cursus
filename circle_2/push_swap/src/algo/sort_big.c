/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   sort_big.c                                         :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: ancrodri <ancrodri@student.42madrid.com    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/12/05 19:18:03 by ancrodri          #+#    #+#             */
/*   Updated: 2025/12/05 19:29:58 by ancrodri         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "push_swap.h"

/*
** push_chunks_to_b -- Empuja desde A hacia B usando trozos basados en
** el índice.  Los elementos se envían a B cuando su índice cae en
** el rango actual (chunk).  Los que están en la mitad inferior del
** chunk se rotan en B para balancear la distribución.
*/
static void	push_chunks_to_b(t_node **a, t_node **b, int size)
{
	int	chunk;
	int	i;
	int	min_index;

	if (size <= 100)
		chunk = 15;
	else
		chunk = 30;
	min_index = 0;
	i = 0;
	while (i < size)
	{
		if ((*a)->index <= min_index + chunk)
		{
			pb(a, b, 1);
			if ((*b)->index < min_index + chunk / 2)
				rb(b, 1);
			min_index++;
			i++;
		}
		else
			ra(a, 1);
	}
}

/*
** move_max_to_top -- Lleva el elemento con el índice más alto en B
** hasta el tope de la pila.  Utiliza rb o rrb según el camino más
** corto calculado con la posición relativa.
*/
static void	move_max_to_top(t_node **b)
{
	int	max;
	int	pos;
	int	size;

	size = stack_size(*b);
	max = find_max_index(*b);
	pos = position_of_index(*b, max);
	if (pos <= size / 2)
	{
		while (pos-- > 0)
			rb(b, 1);
	}
	else
	{
		while (pos++ < size)
			rrb(b, 1);
	}
}

/*
** sort_big -- Algoritmo principal para listas de tamaño > 5.
** 1) Empuja elementos en trozos de A a B.  2) Una vez en B, se
** traen de vuelta a A en orden descendente sacando siempre el
** mayor índice de B.
*/
void	sort_big(t_node **a, t_node **b)
{
	int	size;

	size = stack_size(*a);
	push_chunks_to_b(a, b, size);
	while (*b)
	{
		move_max_to_top(b);
		pa(a, b, 1);
	}
}
