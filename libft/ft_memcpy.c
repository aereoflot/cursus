/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_memcpy.c                                        :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: ancrodri <ancrodri@student.42madrid.com    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/10/01 14:20:00 by ancrodri          #+#    #+#             */
/*   Updated: 2025/10/10 13:20:10 by ancrodri         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "libft.h"

void	*ft_memcpy(void *dest, const void *src, size_t n)
{
	unsigned char		*desti;
	const unsigned char	*source;

	if (!dest && !src)
		return (NULL);
	source = (const unsigned char *)src;
	desti = (unsigned char *)dest;
	while (n--)
	{
		*desti = *source;
		desti++;
		source++;
	}
	return (dest);
}
	// Copies memory from one area to another.
