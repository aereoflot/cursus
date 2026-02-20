/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_printf.c                                        :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: ancrodri <ancrodri@student.42madrid.com    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/10/10 00:00:00 by ancrodri          #+#    #+#             */
/*   Updated: 2025/10/11 17:24:57 by ancrodri         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "ft_printf.h"

static int	aplications(va_list args, char caracter)
{
	if (caracter == 'c')
		return (ft_putchar(va_arg(args, int)));
	else if (caracter == 's')
		return (ft_putstr(va_arg(args, char *)));
	else if (caracter == 'p')
		return (ft_putptr(va_arg(args, void *)));
	else if (caracter == 'd' || caracter == 'i')
		return (ft_putnbr(va_arg(args, int)));
	else if (caracter == 'u')
		return (ft_putunbr(va_arg(args, unsigned int)));
	else if (caracter == 'x' || caracter == 'X')
		return (ft_puthex(va_arg(args, unsigned int), caracter));
	else if (caracter == '%')
		return (ft_putchar('%'));
	return (0);
}

int	ft_printf(const char *format, ...)
{
	va_list	args;
	int		i;
	int		count;

	if (!format)
		return (-1);
	va_start(args, format);
	i = 0;
	count = 0;
	while (format[i])
	{
		if (format[i] == '%' && format[i + 1])
		{
			i++;
			count += aplications(args, format[i]);
		}
		else if (format[i] != '%')
		{
			count += ft_putchar(format[i]);
		}
		i++;
	}
	va_end(args);
	return (count);
}
