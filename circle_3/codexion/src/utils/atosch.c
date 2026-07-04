/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   atosch.c                                           :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: ancrodri <ancrodri@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/07/04 17:28:41 by ancrodri          #+#    #+#             */
/*   Updated: 2026/07/04 17:28:41 by ancrodri         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "codexion.h"

static char	*to_lower(const char *s)
{
	char	*res;
	int		i;

	res = malloc(ft_strlen(s) + 1);
	if (!res)
		return (NULL);
	i = 0;
	while (s[i])
	{
		res[i] = s[i];
		if (s[i] >= 'A' && s[i] <= 'Z')
			res[i] = s[i] + 32;
		i++;
	}
	res[i] = '\0';
	return (res);
}

t_scheduler	ft_atosch(const char *nptr)
{
	char	*low;

	low = to_lower(nptr);
	if (low && ft_strcmp(low, "fifo") == 0)
	{
		free(low);
		return (FIFO);
	}
	if (low && ft_strcmp(low, "edf") == 0)
	{
		free(low);
		return (EDF);
	}
	free(low);
	return (error("Scheduler value must be one of: fifo, edf"));
}
