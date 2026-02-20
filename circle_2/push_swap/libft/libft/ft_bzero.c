/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_bzero.c                                         :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: ancrodri <ancrodri@student.42madrid.com    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/10/01 17:03:02 by acano-sa          #+#    #+#             */
/*   Updated: 2025/12/05 19:15:12 by ancrodri         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

/// Sets the first n bytes of the memory area 
/// 	pointed to by s to zero (null bytes).
/// @param s Pointer to the memory area to be set to zero.
/// @param n Number of bytes to be set to zero.

#include "libft.h"

void	ft_bzero(void *s, size_t n)
{
	size_t			i;
	unsigned char	*str;

	str = (unsigned char *)s;
	i = 0;
	while (i < n)
	{
		str[i] = '\0';
		i++;
	}
}
