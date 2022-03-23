def positive_even_squares(*args):
    filtered_list = []
    for lst in args:
        filtered_list += list(
            map(lambda x: x ** 2,
                filter(lambda x: x % 2 == 0,
                       filter(lambda x: x > 0,
                              lst))))

    return filtered_list


args = [[-5, 2, 3, 4, 5], [1, 3, 5, 6, 7], [-9, -8, 10]]
print(positive_even_squares(*args))
# print(positive_even_squares([[-5, 2, 3, 4, 5], [1, 3, 5, 6, 7], [-9, -8, 10]]))
