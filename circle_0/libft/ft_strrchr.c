/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_strrchr.c                                       :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: ancrodri <ancrodri@student.42madrid.com    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/10/01 14:20:00 by ancrodri          #+#    #+#             */
/*   Updated: 2025/10/02 13:56:52 by ancrodri         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "libft.h"

char	*ft_strrchr(const char *str, int c)
{
	const char	*pnt;

	pnt = NULL;
	while (*str)
	{
		if (*str == (char)c)
			pnt = str;
		str++;
	}
	if ((char)c == '\0')
		return ((char *)str);
	return ((char *)pnt);
}
	// Finds the last occurrence of a character.
