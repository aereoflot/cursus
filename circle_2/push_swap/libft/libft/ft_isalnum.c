/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_isalnum.c                                       :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: ancrodri <ancrodri@student.42madrid.com    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/09/30 10:22:11 by acano-sa          #+#    #+#             */
/*   Updated: 2025/12/05 19:15:25 by ancrodri         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

/// Checks if the given character is alphanumeric (either a letter or a digit).
/// @param c The character to be checked.
/// @return Returns a non-zero value if the character is alphanumeric, 
/// 	otherwise returns 0.

#include "libft.h"

int	ft_isalnum(int c)
{
	return (ft_isalpha(c) || ft_isdigit(c));
}
