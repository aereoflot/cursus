/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   error.c                                              :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: angel <angel@student.42.fr>                +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/06/30 00:00:00 by angel             #+#    #+#             */
/*   Updated: 2026/06/30 00:00:00 by angel            ###   ########.fr       */
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
