import pytest
import numpy

from src import connect4


def test_making_board():
    """Check that the correct amount of collumns and rows are created."""
    test_board = connect4.making_board()
    v = test_board == numpy.zeros((6,7))
    assert v.all()


def test_dropping_piece():
    board = connect4.making_board()
    connect4.dropping_piece(board, 0, 0, 1)
    assert board[0][0] == 1
