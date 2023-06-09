import random

# logic game

options = ('rock', 'paper', 'scissors')

Com_wins = 0
User_wins = 0
rounds = 1

while True:

    print('*' * 10)
    print('ROUND', rounds)
    print('*' * 10)

    print(f'COM {Com_wins} Vs. USER {User_wins}')

    user_option = input('rock, paper or scissors: ').lower().strip()
    com_option = random.choice(options)

    if not user_option in options:
        print('This choice is invalid!!!')
        print('')
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
            print('')
            print('tie!')
            print('')

        elif user_option == 'rock':
            if com_option == 'scissors':
                print('rock beats scissors')
                print('')
                print('User wins!'.upper())
                print('')
                User_wins += 1
            else:
                print('paper beats rock')
                print('')
                print('Com wins!'.upper())
                print('')
                Com_wins += 1

        elif user_option == 'scissors':
            if com_option == 'paper':
                print('scissors beats paper')
                print('')
                print('User wins'.upper())
                print('')
                User_wins += 1
            else:
                print('rock beats scissors')
                print('')
                print('Com wins!'.upper())
                print('')
                Com_wins += 1

        elif user_option == 'paper':
            if com_option == 'rock':
                print('paper beats rock')
                print('')
                print('User wins!'.upper())
                print('')
                User_wins += 1
            else:
                print('scissors beats paper')
                print('')
                print('Com wins!'.upper())
                print('')
                Com_wins += 1
    
    if Com_wins == 2:
        print(f'COM {Com_wins} Vs. USER {User_wins}')
        print('The computer wins the game!'.upper())
        break

    if User_wins == 2:
        print(f'COM {Com_wins} Vs. USER {User_wins}')
        print('The user wins the game!'.upper())
        break

    rounds += 1