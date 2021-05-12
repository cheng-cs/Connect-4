import numpy as np
import sys


# this is all calculated using pixels
# use `pip install pygame (my version is 2.0.1)`

# to make the code more presentiable
# We use 2 global variable

ROW = 6
COLUMN = 7


def making_board():
    board = np.zeros((ROW, COLUMN))
    return board


def dropping_piece(board, row, selection, piece):
    board[row][selection] = piece


def is_location_valid(board, selection):
    # making sure the selection from the player is legal
    return board[ROW - 1][selection] == 0


def get_next_row(board, selection):
    # if there are spaces left on the board, this will let us put something in it
    for r in range(ROW):
        if board[r][selection] == 0:
            return r


def print_board(board):
    # print board so that it display the right thing
    # reversing board, can't use flip due to numpy version
    reverse_board = board[::-1]
    print(reverse_board)


def winner(board, piece):
    # check all horizontal locations on the board for a win
    # reason for 3 is becuase in the board the last 3 COLUMN does not work. so we take it off
    # this will make more sense when you run the code. Its hard explaining using words.
    for c in range(COLUMN - 3):
        for r in range(ROW):
            if (
                board[r][c] == piece
                and board[r][c + 1] == piece
                and board[r][c + 2] == piece
                and board[r][c + 3] == piece
            ):
                return True

    # Checking all vertical locations on the board for a win
    for c in range(COLUMN):
        for r in range(ROW - 3):
            if (
                board[r][c] == piece
                and board[r + 1][c] == piece
                and board[r + 2][c] == piece
                and board[r + 3][c] == piece
            ):
                return True

    # Checking postitively sloped
    for c in range(COLUMN - 3):
        for r in range(ROW - 3):
            if (
                board[r][c] == piece
                and board[r + 1][c] + 1 == piece
                and board[r + 2][c + 2] == piece
                and board[r + 3][c + 3] == piece
            ):
                return True

    # Checking negatively spoped
    for c in range(COLUMN - 3):
        for r in range(3, ROW):
            if (
                board[r][c] == piece
                and board[r - 1][c] + 1 == piece
                and board[r - 2][c + 2] == piece
                and board[r - 3][c + 3] == piece
            ):
                return True


def run_turn(board, turn):
    selection = int(input(f"Player {turn} Make your move (0-6):"))

    if is_location_valid(board, selection):
        # if there is a space on our board that is not occupied, than we can move on
        row = get_next_row(board, selection)
        # allows us to drop pieces into said spaces
        dropping_piece(board, row, selection, turn)

        if winner(board, turn):
            print(f"Player {turn} Wins")
            return True


if __name__ == "__main__":
    board = making_board()
    print_board(board)
    game_over = False
    turn = 0

    while not game_over:
        game_over = run_turn(board, turn + 1)
        print_board(board)
        turn += 1
        # taking the remiander and % by 2
        # the goal here is to allow player 1 and 2 to play
        turn = turn % 2
    input()
