/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   get_next_line.c                                    :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: ancrodri <ancrodri@student.42madrid.com    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/10/11 17:37:13 by ancrodri          #+#    #+#             */
/*   Updated: 2025/10/13 21:21:16 by ancrodri         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "get_next_line.h"

static char	*ft_read_and_join(int fd, char *saved, int *eof)
{
	char	*buffer;
	char	*new_saved;
	int		byte_read;

	buffer = malloc(BUFFER_SIZE + 1);
	if (!buffer)
		return (saved);
	byte_read = read(fd, buffer, BUFFER_SIZE);
	if (byte_read < 0)
	{
		free(buffer);
		free(saved);
		return (NULL);
	}
	if (byte_read == 0)
		*eof = 1;
	buffer[byte_read] = '\0';
	new_saved = ft_strjoin(saved, buffer);
	free(buffer);
	free(saved);
	return (new_saved);
}

static char	*ft_process_line(char **saved, int nl_pos)
{
	char	*line;
	char	*temp;

	line = ft_extract_line(*saved, nl_pos);
	temp = *saved;
	*saved = ft_strdup(*saved + nl_pos + 1);
	free(temp);
	return (line);
}

static char	*ft_handle_eof(char **saved)
{
	char	*line;

	line = NULL;
	if (*saved && (*saved)[0])
		line = ft_strdup(*saved);
	free(*saved);
	*saved = NULL;
	return (line);
}

char	*get_next_line(int fd)
{
	static char	*saved;
	int			nl_pos;
	int			eof;

	if (fd < 0)
		return (NULL);
	while (1)
	{
		eof = 0;
		saved = ft_read_and_join(fd, saved, &eof);
		if (!saved)
			return (NULL);
		nl_pos = ft_find_newline(saved);
		if (nl_pos >= 0)
			return (ft_process_line(&saved, nl_pos));
		if (!eof)
			continue ;
		return (ft_handle_eof(&saved));
	}
}
