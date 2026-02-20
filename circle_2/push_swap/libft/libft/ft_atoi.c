/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_atoi.c                                          :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: ancrodri <ancrodri@student.42madrid.com    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/10/01 19:44:17 by acano-sa          #+#    #+#             */
/*   Updated: 2025/12/05 19:15:09 by ancrodri         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

/// Converts the initial portion of the string pointed 
/// 	to by str to int representation.
/// @param str The string to be converted.
/// @return The converted integer value. If the value exceeds the range of int, 
///		it returns -1 for overflow and 0 for underflow.

#include "libft.h"

int	ft_atoi(const char *str)
{
	int				sign;
	long long		result;
	size_t			i;

	sign = 1;
	result = 0;
	i = 0;
	while (str[i] == ' ' || (str[i] >= 9 && str[i] <= 13))
		i++;
	if (str[i] == '-' || str[i] == '+')
	{
		if (str[i] == '-')
			sign = -1;
		i++;
	}
	while (str[i] >= '0' && str[i] <= '9')
	{
		result = result * 10 + (str[i] - '0');
		if (result * sign > 2147483647)
			return (-1);
		if (result * sign < -2147483648)
			return (0);
		i++;
	}
	return ((int)(result * sign));
}
