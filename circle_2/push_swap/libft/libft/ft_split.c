/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_split.c                                         :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: ancrodri <ancrodri@student.42madrid.com    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/10/06 11:51:47 by acano-sa          #+#    #+#             */
/*   Updated: 2025/12/05 19:17:04 by ancrodri         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "libft.h"

/// Counts the number of words in the string separated by the given delimiter.
/// @param s The input string.
/// @param c The delimiter character.
/// @return The number of words found in the string.

static size_t	count_words(const char *s, char c)
{
	size_t	count;
	size_t	i;

	count = 0;
	i = 0;
	while (s[i])
	{
		while (s[i] == c)
			i++;
		if (s[i])
			count++;
		while (s[i] && s[i] != c)
			i++;
	}
	return (count);
}

/// Frees the allocated memory for the split result in case of an error.
/// @param result The array of strings to be freed.
/// @param j The number of strings already allocated.

static void	free_split(char **result, size_t j)
{
	while (j > 0)
		free(result[--j]);
	free(result);
}

/// Extracts a word from the string starting at index i, skipping delimiters.
/// @param s The input string.
/// @param c The delimiter character.
/// @param i The current index in the string.
/// @return The extracted word as a newly allocated string.

static char	*get_word(const char *s, char c, size_t *i)
{
	size_t	start;
	size_t	end;

	while (s[*i] == c)
		(*i)++;
	start = *i;
	while (s[*i] && s[*i] != c)
		(*i)++;
	end = *i;
	return (ft_substr(s, start, end - start));
}

/// Fills the split result array with words extracted from the string.
/// @param s The input string.
/// @param c The delimiter character.
/// @param word_count The number of words to extract.
/// @return The array of strings containing the split words,
/// 	or NULL if allocation fails.

static char	**fill_split(const char *s, char c, size_t word_count)
{
	char	**result;
	size_t	i;
	size_t	j;

	i = 0;
	j = 0;
	result = (char **)malloc((word_count + 1) * sizeof(char *));
	if (!result)
		return (NULL);
	while (j < word_count)
	{
		result[j] = get_word(s, c, &i);
		if (!result[j])
		{
			free_split(result, j);
			return (NULL);
		}
		j++;
	}
	result[j] = NULL;
	return (result);
}

/// Splits the input string into an array of strings using the given delimiter.
/// @param s The input string to be split.
/// @param c The delimiter character.
/// @return An array of strings resulting from the split,
/// 	or NULL if allocation fails.

char	**ft_split(char const *s, char c)
{
	size_t	word_count;

	if (!s)
		return (NULL);
	word_count = count_words(s, c);
	return (fill_split(s, c, word_count));
}
