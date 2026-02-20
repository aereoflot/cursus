/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_putunbr.c                                       :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: ancrodri <ancrodri@student.42madrid.com    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/10/10 13:33:17 by ancrodri          #+#    #+#             */
/*   Updated: 2025/10/11 17:05:25 by ancrodri         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "ft_printf.h"

int	lenn(unsigned int n)
{
	int	len;

	if (n == 0)
		return (1);
	len = 0;
	while (n > 0)
	{
		n = n / 10;
		len++;
	}
	return (len);
}

int	ft_putunbr(unsigned int n)
{
	int		len;

	len = lenn(n);
	if (n == 0)
	{
		ft_putchar('0');
		return (1);
	}
	if (n >= 10)
		ft_putunbr(n / 10);
	ft_putchar((n % 10) + '0');
	return (len);
}
