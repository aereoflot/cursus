/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   get_next_line.c                                    :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: ancrodri <ancrodri@student.42madrid.com    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/10/15 18:08:41 by acano-sa          #+#    #+#             */
/*   Updated: 2025/12/05 19:14:54 by ancrodri         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "get_next_line.h"

char	*get_next_line(int fd)
{
	static char	*remainder;
	char		buffer[BUFFER_SIZE + 1];
	char		*line;

	if (fd < 0 || BUFFER_SIZE <= 0)
		return (NULL);
	remainder = read_and_accumulate(fd, remainder, buffer);
	if (!remainder)
		return (NULL);
	if (remainder[0] == '\0')
	{
		free(remainder);
		remainder = NULL;
		return (NULL);
	}
	line = extract_line(remainder);
	remainder = save_remainder(remainder);
	return (line);
}

char	*read_and_accumulate(int fd, char *remainder, char *buffer)
{
	int	bytes_read;

	bytes_read = 1;
	while (!ft_strchr(remainder, '\n') && bytes_read > 0)
	{
		bytes_read = read(fd, buffer, BUFFER_SIZE);
		if (bytes_read < 0)
		{
			free(remainder);
			return (NULL);
		}
		if (bytes_read == 0)
			break ;
		buffer[bytes_read] = '\0';
		remainder = ft_strjoin(remainder, buffer);
		if (!remainder)
			return (NULL);
	}
	return (remainder);
}

char	*extract_line(char *remainder)
{
	int		i;
	char	*line;

	if (!remainder)
		return (NULL);
	i = 0;
	while (remainder[i] && remainder[i] != '\n')
		i++;
	if (remainder[i] == '\n')
		line = ft_substr(remainder, 0, i + 1);
	else
		line = ft_substr(remainder, 0, i);
	return (line);
}

char	*save_remainder(char *remainder)
{
	int		i;
	char	*tmp;
	char	*new_rem;

	if (!remainder)
		return (NULL);
	i = 0;
	while (remainder[i] && remainder[i] != '\n')
		i++;
	tmp = remainder;
	if (remainder[i] == '\n')
		new_rem = ft_substr(remainder, i + 1, ft_strlen(remainder) - (i + 1));
	else
		new_rem = NULL;
	free(tmp);
	return (new_rem);
}
