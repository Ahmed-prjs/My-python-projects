def table(pick):
    print(f'  {pick[1]} | {pick[2]} | {pick[3]} ')
    print('-------------')
    print(f'  {pick[4]} | {pick[5]} | {pick[6]} ')
    print('-------------')
    print(f'  {pick[7]} | {pick[8]} | {pick[9]} ')


pick = ['#', 1, 2, 3, 4, 5, 6, 7, 8, 9]


# table(pick)

def winner():
    # answer
    # check for a winning pattern
    if pick[1] == pick[2] == pick[3] and pick[1] != ' ':
        print(f'{pick[1]} wins')
        return True

    elif pick[1] == pick[4] == pick[7] and pick[1] != ' ':
        print(f'{pick[1]} wins')
        return True
    elif pick[1] == pick[5] == pick[9] and pick[1] != ' ':
        print(f'{pick[1]} wins')
        return True
    elif pick[7] == pick[5] == pick[3] and pick[7] != ' ':
        print(f'{pick[7]} wins')
        return True
    elif pick[7] == pick[8] == pick[9] and pick[7] != ' ':
        print(f'{pick[7]} wins')
        return True
    elif pick[4] == pick[5] == pick[6] and pick[4] != ' ':
        print(f'{pick[4]} wins')
        return True
    elif pick[2] == pick[5] == pick[8] and pick[2] != ' ':
        print(f'{pick[2]} wins')
        return True
    elif pick[3] == pick[6] == pick[9] and pick[3] != ' ':
        print(f'{pick[3]} wins')
        return True
    return False


print('Choose X or O')
player1 = input('> ').upper()
while player1 != 'X' and player1 !='O':
    print('Choose either ❌ or ⭕')
    player1 = input('> ').upper()


