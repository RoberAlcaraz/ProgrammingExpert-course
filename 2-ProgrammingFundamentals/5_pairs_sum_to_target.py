# 5. Pairs Sum to Target

#   Write a function that accepts two lists (list1 and list2) of integers and a target integer named
#   target. Your function should return all pairs of indices in the
#   form [x, y] where list1[x] + list2[y] == target. In
#   other words, return the pairs of indices where the sum of their values equals target.

list1 = [1, -2, 4, 5, 9]
list2 = [4, 2, -4, -4, 0]
target = 5


def pairs_sum_to_target(list1, list2, target):
    list_of_pairs = []

    for idx1, num1 in enumerate(list1):
        for idx2, num2 in enumerate(list2):
            if num1 + num2 == target:
                list_of_pairs.append([idx1, idx2])

    return list_of_pairs


print(pairs_sum_to_target(list1, list2, target))
