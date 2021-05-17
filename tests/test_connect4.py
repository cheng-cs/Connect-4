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
        (numpy.array([[0, 0, 0, 1, 0, 0, 0], [0, 0, 1, 0, 0, 0, 0], [0, 1, 0, 0, 0, 0, 0],
                      [1, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0]])),
        (numpy.array([[1, 1, 1, 1, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0],
                      [0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0]])),
        (numpy.array([[1, 0, 0, 0, 0, 0, 0], [1, 0, 0, 0, 0, 0, 0], [1, 0, 0, 0, 0, 0, 0],
                      [1, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0]])),
        (numpy.array([[1, 0, 0, 0, 0, 0, 0], [0, 1, 0, 0, 0, 0, 0], [0, 0, 1, 0, 0, 0, 0],
                      [0, 0, 0, 1, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0]])),
    ]
)
def test_winner_true(board):
    """Check that each winning board type returns True."""
    assert connect4.winner(board, 1) is True


def test_winner_false():
    """Check that a board type that has not won is not True"""
    assert connect4.winner(connect4.making_board(), 1) is None


def test_run_turn():
    """Check that run turn correctly places the piece and evaluates the state of the game after."""
    board = (numpy.array([[0, 1, 1, 1, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0],
                          [0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0]]))
    empty_board = connect4.making_board()
    connect4.input = lambda x: '0'
    assert connect4.run_turn(board, 1) is True
    assert connect4.run_turn(empty_board, 1) is None
