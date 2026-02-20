/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   check_args.c                                       :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: ancrodri <ancrodri@student.42madrid.com    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/12/05 19:19:12 by ancrodri          #+#    #+#             */
/*   Updated: 2025/12/05 19:36:25 by ancrodri         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "push_swap.h"

/*
** check_numeric -- Returns 1 if the string represents a valid integer,
** allowing an optional sign at the beginning and then only digits.
*/
int	check_numeric(char *str)
{
	int	i;

	if (!str || !str[0])
		return (0);
	i = 0;
	if (str[i] == '+' || str[i] == '-')
		i++;
	if (!str[i])
		return (0);
	while (str[i])
	{
		if (!ft_isdigit((unsigned char)str[i]))
			return (0);
		i++;
	}
	return (1);
}

/*
** check_int_range -- Checks that the string converted to long is
** within the range of a 32-bit int. Returns 1 if within range,
** 0 otherwise.
*/
int	check_int_range(const char *str)
{
	long	result;
	long	sign;
	int		i;

	result = 0;
	sign = 1;
	i = 0;
	if (str[i] == '+' || str[i] == '-')
	{
		if (str[i] == '-')
			sign = -1;
		i++;
	}
	while (str[i])
	{
		result = result * 10 + (str[i] - '0');
		if (sign * result > 2147483647 || sign * result < -2147483648)
			return (0);
		i++;
	}
	return (1);
}

/*
** has_duplicates -- Checks if there are duplicate values in the linked
** list. Returns 1 if a duplicate is found, 0 otherwise.
*/
int	has_duplicates(t_node *stack)
{
	t_node	*cur;
	t_node	*tmp;

	cur = stack;
	while (cur)
	{
		tmp = cur->next;
		while (tmp)
		{
			if (tmp->value == cur->value)
				return (1);
			tmp = tmp->next;
		}
		cur = cur->next;
	}
	return (0);
}
