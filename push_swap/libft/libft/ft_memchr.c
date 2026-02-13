/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_memchr.c                                        :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: ancrodri <ancrodri@student.42madrid.com    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/10/01 19:00:00 by acano-sa          #+#    #+#             */
/*   Updated: 2025/12/05 19:16:44 by ancrodri         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

/// Searches for the first occurrence of the character c 
///		(converted to an unsigned char) 
///		in the first n bytes of the memory area pointed to by s.
/// @param s Pointer to the memory area to be searched.
/// @param c The character to be located (passed as an int, 
/// 	but treated as an unsigned char).
/// @param n The number of bytes to be analyzed.
/// @return A pointer to the first occurrence of the character c 
///		in the memory area s, 
///		or NULL if the character is not found within the first n bytes.

#include "libft.h"

void	*ft_memchr(const void *s, int c, size_t n)
{
	size_t				i;
	const unsigned char	*str;
	unsigned char		ch;

	str = (const unsigned char *)s;
	ch = (unsigned char)c;
	i = 0;
	while (i < n)
	{
		if (str[i] == ch)
			return ((void *)(str + i));
		i++;
	}
	return (NULL);
}
