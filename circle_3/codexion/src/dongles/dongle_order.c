/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   dongle_order.c                                     :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: ancrodri <ancrodri@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/07/04 17:21:09 by ancrodri          #+#    #+#             */
/*   Updated: 2026/07/04 17:21:20 by ancrodri         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "codexion.h"

void	get_dongle_order(t_coder *coder,
						t_dongle **first, t_dongle **second)
{
	if (coder->left_idx <= coder->right_idx)
	{
		*first = coder->left;
		*second = coder->right;
	}
	else
	{
		*first = coder->right;
		*second = coder->left;
	}
}
