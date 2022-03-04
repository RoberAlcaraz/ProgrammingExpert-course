# Random Number Guesser

# Write a program that asks the user to enter two integers representing the
# start and the end of a range. The program should then generate a random
# number within this range (inclusively) and ask the user to guess numbers
# until they guess the randomly generated number. Once the user guesses the
# random number, the program should tell them how many attempts it took them
# to guess it.


# Your program needs to ensure that the range of numbers given is valid. For
# example, if the user enters a number for the end of the range that is less
# than the start of the range your program needs ask them to enter a valid
# number. Your program must also handle any other errors that might occur,
# like the user entering a string instead of an integer.


# Note: You may assume the start of the range will never be negative (i.e you
# don't need to handle negative values).

import random

number_1 = input('Enter the start of the range: ')
while not number_1.isdigit():
    print('Please enter a valid number.')
    number_1 = input('Enter the start of the range: ')
number_1 = int(number_1)

while True:
    number_2 = input('Enter the end of the range: ')

    while not number_2.isdigit():
        print('Please enter a valid number.')
        number_2 = input('Enter the end of the range: ')
    number_2 = int(number_2)

    if number_2 < number_1:
        print('Please enter a valid number.')
    else:
        break

random_number = random.randint(number_1, number_2)
guessed_number = 0
attempts = 0

while guessed_number != random_number:
    guessed_number = input('Guess a number: ')
    while not guessed_number.isdigit():
        print('Please enter a valid number.')
        guessed_number = input('Guess a number: ')
    guessed_number = int(guessed_number)
    attempts += 1

if attempts == 1:
    print(f'You guessed the number in 1 attempt')
else:
    print(f'You guessed the number in {attempts} attempts')
