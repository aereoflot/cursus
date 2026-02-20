/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_toupper.c                                       :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: ancrodri <ancrodri@student.42madrid.com    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/10/01 18:42:53 by acano-sa          #+#    #+#             */
/*   Updated: 2025/12/05 19:17:55 by ancrodri         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

/// Converts a lowercase letter to its uppercase equivalent. 
///		If the character is not a lowercase letter, it is returned unchanged.
/// @param c The character to be converted.
/// @return The uppercase equivalent of the character 
///		if it is a lowercase letter; otherwise, returns the character unchanged.

#include "libft.h"

int	ft_toupper(int c)
{
	if (c >= 'a' && c <= 'z')
		return (c - 32);
	return (c);
}
