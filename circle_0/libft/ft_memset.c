/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_memset.c                                        :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: ancrodri <ancrodri@student.42madrid.com    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/10/01 13:57:11 by ancrodri          #+#    #+#             */
/*   Updated: 2025/10/02 13:59:27 by ancrodri         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "libft.h"

void	*ft_memset(void *pnt, int c, size_t n)
{
	int				i;
	unsigned char	*ptr;

	ptr = (unsigned char *)pnt;
	i = 0;
	while (n)
	{
		ptr[i] = (unsigned char)c;
		i++;
		n--;
	}
	return (pnt);
}
	// Fills memory with a value.
