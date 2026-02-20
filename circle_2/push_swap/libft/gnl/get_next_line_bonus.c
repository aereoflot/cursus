/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   get_next_line_bonus.c                              :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: ancrodri <ancrodri@student.42madrid.com    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/10/15 18:20:00 by acano-sa          #+#    #+#             */
/*   Updated: 2025/12/05 19:14:42 by ancrodri         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "get_next_line_bonus.h"

char	*get_next_line(int fd)
{
	static char	*remainder[FD_MAX];
	char		buffer[BUFFER_SIZE + 1];
	char		*line;

	if (fd < 0 || BUFFER_SIZE <= 0 || fd >= FD_MAX)
		return (NULL);
	remainder[fd] = read_and_accumulate(fd, remainder[fd], buffer);
	if (!remainder[fd])
		return (NULL);
	if (remainder[fd][0] == '\0')
	{
		free(remainder[fd]);
		remainder[fd] = NULL;
		return (NULL);
	}
	line = extract_line(remainder[fd]);
	remainder[fd] = save_remainder(remainder[fd]);
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
