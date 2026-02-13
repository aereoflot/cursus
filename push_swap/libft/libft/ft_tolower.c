/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_tolower.c                                       :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: ancrodri <ancrodri@student.42madrid.com    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/10/01 18:43:21 by acano-sa          #+#    #+#             */
/*   Updated: 2025/12/05 19:17:53 by ancrodri         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

/// Converts an uppercase letter to its lowercase equivalent. 
//		If the character is not an uppercase letter, it is returned unchanged.
/// @param c The character to be converted.
/// @return The lowercase equivalent of the character 
///		if it is an uppercase letter; 
///		otherwise, returns the character unchanged.

#include "libft.h"

int	ft_tolower(int c)
{
	if (c >= 'A' && c <= 'Z')
		return (c + 32);
	return (c);
}
