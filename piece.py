from enum import Enum


class Colour(Enum):
    WHITE = 0
    BLACK = 1


class Piece:
    def __init__(self, colour):
        assert isinstance(colour, Colour)
        self.colour = colour
        self.square = None


class Pawn(Piece):
    pass


class Rook(Piece):
    pass


class Knight(Piece):
    pass


class Bishop(Piece):
    pass


class Queen(Piece):
    pass


class King(Piece):
    pass