#IF PLAYER-1 IS X
while player1 == 'X':

    print("player2 is '⭕'")

    print('Possible positions for your picks')
    print(f'  1 | 2 | 3 ')
    print('-------------')
    print(f'  4 | 5 | 6 ')
    print('-------------')
    print(f'  7 | 8 | 9 ')

    # Round 1
    print('player1 choose a position')
    while True:

        try:
            answer1 = int(input('> '))

            if answer1 not in range(1, 10):
                print('Please choose a number between 1 and 9.')
            else:
                break
        except ValueError:
            print('Invalid input. Please enter a number.')
    print('\n' * 100)
    pick[answer1] = '❌'
    table(pick)

    print('Player2 choose a position')
    while True:

        try:
            answer2 = int(input('> '))

            if answer2 not in range(1, 10):
                print('Please choose a number between 1 and 9.')
            elif answer2 == answer1:
                print('That spot is taken. Pick another position.')
            else:
                break
        except ValueError:
            print('Invalid input. Please enter a number.')
    pick[answer2] = '⭕'
    print('\n' * 100)
    table(pick)

    # Round 2
    print('player1 choose a position')
    while True:

        try:
            answer3 = int(input('> '))

            if answer3 not in range(1, 10):
                print('Please choose a number between 1 and 9.')
            elif answer3 == answer2 or answer3 == answer1:
                print('That spot is taken. Pick another position.')
            else:
                break
        except ValueError:
            print('Invalid input. Please enter a number.')
    pick[answer3] = '❌'
    print('\n' * 100)
    table(pick)

    print('Player2 choose a position')
    while True:

        try:
            answer4 = int(input('> '))

            if answer4 not in range(1, 10):
                print('Please choose a number between 1 and 9.')
            elif answer4 == answer3 or answer4 == answer2 or answer4 == answer1:
                print('That spot is taken. Pick another position.')
            else:
                break
        except ValueError:
            print('Invalid input. Please enter a number.')
    pick[answer4] = '⭕'
    print('\n' * 100)
    table(pick)

    # Round 3
    print('player1 choose a position')
    while True:

        try:
            answer5 = int(input('> '))

            if answer5 not in range(1, 10):
                print('Please choose a number between 1 and 9.')
            elif answer5 == answer1 or answer5 == answer2 or answer5 == answer3 or answer5 == answer4:
                print('That spot is taken. Pick another position.')
            else:
                break
        except ValueError:
            print('Invalid input. Please enter a number.')
    pick[answer5] = '❌'
    print('\n' * 100)
    table(pick)

    print('Player2 choose a position')
    while True:

        try:
            answer6 = int(input('> '))

            if answer6 not in range(1, 10):
                print('Please choose a number between 1 and 9.')
            elif answer6 == answer5 or answer6 == answer4 or answer6 == answer3 or answer6 == answer2 or answer6 == answer1:
                print('That spot is taken. Pick another position.')
            else:
                break
        except ValueError:
            print('Invalid input. Please enter a number.')
    pick[answer6] = '⭕'
    print('\n' * 100)
    table(pick)

    if winner():
        break


    # Round 4
    print('player1 choose a position')
    while True:

        try:
            answer7 = int(input('> '))

            if answer7 not in range(1, 10):
                print('Please choose a number between 1 and 9.')
            elif answer7 == answer1 or answer7 == answer2 or answer7 == answer3 or answer7 == answer4 or answer7 == answer5 or answer7 == answer6:
                print('That spot is taken. Pick another position.')
            else:
                break
        except ValueError:
            print('Invalid input. Please enter a number.')
    pick[answer7] = '❌'
    print('\n' * 100)
    table(pick)

    print('Player2 choose a position')
    while True:

        try:
            answer8 = int(input('> '))

            if answer8 not in range(1, 10):
                print('Please choose a number between 1 and 9.')
            elif answer8 == answer5 or answer8 == answer4 or answer8 == answer3 or answer8 == answer2 or answer8 == answer1 or answer8 == answer6 or answer8 == answer7:
                print('That spot is taken. Pick another position.')
            else:
                break
        except ValueError:
            print('Invalid input. Please enter a number.')
    pick[answer8] = '⭕'
    print('\n' * 100)
    table(pick)

    if winner():
        break


    # Round 5
    print('player1 choose a position')
    while True:
        turn = 9
        try:
            answer9 = int(input('> '))

            if answer9 not in range(1, 10):
                print('Please choose a number between 1 and 9.')
            elif answer9 == answer1 or answer9 == answer2 or answer9 == answer3 or answer9 == answer4 or answer9 == answer5 or answer9 == answer6 or answer9 == answer7 or answer9 == answer8:
                print('That spot is taken. Pick another position.')
            else:
                break
        except ValueError:
            print('Invalid input. Please enter a number.')
    pick[answer9] = '❌'
    print('\n' * 100)
    table(pick)

    if winner():
        break
    elif turn == 9 and not winner():
        print("It's a tie")
        break

#IF PLAYER-1 IS O

