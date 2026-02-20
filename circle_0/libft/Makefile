# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::  #
#    Makefile                                            :+:      :+:    :+:  #
#                                                     +:+ +:+         +:+    #
#    By: ancrodri <ancrodri@student.42madrid.com     +#+  +:+       +#+       #
#                                                 +#+#+#+#+#+   +#+           #
#    Created: 2025/10/02 00:00:00 by anco               #+#    #+#            #
#    Updated: 2025/10/02 00:00:00 by anco               ###   ########.fr      #
#                                                                              #
# **************************************************************************** #

NAME = libft.a

SRCS = $(wildcard *.c)
OBJS = $(SRCS:.c=.o)

CC = gcc
CFLAGS = -Wall -Wextra -Werror
AR = ar rcs
RM = rm -f

all: $(NAME)

$(NAME): $(OBJS)
	$(AR) $(NAME) $(OBJS)

%.o: %.c
	$(CC) $(CFLAGS) -c $< -o $@

clean:
	$(RM) $(OBJS)

fclean: clean
	$(RM) $(NAME)

re: fclean all

.PHONY: all clean fclean re
