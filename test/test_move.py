import pytest

from board import Board
from utils import colour_pieces, set_board
from move import Move, RemovalTransformation, SetTransformation, OrdinaryMove
from piece import Colour, Pawn


@pytest.fixture
def board():
    board = Board()
    white_pieces, black_pieces = [colour_pieces(c) for c in Colour]
    set_board(board, white_pieces, black_pieces)
    return board


def test_move(board):
    move = Move(0, Colour.WHITE)
    from_square = board['e2']
    to_square = board['e4']
    piece = from_square.piece
    move.transformations = [RemovalTransformation(from_square),
                            SetTransformation(to_square, piece)]
    move.apply()
    assert from_square.piece is None
    assert to_square.piece is piece


def test_ordinary_move(board):
    from_square = board['e2']
    to_square = board['e4']
    piece = board['e2'].piece
    move = OrdinaryMove(0, from_square, to_square)
    move.apply()
    assert from_square.piece is None
    assert to_square.piece is piece


def test_ordinary_move_capture():
    board = Board()
    white_pawn = Pawn(Colour.WHITE)
    black_pawn = Pawn(Colour.BLACK)
    board['e4'].set_piece(white_pawn)
    board['d5'].set_piece(black_pawn)
    move = OrdinaryMove(1, board['e4'], board['d5'])
    move.apply()
    assert black_pawn.square is None
    assert board['d5'].piece is white_pawn
    assert board['e4'].piece is None
