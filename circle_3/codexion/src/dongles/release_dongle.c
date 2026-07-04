/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   release_dongle.c                                   :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: ancrodri <ancrodri@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/07/04 17:21:38 by ancrodri          #+#    #+#             */
/*   Updated: 2026/07/04 17:21:38 by ancrodri         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "codexion.h"

static void	release_dongle(t_dongle *dongle)
{
	pthread_mutex_lock(&dongle->mutex);
	dongle->available = 1;
	dongle->last_release_ms = get_time_ms();
	pthread_cond_broadcast(&dongle->cond);
	pthread_mutex_unlock(&dongle->mutex);
}

void	release_one_dongle(t_dongle *dongle)
{
	release_dongle(dongle);
}

void	release_dongles(t_coder *coder)
{
	if (coder->left == coder->right)
		release_dongle(coder->left);
	else
	{
		release_dongle(coder->left);
		release_dongle(coder->right);
	}
}
