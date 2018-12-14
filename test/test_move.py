import pytest

from board import Board
from game import colour_pieces, set_board
from move import Move, RemovalTransformation, SetTransformation
from piece import Colour


@pytest.fixture
def board():
    board = Board()
    white_pieces, black_pieces = [colour_pieces(c) for c in Colour]
    set_board(board, white_pieces, black_pieces)
    return board


def test_move_apply(board):
    move = Move()
    from_square = board['e2']
    to_square = board['e4']
    piece = from_square.piece
    move.transformations = [RemovalTransformation(from_square),
                            SetTransformation(to_square, piece)]
    move.apply()
    assert from_square.piece is None
    assert to_square.piece is piece
