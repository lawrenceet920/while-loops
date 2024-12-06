# Ethan Lawrence
# Dec 6 2024
# While loops

import random
# Variable List
name =(input('Hello What is your name?      '))
magic_number = random.randint(1, 100)
guesses_taken = 0

# Start

# -- Magic Number -- #
# print(f'Hi {name} Welcome to higher or lower, In 5 moves guess my number, and I will tell you if it it higher or lower then mine')

# while guesses_taken < 5:
#     guess = int(input(f'Round {guesses_taken + 1}, enter your guess:    '))
#     if guess == magic_number:   # Correct
#         print('Correct, you win!')
#         break
#     elif guess < magic_number:  # Lower
#         print('Your guess is LOWER then the magic number.\n')
#         guesses_taken += 1
#     elif guess > magic_number:  # Higher
#         print('Your guess is HIGHER then the magic number.\n')
#         guesses_taken += 1
#     else:
#         print('ERROR PLEASE RETRY PROGRAM')
# else:
#     print(f'You ran out of guesses the number was {magic_number}')

# -- Tempitures -- #
temps = []
end_loop = True
while end_loop:
    new_temp = int(input('Please enter the next temperature:   '))
    if new_temp == -9999:
        end_loop = False
    else:
        temps.append(new_temp)
else:
    if len(temps) != 0:
        print('\n Listed tempitures:')
        print(temps)
        print()
        print(f'The average tempiture is : {(sum(temps) / len(temps)):.2f}F')
    else:
        print('No temperatures were entered')