from square import Square
from piece import Rook, Colour


def test_set_piece():
    square = Square('a', '1')
    piece = Rook(Colour.WHITE)
    square.set_piece(piece)
    assert square.piece is piece
    assert piece.square is square


def test_remove_piece():
    square = Square('a', '1')
    piece = Rook(Colour.WHITE)
    square.set_piece(piece)
    square.remove_piece()
    assert square.piece is None
    assert piece.square is None
