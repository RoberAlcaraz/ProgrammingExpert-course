# 4. Longest Unique Words

# Write a function that accepts a list of strings that represent words and a
# positive integer n , representing the number of words to return.
# Your function should return a new list containing the n longest
# unique words from the input list. Words are unique if they only appear one
# time in the input list.

# There will always be exactly n  words to return and you may
# return the words in any order.

# Note: all strings in the input list will not contain any special characters
# or spaces.

words = ['Longer', 'Whatever', 'Longer', 'Ball', 'Rock', 'Rocky', 'Rocky']
n = 3


def get_n_longest_unique_words(words, n):
    counted_words = [words.count(word) for word in words]
    unique_list = []

    for i in range(len(counted_words)):

        if counted_words[i] == 1:

            unique_list.append(words[i])

    sorted_list = sorted(unique_list, key=lambda x: len(x), reverse=True)
    return sorted_list[:n]


get_n_longest_unique_words(words, n)
