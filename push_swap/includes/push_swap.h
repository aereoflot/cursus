/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   push_swap.h                                        :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: ancrodri <ancrodri@student.42madrid.com    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/12/05 19:14:13 by ancrodri          #+#    #+#             */
/*   Updated: 2025/12/05 20:21:57 by ancrodri         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#ifndef PUSH_SWAP_H
# define PUSH_SWAP_H

# include "libft.h"
# include <stdlib.h>
# include <unistd.h>

/*
** s_node - Node of our linked list representing a stack. Each element
** has an original value (value), an assigned index (index) and a pointer
** to the next node. The index is used by the main algorithm to easily
** classify elements into groups.
*/
typedef struct s_node
{
	int				value;
	int				index;
	struct s_node	*next;
}					t_node;

/*
** Parsing functions
*/
t_node				*parse_args(int argc, char **argv);
int					check_numeric(char *str);
int					check_int_range(const char *str);
int					has_duplicates(t_node *stack);
t_node				*build_stack(char **split);

/*
** Basic stack operations
*/
void				stack_add_back(t_node **stack, t_node *new);
t_node				*stack_new(int value);
int					stack_size(t_node *stack);
void				stack_clear(t_node **stack);
t_node				*stack_last(t_node *stack);

/*
** Movement operations (swap, push, rotate, reverse rotate)
*/
void				sa(t_node **a, int print);
void				sb(t_node **b, int print);
void				ss(t_node **a, t_node **b, int print);
void				pa(t_node **a, t_node **b, int print);
void				pb(t_node **a, t_node **b, int print);
void				ra(t_node **a, int print);
void				rb(t_node **b, int print);
void				rr(t_node **a, t_node **b, int print);
void				rra(t_node **a, int print);
void				rrb(t_node **b, int print);
void				rrr(t_node **a, t_node **b, int print);

/*
** Utility functions
*/
void				print_error_and_exit(t_node **a, t_node **b);
int					is_sorted(t_node *a);
void				assign_indexes(t_node *a);
int					find_max_index(t_node *stack);
int					position_of_index(t_node *stack, int index);

/*
** Sorting algorithms
*/
void				sort_stack(t_node **a, t_node **b);
void				sort_three(t_node **a);
void				sort_five(t_node **a, t_node **b);
void				sort_big(t_node **a, t_node **b);

#endif