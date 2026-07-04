/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   atoui.c                                            :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: ancrodri <ancrodri@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/07/04 17:28:45 by ancrodri          #+#    #+#             */
/*   Updated: 2026/07/04 17:28:45 by ancrodri         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

unsigned int	ft_atoui(const char *nptr)
{
	unsigned int	res;

	res = 0;
	while ((*nptr >= 9 && *nptr <= 13) || *nptr == ' ')
		nptr++;
	if (*nptr == '-')
		return (0);
	if (*nptr == '+')
		nptr++;
	while (*nptr >= '0' && *nptr <= '9')
		res = res * 10 + (*nptr++ - '0');
	return (res);
}
