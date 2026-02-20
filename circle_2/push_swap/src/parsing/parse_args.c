/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   parse_args.c                                       :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: ancrodri <ancrodri@student.42madrid.com    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/12/05 19:19:34 by ancrodri          #+#    #+#             */
/*   Updated: 2025/12/05 19:36:25 by ancrodri         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "push_swap.h"

/*
** join_and_split -- Concatenates all arguments (except argv[0]) into
** a single string separated by spaces and then splits them using ft_split.
** This allows accepting both separate arguments and a string in quotes.
** Returns an array of strings terminated in NULL.
*/
static char	**join_and_split(int argc, char **argv)
{
	char	*joined;
	char	*tmp;
	char	**split;
	int		i;

	joined = ft_strdup("");
	if (!joined)
		return (NULL);
	i = 1;
	while (i < argc)
	{
		tmp = ft_strjoin(joined, " ");
		free(joined);
		if (!tmp)
			return (NULL);
		joined = ft_strjoin(tmp, argv[i]);
		free(tmp);
		if (!joined)
			return (NULL);
		i++;
	}
	split = ft_split(joined, ' ');
	free(joined);
	return (split);
}

/*
** free_split -- Frees an array of strings created by ft_split.
*/
static void	free_split(char **split)
{
	int	i;

	if (!split)
		return ;
	i = 0;
	while (split[i])
	{
		free(split[i]);
		i++;
	}
	free(split);
}

/*
** parse_args -- Entry point for parsing. Joins and splits the arguments,
** checks that each token is numeric and within the range of an int,
** then builds a linked list with build_stack. If there is a memory error
** or invalid token, prints "Error" and terminates.
*/
t_node	*parse_args(int argc, char **argv)
{
	char	**split;
	t_node	*a;
	int		i;

	split = join_and_split(argc, argv);
	if (!split || !split[0])
	{
		free_split(split);
		return (NULL);
	}
	i = 0;
	while (split[i])
	{
		if (!check_numeric(split[i]) || !check_int_range(split[i]))
		{
			free_split(split);
			print_error_and_exit(NULL, NULL);
		}
		i++;
	}
	a = build_stack(split);
	free_split(split);
	return (a);
}
