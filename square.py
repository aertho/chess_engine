def valid_square_coordinates(file, rank=''):
    from board import Board
    if not ((len(file) == 1 and len(rank) == 1) or (len(file) == 2 and len(rank) == 0)):
        return False
    if len(file) == 2:
        file, rank = file[:]
    return file in Board.FILES and rank in Board.RANKS


class Square:
    def __init__(self, file, rank):
        assert valid_square_coordinates(file, rank)
        self.file = file
        self.rank = rank
        self.piece = None

    def __repr__(self):
        return '<Square(file={}, rank={})>'.format(self.file, self.rank)

    def set_piece(self, piece):
        assert piece.square is None
        self.piece = piece
        self.piece.square = self

    def remove_piece(self):
        self.piece.square = None
        self.piece = None

    def __sub__(self, other):
        assert isinstance(other, Square)
        return ord(self.file) - ord(other.file), ord(self.rank) - ord(other.rank)
