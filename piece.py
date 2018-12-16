from enum import Enum


def is_horizontal(change):
    return change[0] != 0 and change[1] == 0


def is_vertical(change):
    return change[1] != 0 and change[0] == 0


def is_diagonal(change):
    return abs(change[1]) == abs(change[0])


class Colour(Enum):
    WHITE = 0
    BLACK = 1


class Piece:
    def __init__(self, colour):
        assert isinstance(colour, Colour)
        self.colour = colour
        self.square = None

    def __repr__(self):
        return "<{} {}>".format(self.colour, self.__class__.__name__)

    def valid_change(self, to_square, is_capture):
        raise NotImplementedError


class Pawn(Piece):
    def valid_change(self, to_square, is_capture):
        change = to_square - self.square
        if self.colour == Colour.WHITE:
            if is_capture:
                return change in ((1, 1), (-1, 1))
            if self.square.rank == '2':
                return change in ((0, 1), (0, 2))
            return change == (0, 1)
        if self.colour.BLACK == Colour.BLACK:
            if is_capture:
                return change in ((1, -1), (-1, -1))
            if self.square.rank == '7':
                return change in ((0, -1), (0, -2))
            return change == (0, -1)


class Rook(Piece):
    def valid_change(self, to_square, is_capture):
        change = to_square - self.square
        return is_horizontal(change) or is_vertical(change)


class Knight(Piece):
    def valid_change(self, to_square, is_capture):
        change = to_square - self.square
        return (abs(change[0]) == 1 and abs(change[1]) == 2) or (abs(change[0]) == 2 and abs(change[1]) == 1)


class Bishop(Piece):
    def valid_change(self, to_square, is_capture):
        change = to_square - self.square
        return is_diagonal(change)


class Queen(Piece):
    def valid_change(self, to_square, is_capture):
        change = to_square - self.square
        return is_diagonal(change) or is_horizontal(change) or is_vertical(change)


class King(Piece):
    def valid_change(self, to_square, is_capture):
        change = to_square - self.square
        return change != (0, 0) and abs(change[0]) <= 1 and abs(change[1]) <= 1
