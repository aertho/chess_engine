from piece import Pawn, Colour, Rook, Knight, Bishop, Queen
from square import Square


def test_pawn_valid_change_white_rank2():
    current_square = Square('e', '2')
    piece = Pawn(Colour.WHITE)
    current_square.set_piece(piece)
    to_square = Square('e', '3')
    assert piece.valid_change(to_square, is_capture=False)
    to_square = Square('e', '4')
    assert piece.valid_change(to_square, is_capture=False)


def test_pawn_valid_change_white_any_rank():
    current_square = Square('e', '3')
    piece = Pawn(Colour.WHITE)
    current_square.set_piece(piece)
    to_square = Square('e', '4')
    assert piece.valid_change(to_square, is_capture=False)
    to_square = Square('e', '5')
    assert not piece.valid_change(to_square, is_capture=False)


def test_pawn_valid_change_white_capture():
    current_square = Square('e', '3')
    piece = Pawn(Colour.WHITE)
    current_square.set_piece(piece)
    to_square = Square('d', '4')
    to_square.set_piece(Pawn(Colour.BLACK))
    assert piece.valid_change(to_square, is_capture=True)
    to_square = Square('f', '4')
    to_square.set_piece(Pawn(Colour.BLACK))
    assert piece.valid_change(to_square, is_capture=True)
    to_square = Square('e', '4')
    to_square.set_piece(Pawn(Colour.BLACK))
    assert not piece.valid_change(to_square, is_capture=True)


def test_pawn_valid_change_black_rank7():
    current_square = Square('e', '7')
    piece = Pawn(Colour.BLACK)
    current_square.set_piece(piece)
    to_square = Square('e', '6')
    assert piece.valid_change(to_square, is_capture=False)
    to_square = Square('e', '5')
    assert piece.valid_change(to_square, is_capture=False)


def test_pawn_valid_change_black_any_rank():
    current_square = Square('e', '6')
    piece = Pawn(Colour.BLACK)
    current_square.set_piece(piece)
    to_square = Square('e', '5')
    assert piece.valid_change(to_square, is_capture=False)
    to_square = Square('e', '4')
    assert not piece.valid_change(to_square, is_capture=False)


def test_pawn_valid_change_black_capture():
    current_square = Square('e', '6')
    piece = Pawn(Colour.BLACK)
    current_square.set_piece(piece)
    to_square = Square('d', '5')
    to_square.set_piece(Pawn(Colour.BLACK))
    assert piece.valid_change(to_square, is_capture=True)
    to_square = Square('f', '5')
    to_square.set_piece(Pawn(Colour.BLACK))
    assert piece.valid_change(to_square, is_capture=True)
    to_square = Square('e', '4')
    to_square.set_piece(Pawn(Colour.BLACK))
    assert not piece.valid_change(to_square, is_capture=True)


def test_rook():
    current_square = Square('e', '4')
    piece = Rook(Colour.WHITE)
    current_square.set_piece(piece)
    to_square = Square('e', '8')
    assert piece.valid_change(to_square, is_capture=False)
    to_square = Square('e', '1')
    assert piece.valid_change(to_square, is_capture=False)
    to_square = Square('a', '4')
    assert piece.valid_change(to_square, is_capture=False)
    to_square = Square('h', '4')
    assert piece.valid_change(to_square, is_capture=False)
    to_square = Square('f', '5')
    assert not piece.valid_change(to_square, is_capture=False)


def test_knight():
    current_square = Square('e', '4')
    piece = Knight(Colour.WHITE)
    current_square.set_piece(piece)
    to_square = Square('f', '6')
    assert piece.valid_change(to_square, is_capture=False)
    to_square = Square('f', '2')
    assert piece.valid_change(to_square, is_capture=False)
    to_square = Square('d', '6')
    assert piece.valid_change(to_square, is_capture=False)
    to_square = Square('d', '2')
    assert piece.valid_change(to_square, is_capture=False)
    to_square = Square('g', '3')
    assert piece.valid_change(to_square, is_capture=False)
    to_square = Square('g', '5')
    assert piece.valid_change(to_square, is_capture=False)
    to_square = Square('c', '3')
    assert piece.valid_change(to_square, is_capture=False)
    to_square = Square('c', '5')
    assert piece.valid_change(to_square, is_capture=False)
    to_square = Square('a', '5')
    assert not piece.valid_change(to_square, is_capture=False)


def test_bishop():
    current_square = Square('e', '4')
    piece = Bishop(Colour.WHITE)
    current_square.set_piece(piece)
    to_square = Square('h', '1')
    assert piece.valid_change(to_square, is_capture=False)
    to_square = Square('b', '1')
    assert piece.valid_change(to_square, is_capture=False)
    to_square = Square('a', '8')
    assert piece.valid_change(to_square, is_capture=False)
    to_square = Square('h', '7')
    assert piece.valid_change(to_square, is_capture=False)
    to_square = Square('g', '7')
    assert not piece.valid_change(to_square, is_capture=False)


def test_queen():
    current_square = Square('e', '4')
    piece = Queen(Colour.WHITE)
    current_square.set_piece(piece)
    to_square = Square('h', '1')
    assert piece.valid_change(to_square, is_capture=False)
    to_square = Square('e', '1')
    assert piece.valid_change(to_square, is_capture=False)
    to_square = Square('a', '4')
    assert piece.valid_change(to_square, is_capture=False)
    to_square = Square('h', '4')
    assert piece.valid_change(to_square, is_capture=False)
    to_square = Square('h', '1')
    assert piece.valid_change(to_square, is_capture=False)
    to_square = Square('b', '1')
    assert piece.valid_change(to_square, is_capture=False)
    to_square = Square('a', '8')
    assert piece.valid_change(to_square, is_capture=False)
    to_square = Square('h', '7')
    assert piece.valid_change(to_square, is_capture=False)
    to_square = Square('a', '5')
    assert not piece.valid_change(to_square, is_capture=False)


def test_king():
    current_square = Square('e', '4')
    piece = Queen(Colour.WHITE)
    current_square.set_piece(piece)
    to_square = Square('e', '5')
    assert piece.valid_change(to_square, is_capture=False)
    to_square = Square('e', '3')
    assert piece.valid_change(to_square, is_capture=False)
    to_square = Square('f', '3')
    assert piece.valid_change(to_square, is_capture=False)
    to_square = Square('f', '4')
    assert piece.valid_change(to_square, is_capture=False)
    to_square = Square('f', '5')
    assert piece.valid_change(to_square, is_capture=False)
    to_square = Square('d', '3')
    assert piece.valid_change(to_square, is_capture=False)
    to_square = Square('d', '4')
    assert piece.valid_change(to_square, is_capture=False)
    to_square = Square('d', '5')
    assert piece.valid_change(to_square, is_capture=False)
    to_square = Square('d', '6')
    assert not piece.valid_change(to_square, is_capture=False)
