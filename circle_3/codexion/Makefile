NAME		= codexion
CC			= cc
CFLAGS		= -Wall -Wextra -Werror -pthread -Iincludes

SRCS_DIR	= src
OBJS_DIR	= obj

SRCS		= main.c \
			  parsing/parse_args.c \
			  init/init_data.c \
			  init/init_coders.c \
			  init/init_dongles.c \
			  threads/coder_routine.c \
			  threads/monitor.c \
			  dongles/acquire_dongle.c \
			  dongles/dongle_order.c \
			  dongles/release_dongle.c \
			  queue/heap.c \
			  queue/scheduler.c \
			  utils/log.c \
			  utils/error.c \
			  utils/atoui.c \
			  utils/atosch.c \
			  utils/strcmp.c \
			  utils/strlen.c \
			  utils/isnumber.c \
			  utils/cleanup.c \
			  utils/time.c

OBJS		= $(addprefix $(OBJS_DIR)/,$(SRCS:.c=.o))

all: $(NAME)

$(NAME): $(OBJS)
	$(CC) $(OBJS) -o $(NAME) -pthread

$(OBJS_DIR)/%.o: $(SRCS_DIR)/%.c
	@mkdir -p $(dir $@)
	$(CC) $(CFLAGS) -c $< -o $@

clean:
	rm -rf $(OBJS_DIR)

fclean: clean
	rm -f $(NAME)

re: fclean all

.PHONY: all clean fclean re
