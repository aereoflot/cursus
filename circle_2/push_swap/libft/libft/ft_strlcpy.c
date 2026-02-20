/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_strlcpy.c                                       :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: ancrodri <ancrodri@student.42madrid.com    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/10/01 18:32:23 by acano-sa          #+#    #+#             */
/*   Updated: 2025/12/05 19:17:28 by ancrodri         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

/// Copies up to dstsize - 1 characters from the string src to dst, 
///		null-terminating the result if dstsize is not 0.
/// @param dst The destination string where the content is to be copied.
/// @param src The source string from which the content is to be copied.
/// @param dstsize The size of the destination buffer.
/// @return The total length of the string it tried to create (length of src).

#include "libft.h"

size_t	ft_strlcpy(char *dst, const char *src, size_t dstsize)
{
	size_t	i;

	i = 0;
	if (dstsize == 0)
		return (ft_strlen(src));
	while (src[i] && i < dstsize - 1)
	{
		dst[i] = src[i];
		i++;
	}
	dst[i] = '\0';
	return (ft_strlen(src));
}
