/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   get_next_line_bonus.h                              :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: ancrodri <ancrodri@student.42madrid.com    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/10/16 16:04:36 by ancrodri          #+#    #+#             */
/*   Updated: 2025/10/16 16:53:00 by ancrodri         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#ifndef GET_NEXT_LINE_BONUS_H
# define GET_NEXT_LINE_BONUS_H

# include <fcntl.h>
# include <stdlib.h>
# include <unistd.h>

# ifndef BUFFER_SIZE
#  define BUFFER_SIZE 42
# endif

# define MAX_FD 1024

char		*get_next_line(int fd);
char		*ft_strjoin(char const *s1, char const *s2);
int			ft_strlen(const char *str);
char		*ft_strdup(const char *src);
int			ft_find_newline(const char *str);
char		*ft_extract_line(char *saved, int nl_pos);

#endif