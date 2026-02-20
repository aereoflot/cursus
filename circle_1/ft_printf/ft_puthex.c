/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_puthex.c                                        :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: ancrodri <ancrodri@student.42madrid.com    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/10/07 00:00:00 by ancrodri          #+#    #+#             */
/*   Updated: 2025/10/10 19:34:12 by ancrodri         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "ft_printf.h"

static int	ft_count_hex_digits(unsigned long n)
{
	int	count;

	if (n == 0)
		return (1);
	count = 0;
	while (n != 0)
	{
		n /= 16;
		count++;
	}
	return (count);
}

int	ft_puthex(unsigned long n, char format)
{
	char	*hex_digits_lower;
	char	*hex_digits_upper;
	int		count;

	hex_digits_lower = "0123456789abcdef";
	hex_digits_upper = "0123456789ABCDEF";
	count = ft_count_hex_digits(n);
	if (n >= 16)
	{
		ft_puthex(n / 16, format);
	}
	if (format == 'x')
		ft_putchar(hex_digits_lower[n % 16]);
	else
		ft_putchar(hex_digits_upper[n % 16]);
	return (count);
}
