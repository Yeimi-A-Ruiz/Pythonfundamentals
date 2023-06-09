import random

# logic game

options = ('rock', 'paper', 'scissors')

user_option = input('rock, paper or scissors: ').lower().strip()
com_option = random.choice(options)

if not user_option in options:
    print('This choice is invalid!!!')
else:
    print(f'User choice {user_option} vs computer choice {com_option}')

# logical approach

"""
equal selection tie
rock beats scissors
scissors beats paper
paper beats rock
"""

if user_option == com_option:
    print('tie!')

elif user_option == 'rock':
    if com_option == 'scissors':
        print('rock beats scissors')
        print('User wins!')
    else:
        print('paper beats rock')
        print('Com wins!')

elif user_option == 'scissors':
    if com_option == 'paper':
        print('scissors beats paper')
        print('User wins')
    else:
        print('rock beats scissors')
        print('Com wins!')

elif user_option == 'paper':
    if com_option == 'rock':
        print('paper beats rock')
        print('User wins!')
    else:
        print('scissors beats paper')
        print('Com wins!')