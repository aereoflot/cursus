/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_strncmp.c                                       :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: ancrodri <ancrodri@student.42madrid.com    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/10/01 18:48:02 by acano-sa          #+#    #+#             */
/*   Updated: 2025/12/05 19:17:34 by ancrodri         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

/// Compares up to n characters of the strings s1 and s2.
/// @param s1 The first string to be compared.
/// @param s2 The second string to be compared.
/// @param n The maximum number of characters to compare.
/// @return An integer less than, equal to, or greater than zero if s1 
///		(or the first n bytes thereof) is found, 
///		respectively, to be less than, to match, or be greater than s2.

#include "libft.h"

int	ft_strncmp(const char *s1, const char *s2, size_t n)
{
	size_t	i;

	i = 0;
	if (n == 0)
		return (0);
	while (s1[i] && s2[i] && s1[i] == s2[i] && i < n - 1)
		i++;
	return ((unsigned char)s1[i] - (unsigned char)s2[i]);
}
