# 6. Create strings from characters

# Write a function that accepts a dictonary called
# frequencies and two strings named string1 and string2.
# The frequencies dictionary contains
# character keys and integer values, the value associated with each character
# represents its frequency. Your function should return 0, 1 or 2 according
# on the cases below:

# - 2:  if the frequency of characters
#   in the dictionary is sufficient to create both string1 and string2
#   without reusing any CHARACTERS

# - 1:  if the frequency of characters
#   in the dictionary is sufficient to create either string1 or string2
#   without reusing any CHARACTERS

# - 0:  if the frequency of characters
#   in the dictionary is not sufficient to create either string1 or string2
#   without reusing any CHARACTERS

frequencies = {"h": 2, "e": 1, "l": 1, "r": 4, "a": 3,  "o": 2, "d": 1, "w": 1}
string1 = 'hello'
string2 = 'world'


def get_freq_dictionary_from_string(string):
    string_freq = {}
    for char in string:
        if char not in string_freq.keys():
            string_freq[char] = 1
        else:
            string_freq[char] += 1
    return string_freq


def create_strings_from_characters(frequencies, string1, string2):

    strings = [string1, string2]

    list_of_dicts = []

    for st in strings:
        list_of_dicts.append(get_freq_dictionary_from_string(st))

    cases = 2
    for dic in list_of_dicts:
        for key, val in dic.items():
            if key in frequencies.keys() and val <= frequencies[key]:
                frequencies[key] -= val
            else:
                cases -= 1
                continue

    if cases < 0:
        cases = 0

    return cases


frequencies = {"h": 2, "e": 1, "l": 2, "r": 4, "a": 3, "o": 2, "d": 1, "w": 1}
string1 = "hello"
string2 = "world"
print(create_strings_from_characters(frequencies, string1, string2))
