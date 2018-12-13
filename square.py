from board import Board


class Square:
    def __init__(self, file, rank):
        assert file in Board.FILES
        assert rank in Board.RANKS
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