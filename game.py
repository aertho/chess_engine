from board import Board
from piece import Pawn, Colour, Rook, Knight, Bishop, Queen, King


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


class Game:
    def __init__(self):
        self.board, self.white_pieces, self.black_pieces = chess_set()
        self.reset_game()

    def reset_game(self):
        for file, p in zip(Board.FILES, pieces_of(self.white_pieces, Pawn)):
            self.board[file, '2'].set_piece(p)
        for file, p in zip(['a', 'h'], pieces_of(self.white_pieces, Rook)):
            self.board[file, '1'].set_piece(p)
        for file, p in zip(['b', 'g'], pieces_of(self.white_pieces, Knight)):
            self.board[file, '1'].set_piece(p)
        for file, p in zip(['c', 'f'], pieces_of(self.white_pieces, Bishop)):
            self.board[file, '1'].set_piece(p)
        self.board['d', '1'].set_piece(pieces_of(self.white_pieces, Queen)[0])
        self.board['e', '1'].set_piece((pieces_of(self.white_pieces, King)[0]))

        for file, p in zip(Board.FILES, pieces_of(self.black_pieces, Pawn)):
            self.board[file, '7'].set_piece(p)
        for file, p in zip(['a', 'h'], pieces_of(self.black_pieces, Rook)):
            self.board[file, '8'].set_piece(p)
        for file, p in zip(['b', 'g'], pieces_of(self.black_pieces, Knight)):
            self.board[file, '8'].set_piece(p)
        for file, p in zip(['c', 'f'], pieces_of(self.black_pieces, Bishop)):
            self.board[file, '8'].set_piece(p)
        self.board['d', '8'].set_piece(pieces_of(self.black_pieces, Queen)[0])
        self.board['e', '8'].set_piece((pieces_of(self.black_pieces, King)[0]))
