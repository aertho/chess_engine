from board import Board
from piece import Pawn, Rook, Knight, Bishop, Queen, King, Colour


def pieces_of(pieces, piece_type):
    return [p for p in pieces if isinstance(p, piece_type)]


def colour_pieces(colour):
    pieces = [Pawn(colour) for _ in range(8)]
    pieces += [Rook(colour) for _ in range(2)]
    pieces += [Knight(colour) for _ in range(2)]
    pieces += [Bishop(colour) for _ in range(2)]
    pieces += [Queen(colour)]
    pieces += [King(colour)]
    return pieces


def chess_set():
    board = Board()
    white_pieces = colour_pieces(Colour.WHITE)
    black_pieces = colour_pieces(Colour.BLACK)
    return board, white_pieces, black_pieces


def set_board(board, white_pieces, black_pieces):
    for file, p in zip(Board.FILES, pieces_of(white_pieces, Pawn)):
        board[file, '2'].set_piece(p)
    for file, p in zip(['a', 'h'], pieces_of(white_pieces, Rook)):
        board[file, '1'].set_piece(p)
    for file, p in zip(['b', 'g'], pieces_of(white_pieces, Knight)):
        board[file, '1'].set_piece(p)
    for file, p in zip(['c', 'f'], pieces_of(white_pieces, Bishop)):
        board[file, '1'].set_piece(p)
    board['d', '1'].set_piece(pieces_of(white_pieces, Queen)[0])
    board['e', '1'].set_piece((pieces_of(white_pieces, King)[0]))

    for file, p in zip(Board.FILES, pieces_of(black_pieces, Pawn)):
        board[file, '7'].set_piece(p)
    for file, p in zip(['a', 'h'], pieces_of(black_pieces, Rook)):
        board[file, '8'].set_piece(p)
    for file, p in zip(['b', 'g'], pieces_of(black_pieces, Knight)):
        board[file, '8'].set_piece(p)
    for file, p in zip(['c', 'f'], pieces_of(black_pieces, Bishop)):
        board[file, '8'].set_piece(p)
    board['d', '8'].set_piece(pieces_of(black_pieces, Queen)[0])
    board['e', '8'].set_piece((pieces_of(black_pieces, King)[0]))
