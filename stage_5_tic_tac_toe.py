def grid(list_1):
    print("---------")
    print("|", list_1[0], list_1[1], list_1[2], "|")
    print("|", list_1[3], list_1[4], list_1[5], "|")
    print("|", list_1[6], list_1[7], list_1[8], "|")
    print("---------")


def winner(list_2, name_win):
    win = False
    win_state = name_win * 3
    diagonal_check = [list_2[0] + list_2[4] + list_2[8],
                      list_2[2] + list_2[4] + list_2[6]]
    if win_state in diagonal_check:
        win = True
    else:
        for i in range(3):
            # row check
            if list_2[i] + list_2[i + 1] + list_2[i + 2] == win_state:
                win = True
                break
            # column check
            elif list_2[i] + list_2[i + 3] + list_2[i + 6] == win_state:
                win = True
                break
    return win


def counts(list_3):
    count_x = list_3.count('X')
    count_o = list_3.count('O')
    empty_cells = 9 - count_x - count_o
    count_winners = 0
    the_winner = ''
    if winner(list_3, 'X'):
        count_winners += 1
        the_winner = 'X'
    if winner(list_3, 'O'):
        count_winners += 1
        the_winner = 'O'
    return count_x, count_o, empty_cells, count_winners, the_winner


def states(list_4):

    num_x, num_o, num_empty, num_winners, the_winner = counts(list_4)
    finished = False
    state_message = ""
    if abs(num_x - num_o) >= 2 or num_winners == 2:
        finished = True
        state_message = "Impossible"
    elif num_winners == 1:
        finished = True
        state_message = the_winner + " wins"
    elif num_empty > 0 and num_winners == 0:
        state_message = "Game not finished"
    elif num_empty == 0 and num_winners == 0:
        finished = True
        state_message = "Draw"

    return finished, state_message


def list_position(coords):
    # row_index = coords[0], column_index = coords[1]
    # position = 3 * (row_index - 1) + (column_index - 1)
    position = 3 * int(coords[0]) + int(coords[1]) - 4
    return position


def coords_validity(list_5, coords):
    coords_message = ""
    coords_valid = False
    if coords[0].isnumeric() and coords[1].isnumeric():
        if coords[0] in ['1', '2', '3'] and coords[1] in ['1', '2', '3']:
            list_index = list_position(coords)
            if list_5[list_index] != " ":
                coords_message = "This cell is occupied! Choose another one!"
            else:
                coords_valid = True
        else:
            coords_message = "Coordinates should be from 1 to 3!"
    else:
        coords_message = "You should enter numbers!"
    return coords_valid, coords_message


def moves(list_6, coords, turn):
    list_index = list_position(coords)
    mark = x_or_o(turn)
    list_6[list_index] = mark
    return list_6


def x_or_o(player):
    if player % 2 != 0:
        return "X"
    else:
        return "O"


if __name__ == '__main__':
    # print empty grid from the beginning
    working_list = [" " for _ in range(9)]
    grid(working_list)
    # first player: 'X', second player: 'O'
    next_player = 1
    game_over, state = False, "Game not finished"
    # Game loop: users enter cell coordinates
    while game_over is False:
        valid_coords = False
        while valid_coords is False:
            cell_coords = input("Enter the coordinates: ").split(" ")
            valid_coords, cell_coords_message = coords_validity(working_list, cell_coords)
            print(cell_coords_message)
        working_list = moves(working_list, cell_coords, next_player)
        next_player = (next_player + 1) % 2
        grid(working_list)
        game_over, state = states(working_list)
    print(state)
