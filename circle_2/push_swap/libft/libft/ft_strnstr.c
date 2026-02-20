/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_strnstr.c                                       :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: ancrodri <ancrodri@student.42madrid.com    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/10/01 19:43:50 by acano-sa          #+#    #+#             */
/*   Updated: 2025/12/05 19:17:38 by ancrodri         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

/// Locates the first occurrence of the null-terminated 
///		string needle in the string haystack, 
///		where not more than len characters are searched.
/// @param haystack The string to be searched.
/// @param needle The substring to be located within haystack.
/// @param len The maximum number of characters to search in haystack.
/// @return A pointer to the first occurrence of needle in haystack 
///			within the first len characters, or NULL if needle is not found. 
///			If needle is an empty string, returns haystack.

#include "libft.h"

char	*ft_strnstr(const char *haystack, const char *needle, size_t len)
{
	size_t	i;
	size_t	j;

	if (*needle == '\0')
		return ((char *)haystack);
	i = 0;
	while (haystack[i] && i < len)
	{
		j = 0;
		while (haystack[i + j] == needle[j] && (i + j) < len)
		{
			if (needle[j + 1] == '\0')
				return ((char *)(haystack + i));
			j++;
		}
		i++;
	}
	return (NULL);
}
