/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_isalnum.c                                       :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: ancrodri <ancrodri@student.42madrid.com    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/10/01 12:38:33 by ancrodri          #+#    #+#             */
/*   Updated: 2025/10/04 19:20:39 by ancrodri         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "libft.h"

int	ft_isalnum(int a)
{
	if (((a >= 'a' && a <= 'z') || (a >= 'A' && a <= 'Z'))
		|| (a >= '0' && a <= '9'))
		return (1);
	return (0);
}
// Checks if character is alphanumeric.
