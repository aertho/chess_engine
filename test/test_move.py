import pytest

from board import Board
from utils import colour_pieces, set_board
from move import Move, RemovalTransformation, SetTransformation, OrdinaryMove, CaptureMove
from piece import Colour, Pawn


@pytest.fixture
def board():
    board = Board()
    white_pieces, black_pieces = [colour_pieces(c) for c in Colour]
    set_board(board, white_pieces, black_pieces)
    return board


def test_move(board):
    from_square = 'e2'
    to_square = 'e4'
    move = Move(0, Colour.WHITE, from_square, to_square)
    piece = board[from_square].piece
    move.transformations.append(RemovalTransformation(from_square))
    move.transformations.append(SetTransformation(to_square, move.transformations[0]))
    move.apply(board)
    assert board[from_square].piece is None
    assert board[to_square].piece is piece


def test_ordinary_move(board):
    from_square = 'e2'
    to_square = 'e4'
    piece = board[from_square].piece
    move = OrdinaryMove(0, Colour.WHITE, from_square, to_square)
    move.apply(board)
    assert board[from_square].piece is None
    assert board[to_square].piece is piece


def test_ordinary_move_capture():
    board = Board()
    white_pawn = Pawn(Colour.WHITE)
    black_pawn = Pawn(Colour.BLACK)
    board['e4'].set_piece(white_pawn)
    board['d5'].set_piece(black_pawn)
    move = CaptureMove(1, Colour.WHITE, 'e4', 'd5')
    move.apply(board)
    assert black_pawn.square is None
    assert board['d5'].piece is white_pawn
    assert board['e4'].piece is None
