/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_strlcat.c                                       :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: ancrodri <ancrodri@student.42madrid.com    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/10/01 18:36:21 by acano-sa          #+#    #+#             */
/*   Updated: 2025/12/05 19:17:25 by ancrodri         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

/// Appends the string src to the end of dst. 
///		It will append at most dstsize - strlen(dst) - 1 characters. 
///		It will then NUL-terminate, 
//		unless dstsize is 0 or the original dst string was longer than dstsize.
/// @param dst The destination string to which src will be appended.
/// @param src The source string to be appended to dst.
/// @param dstsize The total size of the destination buffer.
/// @return The total length of the string it tried to create 
///		(initial length of dst plus length of src).

#include "libft.h"

size_t	ft_strlcat(char *dst, const char *src, size_t dstsize)
{
	size_t	dst_len;
	size_t	src_len;
	size_t	i;

	dst_len = ft_strlen(dst);
	src_len = ft_strlen(src);
	if (dstsize <= dst_len)
		return (dstsize + src_len);
	i = 0;
	while (src[i] && (dst_len + i) < (dstsize - 1))
	{
		dst[dst_len + i] = src[i];
		i++;
	}
	dst[dst_len + i] = '\0';
	return (dst_len + src_len);
}
