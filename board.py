class Square:
    def __init__(self, file, rank):
        self.file = file
        self.rank = rank
        self.piece = None

    def __repr__(self):
        return '<Square(file={}, rank={})>'.format(self.file, self.rank)


class Board:
    FILES = 'abcdefgh'
    RANKS = '12345678'

    def __init__(self):
        self.squares = [[Square(f, r) for f in Board.FILES] for r in Board.RANKS]

    def __getitem__(self, item):
        file, rank = item
        assert file in Board.FILES
        assert rank in Board.RANKS
        file = ord(file) - ord('a')
        rank = ord(rank) - ord('1')
        return self.squares[rank][file]
