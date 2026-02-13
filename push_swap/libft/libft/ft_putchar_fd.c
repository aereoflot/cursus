/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_putchar_fd.c                                    :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: ancrodri <ancrodri@student.42madrid.com    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/10/06 12:20:36 by acano-sa          #+#    #+#             */
/*   Updated: 2025/12/05 19:16:53 by ancrodri         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "libft.h"

/// Writes a character to the specified file descriptor.
/// @param c The character to write.
/// @param fd The file descriptor to write to.

void	ft_putchar_fd(char c, int fd)
{
	write(fd, &c, 1);
}