while player1 == 'O':
    print("player2 is '❌'")

    print('Possible positions for your picks')
    print(f'  1 | 2 | 3 ')
    print('-------------')
    print(f'  4 | 5 | 6 ')
    print('-------------')
    print(f'  7 | 8 | 9 ')

    # Round 1
    print('player1 choose a position')
    while True:
        try:
            answer1 = int(input('> '))

            if answer1 not in range(1, 10):
                print('Please choose a number between 1 and 9.')
            else:
                break
        except ValueError:
            print('Invalid input. Please enter a number.')
    pick[answer1] = '⭕'
    print('\n' * 100)
    table(pick)

    print('Player2 choose a position')
    while True:
        try:
            answer2 = int(input('> '))

            if answer2 not in range(1, 10):
                print('Please choose a number between 1 and 9.')
            elif answer2 == answer1:
                print('That spot is taken. Pick another position.')
            else:
                break
        except ValueError:
            print('Invalid input. Please enter a number.')
    pick[answer2] = '❌'
    print('\n' * 100)
    table(pick)

    # Round 2
    print('player1 choose a position')
    while True:
        try:
            answer3 = int(input('> '))

            if answer3 not in range(1, 10):
                print('Please choose a number between 1 and 9.')
            elif answer3 == answer2 or answer3 == answer1:
                print('That spot is taken. Pick another position.')
            else:
                break
        except ValueError:
            print('Invalid input. Please enter a number.')
    pick[answer3] = '⭕'
    print('\n' * 100)
    table(pick)

    print('Player2 choose a position')
    while True:
        try:
            answer4 = int(input('> '))

            if answer4 not in range(1, 10):
                print('Please choose a number between 1 and 9.')
            elif answer4 == answer3 or answer4 == answer2 or answer4 == answer1:
                print('That spot is taken. Pick another position.')
            else:
                break
        except ValueError:
            print('Invalid input. Please enter a number.')
    pick[answer4] = '❌'
    print('\n' * 100)
    table(pick)

    # Round 3
    print('player1 choose a position')
    while True:
        try:
            answer5 = int(input('> '))

            if answer5 not in range(1, 10):
                print('Please choose a number between 1 and 9.')
            elif answer5 == answer1 or answer5 == answer2 or answer5 == answer3 or answer5 == answer4:
                print('That spot is taken. Pick another position.')
            else:
                break
        except ValueError:
            print('Invalid input. Please enter a number.')
    pick[answer5] = '⭕'
    print('\n' * 100)
    table(pick)

    print('Player2 choose a position')
    while True:
        try:
            answer6 = int(input('> '))

            if answer6 not in range(1, 10):
                print('Please choose a number between 1 and 9.')
            elif answer6 == answer5 or answer6 == answer4 or answer6 == answer3 or answer6 == answer2 or answer6 == answer1:
                print('That spot is taken. Pick another position.')
            else:
                break
        except ValueError:
            print('Invalid input. Please enter a number.')
    pick[answer6] = '❌'
    print('\n' * 100)
    table(pick)

    if winner():
        break

    # Round 4
    print('player1 choose a position')
    while True:
        try:
            answer7 = int(input('> '))

            if answer7 not in range(1, 10):
                print('Please choose a number between 1 and 9.')
            elif answer7 == answer1 or answer7 == answer2 or answer7 == answer3 or answer7 == answer4 or answer7 == answer5 or answer7 == answer6:
                print('That spot is taken. Pick another position.')
            else:
                break
        except ValueError:
            print('Invalid input. Please enter a number.')
    pick[answer7] = '⭕'
    print('\n' * 100)
    table(pick)

    print('Player2 choose a position')
    while True:
        try:
            answer8 = int(input('> '))

            if answer8 not in range(1, 10):
                print('Please choose a number between 1 and 9.')
            elif answer8 == answer5 or answer8 == answer4 or answer8 == answer3 or answer8 == answer2 or answer8 == answer1 or answer8 == answer6 or answer8 == answer7:
                print('That spot is taken. Pick another position.')
            else:
                break
        except ValueError:
            print('Invalid input. Please enter a number.')
    pick[answer8] = '❌'
    print('\n' * 100)
    table(pick)

    if winner():
        break

    # Round 5
    print('player1 choose a position')
    while True:
        turn = 9
        try:
            answer9 = int(input('> '))

            if answer9 not in range(1, 10):
                print('Please choose a number between 1 and 9.')
            elif answer9 == answer1 or answer9 == answer2 or answer9 == answer3 or answer9 == answer4 or answer9 == answer5 or answer9 == answer6 or answer9 == answer7 or answer9 == answer8:
                print('That spot is taken. Pick another position.')
            else:
                break
        except ValueError:
            print('Invalid input. Please enter a number.')
    pick[answer9] = '⭕'
    print('\n' * 100)
    table(pick)

    if winner():
        break
    elif turn == 9 and not winner():
        print("It's a tie")
        break


