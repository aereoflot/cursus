/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   codexion.h                                         :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: ancrodri <ancrodri@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/07/04 16:24:45 by ancrodri          #+#    #+#             */
/*   Updated: 2026/07/04 17:48:59 by ancrodri         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#ifndef CODEXION_H
# define CODEXION_H

# include <stdio.h>
# include <stdlib.h>
# include <unistd.h>
# include <string.h>
# include <sys/time.h>
# include "struct.h"

/* init */
void	init_data(t_data *data);
void	init_coders(t_data *data);
void	init_dongles(t_data *data);

/* parsing */
void	parse_args(int ac, char **av, t_data *data);

/* threads */
void	*coder_routine(void *arg);
void	*monitor_routine(void *arg);
void	wake_all(t_data *data);
int		is_running(t_data *data);

/* dongles */
void	acquire_dongles(t_coder *coder, t_data *data);
void	get_dongle_order(t_coder *c, t_dongle **f, t_dongle **s);
void	release_dongles(t_coder *coder);
void	release_one_dongle(t_dongle *dongle);

/* scheduler */
int		cmp_fifo(t_request a, t_request b);
int		cmp_edf(t_request a, t_request b);

/* heap */
void	init_heap(t_heap *heap, int capacity, t_cmp cmp);

void	heap_push(t_heap *heap, t_req req);

void	destroy_heap(t_heap *heap);

t_req	heap_pop(t_heap *heap);

t_req	heap_peek(t_heap *heap);

/* utils */
t_uint	ft_atoui(const char *nptr);

int		ft_strcmp(const char *s1, const char *s2);

void	log_action(t_data *data, t_uint id, char *action);

int		error(const char *msg);

int		ft_isnumber(const char *str);

void	cleanup(t_data *data);

void	ft_usleep(unsigned long ms, t_data *data);

t_size	ft_strlen(const char *s);

t_ms	get_time_ms(void);

t_sched	ft_atosch(const char *nptr);

#endif
