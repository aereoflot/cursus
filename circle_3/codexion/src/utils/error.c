/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   error.c                                            :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: ancrodri <ancrodri@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/07/04 17:28:54 by ancrodri          #+#    #+#             */
/*   Updated: 2026/07/04 17:28:54 by ancrodri         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "codexion.h"

int	error(const char *msg)
{
	if (msg)
	{
		write(STDERR_FILENO, "Error: ", 7);
		write(STDERR_FILENO, msg, ft_strlen(msg));
	}
	write(STDERR_FILENO, "\n", 1);
	exit(EXIT_FAILURE);
}
