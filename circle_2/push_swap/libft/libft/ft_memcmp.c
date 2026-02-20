/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_memcmp.c                                        :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: ancrodri <ancrodri@student.42madrid.com    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/10/01 19:00:44 by acano-sa          #+#    #+#             */
/*   Updated: 2025/12/05 19:16:46 by ancrodri         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

/// Compares the first n bytes of the memory areas s1 and s2.
/// @param s1 Pointer to the first memory area to be compared.
/// @param s2 Pointer to the second memory area to be compared.
/// @param n Number of bytes to compare.
/// @return An integer less than, equal to, or greater than zero 
///		if the first n bytes of s1 is found, respectively, 
///		to be less than, to match, or be greater than the first n bytes of s2.

#include "libft.h"

int	ft_memcmp(const void *s1, const void *s2, size_t n)
{
	size_t				i;
	const unsigned char	*str1;
	const unsigned char	*str2;

	str1 = (const unsigned char *)s1;
	str2 = (const unsigned char *)s2;
	i = 0;
	if (n == 0)
		return (0);
	while (i < n)
	{
		if (str1[i] != str2[i])
			return (str1[i] - str2[i]);
		i++;
	}
	return (0);
}
