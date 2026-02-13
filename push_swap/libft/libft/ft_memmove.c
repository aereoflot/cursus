/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_memmove.c                                       :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: ancrodri <ancrodri@student.42madrid.com    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/10/01 17:42:08 by acano-sa          #+#    #+#             */
/*   Updated: 2025/12/05 19:16:49 by ancrodri         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

/// Copies n bytes from memory area src to memory area dest.  
///		The memory areas may overlap; 
///			the copy is always done in a non-destructive manner.
/// @param dest Pointer to the destination 
///		memory area where bytes will be copied.
/// @param src Pointer to the source 
///		memory area from which bytes will be copied.
/// @param n Number of bytes to copy.
/// @return Returns a pointer to the destination memory area dest.

#include "libft.h"

void	*ft_memmove(void *dest, const void *src, size_t n)
{
	unsigned char		*d;
	const unsigned char	*s;

	d = (unsigned char *)dest;
	s = (const unsigned char *)src;
	if (d == s || n == 0)
		return (dest);
	if (d < s)
	{
		while (n--)
			*d++ = *s++;
	}
	else
	{
		d += n;
		s += n;
		while (n--)
			*--d = *--s;
	}
	return (dest);
}
