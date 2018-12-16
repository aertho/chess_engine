class Square:
    def __init__(self, file, rank):
        from board import Board
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

    def __sub__(self, other):
        assert isinstance(other, Square)
        return ord(self.file) - ord(other.file), ord(self.rank) - ord(other.rank)
