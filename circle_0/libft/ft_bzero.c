/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_bzero.c                                         :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: ancrodri <ancrodri@student.42madrid.com    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/10/01 12:24:56 by ancrodri          #+#    #+#             */
/*   Updated: 2025/10/02 13:56:52 by ancrodri         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "libft.h"

void	ft_bzero(void *pnt, size_t len)
{
	int				i;
	unsigned char	*ptr;

	ptr = (unsigned char *)pnt;
	i = 0;
	while (len)
	{
		ptr[i] = 0;
		i++;
		len--;
	}
}
// Fills memory with zeros.
