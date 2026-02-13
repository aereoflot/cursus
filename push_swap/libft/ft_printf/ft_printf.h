/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_printf.h                                        :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: ancrodri <ancrodri@student.42madrid.com    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/10/11 17:49:14 by acano-sa          #+#    #+#             */
/*   Updated: 2025/12/05 19:14:35 by ancrodri         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#ifndef FT_PRINTF_H
# define FT_PRINTF_H

# include <stdarg.h>
# include <unistd.h>
# include <stdlib.h>

int		ft_printf(const char *format, ...);
int		ft_putstr(char *str);
int		ft_putnbr(long n);
int		ft_putnbr_base(unsigned long n, char *base);
int		ft_putchar(char c);
int		ft_format(char c, va_list args);
int		ft_putptr(void *ptr);

#endif