"""Tests the Connect 4 program"""
import numpy
import pytest

from src import connect4


def test_making_board():
    """Check that the correct amount of collumns and rows are created."""
    test_board = connect4.making_board()
    v = test_board == numpy.zeros((6, 7))
    assert v.all()


def test_dropping_piece():
    """Make sure the location of the selection changes the appropriate location on the board."""
    board = connect4.making_board()
    connect4.dropping_piece(board, 0, 0, 1)
    assert board[0][0] == 1


def test_is_location_valid():
    """Check that the board validation test returns
    True if there is a valid space and False if there is not."""
    board = connect4.making_board()
    i = 1
    while i < 6:
        connect4.dropping_piece(board, i, 0, 1)
        i = i + 1

    assert not connect4.is_location_valid(board, 0)
    assert connect4.is_location_valid(board, 1)

@pytest.mark.parametrize(
    "board",
    [
    (numpy.array([[0,0,0,1,0,0,0], [0,0,1,0,0,0,0], [0,1,0,0,0,0,0], [1,0,0,0,0,0,0], [0,0,0,0,0,0,0], [0,0,0,0,0,0,0]])),
    (numpy.array([[1,1,1,1,0,0,0], [0,0,0,0,0,0,0], [0,0,0,0,0,0,0], [0,0,0,0,0,0,0], [0,0,0,0,0,0,0], [0,0,0,0,0,0,0]])),
    (numpy.array([[1,0,0,0,0,0,0], [1,0,0,0,0,0,0], [1,0,0,0,0,0,0], [1,0,0,0,0,0,0], [0,0,0,0,0,0,0], [0,0,0,0,0,0,0]])),
    (numpy.array([[1,0,0,0,0,0,0], [0,1,0,0,0,0,0], [0,0,1,0,0,0,0], [0,0,0,1,0,0,0], [0,0,0,0,0,0,0], [0,0,0,0,0,0,0]])),
    ]
)
def test_winner(board):
    """Check if the winner is not true yet and then check if
    there is a winner after making a move resulting in 4 in a row."""
    assert connect4.winner(board, 1) is True
