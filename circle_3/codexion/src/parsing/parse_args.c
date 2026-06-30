/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   parse_args.c                                         :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: angel <angel@student.42.fr>                +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/06/30 00:00:00 by angel             #+#    #+#             */
/*   Updated: 2026/06/30 00:00:00 by angel            ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "codexion.h"

static void	check_positive(t_data *data)
{
	if (!data->number_of_coders || !data->time_to_burnout
		|| !data->time_to_compile || !data->time_to_debug
		|| !data->time_to_refactor)
		error("Numeric arguments 1-5 must be greater than 0.");
}

void	parse_args(int ac, char **av, t_data *data)
{
	int	i;

	if (ac != 9)
		error("Invalid argument count. Expected 8 arguments.");
	i = 1;
	while (i < 8)
	{
		if (!ft_isnumber(av[i]))
			error("All first 7 arguments must be positive integers.");
		i++;
	}
	data->number_of_coders = ft_atoui(av[1]);
	data->time_to_burnout = ft_atoui(av[2]);
	data->time_to_compile = ft_atoui(av[3]);
	data->time_to_debug = ft_atoui(av[4]);
	data->time_to_refactor = ft_atoui(av[5]);
	data->number_of_compiles_required = ft_atoui(av[6]);
	data->dongle_cooldown = ft_atoui(av[7]);
	data->scheduler = ft_atosch(av[8]);
	check_positive(data);
}
