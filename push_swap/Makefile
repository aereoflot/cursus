NAME		=	push_swap

CC		=	cc
CFLAGS		=	-Wall -Wextra -Werror

INCLUDES	=	-Iincludes -Ilibft/libft

LIBFT_DIR	=	libft/libft
LIBFT		=	$(LIBFT_DIR)/libft.a

SRC_DIR	=	src
SRC_FILES	=	\
	main.c \
	parsing/parse_args.c \
	parsing/check_args.c \
	parsing/build_stack.c \
	stacks/stack_basic.c \
	stacks/stack_utils.c \
	moves/swap.c \
	moves/push.c \
	moves/rotate.c \
	moves/rev_rotate.c \
	utils/error.c \
	utils/indexing.c \
	utils/is_sorted.c \
	algo/sort_small.c \
	algo/sort_big.c

SRCS		=	$(addprefix $(SRC_DIR)/,$(SRC_FILES))
OBJS		=	$(SRCS:.c=.o)

all: $(NAME)

$(LIBFT):
	@$(MAKE) -C $(LIBFT_DIR)

$(NAME): $(LIBFT) $(OBJS)
	$(CC) $(CFLAGS) $(OBJS) $(LIBFT) $(INCLUDES) -o $(NAME)

%.o: %.c
	$(CC) $(CFLAGS) $(INCLUDES) -c $< -o $@

clean:
	@$(MAKE) -C $(LIBFT_DIR) clean
	rm -f $(OBJS)

fclean: clean
	@$(MAKE) -C $(LIBFT_DIR) fclean
	rm -f $(NAME)

re: fclean all

.PHONY: all clean fclean re