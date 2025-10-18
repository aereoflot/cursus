/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_putptr.c                                        :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: ancrodri <ancrodri@student.42madrid.com    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/10/07 13:39:07 by ancrodri          #+#    #+#             */
/*   Updated: 2025/10/15 18:56:01 by ancrodri         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "ft_printf.h"

int	ft_putptr(void *ptr)
{
	unsigned long	adres;
	int				len;

	if (!ptr)
	{
		write(2, "(nil)", 5);
		return (5);
	}
	adres = (unsigned long)ptr;
	write(1, "0x", 2);
	len = 2;
	len += ft_puthex(adres, 'x');
	return (len);
}
