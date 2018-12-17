from square import Square, valid_square_coordinates
from piece import Rook, Colour


def test_is_valid_square_coordinates():
    for f in 'abcdefgh':
        for r in '12345678':
            assert valid_square_coordinates(f, r)
            assert valid_square_coordinates(f + r)
    assert not valid_square_coordinates('i', '8')
    assert not valid_square_coordinates('h', '9')


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
