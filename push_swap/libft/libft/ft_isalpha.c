/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_isalpha.c                                       :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: ancrodri <ancrodri@student.42madrid.com    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/09/30 10:22:19 by acano-sa          #+#    #+#             */
/*   Updated: 2025/12/05 19:15:26 by ancrodri         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

/// Checks if the given character is an alphabetic letter 
///		(either uppercase or lowercase).
/// @param c The character to be checked.
/// @return Returns a non-zero value if the character is an alphabetic letter, 
/// 	otherwise returns 0.

#include "libft.h"

int	ft_isalpha(int c)
{
	if ((c >= 'A' && c <= 'Z') || (c >= 'a' && c <= 'z'))
		return (1);
	return (0);
}
