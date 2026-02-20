/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_calloc.c                                        :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: ancrodri <ancrodri@student.42madrid.com    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/10/01 19:44:52 by acano-sa          #+#    #+#             */
/*   Updated: 2025/12/05 19:15:14 by ancrodri         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

/// Allocates memory for an array of count elements of size bytes each
/// and initializes all bytes in the allocated storage to zero.
/// @param count Number of elements to allocate.
/// @param size Size of each element.
/// @return A pointer to the allocated memory, or NULL if the allocation fails.

#include "libft.h"

void	*ft_calloc(size_t count, size_t size)
{
	void	*ptr;

	ptr = malloc(count * size);
	if (!ptr)
		return (NULL);
	ft_bzero(ptr, count * size);
	return (ptr);
}
