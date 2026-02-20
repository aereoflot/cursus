/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   libft.h                                            :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: ancrodri <ancrodri@student.42madrid.com    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/10/01 12:47:58 by ancrodri          #+#    #+#             */
/*   Updated: 2025/10/10 13:25:22 by ancrodri         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#ifndef LIBFT_H
# define LIBFT_H

# include <stddef.h>
# include <stdio.h>
# include <stdlib.h>
# include <unistd.h>

void				ft_bzero(void *pnt, size_t len);
int					ft_atoi(const char *str);
void				*ft_calloc(unsigned int nmemb, size_t size);
int					ft_isalnum(int a);
int					ft_isalpha(int a);
int					ft_isascii(int a);
int					ft_isdigit(int i);
int					ft_isprint(int a);
int					ft_memcmp(const void *s1, const void *s2, size_t n);
int					ft_strncmp(char *s1, char *s2, unsigned int n);
int					ft_strlen(const char *str);
void				ft_putchar_fd(char c, int fd);
void				ft_putnbr_fd(int n, int fd);
void				ft_putendl_fd(char *s, int fd);
void				ft_putstr_fd(char *s, int fd);
void				*ft_memset(void *pnt, int c, size_t n);
void				*ft_memmove(void *dst, const void *src, size_t len);
void				*ft_memcpy(void *dest, const void *src, size_t n);
char				*ft_strrchr(const char *str, int c);
char				*ft_strchr(const char *str, int c);
char				**ft_split(char const *s, char c);
char				*ft_strnstr(const char *haystack, const char *needle,
						unsigned int len);
char				*ft_strdup(const char *src);
char				*ft_strjoin(char const *s1, char const *s2);
unsigned int		ft_strlcat(char *dest, char *src, unsigned int size);
unsigned int		ft_strlcpy(char *dest, char *src, unsigned int size);
void				*ft_memchr(const void *str, int c, size_t n);
int					ft_toupper(int a);
int					ft_tolower(int a);
char				*ft_strtrim(char const *s1, char const *set);
char				*ft_strmapi(char const *s, char (*f)(unsigned int, char));
void				ft_striteri(char *s, void (*f)(unsigned int, char *));
char				*ft_substr(char const *s, unsigned int start, size_t len);
char				*ft_itoa(int n);

#endif