import random


def init_matrix():
    matrix = [['_'.rjust(2) for _ in range(10)] for _ in range(10)]
    return matrix


def mark_matrix(letter_position, matrix, letter):
    matrix[letter_position[1]][letter_position[0]] = f' {letter}'


def computer_turn(matrix):
    while True:
        letter_position = random.randrange(10), random.randrange(10)
        if matrix[letter_position[0]][letter_position[1]] == ' _':
            mark_matrix(letter_position, matrix, letter='O')
            outline_matrix(matrix)
            break


def outline_matrix(matrix):
    bar = '  ' + '-' * (10 * 3 + 4)
    print(bar)
    for i in range(9, -1, -1):
        print(str(i + 1).rjust(2) + '| ' + ' '.join(matrix[i]) + '  |')
    print(bar)
    _column_numbers = ' ' + ' '.join([str(i + 1).rjust(2) for i in range(10)])
    print('   ' + _column_numbers + '\n')


def player_input(matrix):
    while True:
        player_move = input('Enter your next move: ').split(' ')
        try:
            if not player_move[0].isnumeric() or not player_move[1].isnumeric():
                continue
        except IndexError:
            continue
        if 0 >= int(player_move[0]) or int(player_move[0]) > 10 or 0 >= int(player_move[1]) or int(player_move[1]) > 10:
            continue
        player_move = int(player_move[1]) - 1, int(player_move[0]) - 1
        if matrix[player_move[1]][player_move[0]] != '_'.rjust(2):
            continue
        elif matrix[player_move[1]][player_move[0]] != ' X' and matrix[player_move[1]][player_move[0]] != ' O':
            mark_matrix(player_move, matrix, 'X')
            break


def game_over_conditions(matrix: list) -> bool:
    """
    win_condition - coordinate, iterated horizontally and vertically plus shift to some direction multiplied by digit
        from 0 to 5. It means, here checked if all of 5 coordinates contain similar elements like 'O' or 'X'
    :param matrix: list with lists of elements like ' X', ' O' or ' _'
    :return: bool
    """
    shift = {'vertical': {'n': 1, 'm': 0}, 'horizontal': {'n': 0, 'm': 1},
             'diagonal_1': {'n': 1, 'm': 1}, 'diagonal_2': {'n': 1, 'm': -1}, 'diagonal_2_continue': {'n': -1, 'm': 1}}
    for i in range(10):
        for j in range(10):
            for k, t in shift.items():
                try:
                    win_condition = [matrix[i + t['n'] * q][j + t['m'] * q] for q in range(5)]
                    if len(set(win_condition)) == 1 and win_condition[0] != ' _' \
                            and i + t['n'] * 4 > -1 and j + t['m'] * 4 > -1:
                        if matrix[i][j].strip() == 'X':
                            outline_matrix(matrix)
                            print('Player lost!')
                        elif matrix[i][j].strip() == 'O':
                            print('Computer lost!')
                        else:
                            print('Unexpected person lost')
                            outline_matrix(matrix)
                        return True
                except IndexError:
                    pass
    return False


def run_game(matrix):
    outline_matrix(matrix)

    while True:
        player_input(matrix)
        if game_over_conditions(matrix):
            break
        computer_turn(matrix)
        if game_over_conditions(matrix):
            break


run_game(matrix=init_matrix())
