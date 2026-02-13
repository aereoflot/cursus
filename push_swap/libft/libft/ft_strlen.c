/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_strlen.c                                        :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: ancrodri <ancrodri@student.42madrid.com    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/10/01 18:34:13 by acano-sa          #+#    #+#             */
/*   Updated: 2025/12/05 19:17:30 by ancrodri         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

/// Calculates the length of the string pointed to by s, 
///		excluding the null terminator.
/// @param s The string whose length is to be calculated.
/// @return The length of the string 
///		(number of characters before the null terminator).

#include "libft.h"

size_t	ft_strlen(const char *s)
{
	size_t	len;

	len = 0;
	while (s[len] != '\0')
		len++;
	return (len);
}
