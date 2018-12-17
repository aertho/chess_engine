from square import valid_square_coordinates


class Transformation:
    def __init__(self):
        self.square = None
        self.piece = None
        self.been_applied = False

    def apply(self, board):
        assert not self.been_applied
        self.been_applied = True


class SetTransformation(Transformation):
    def __init__(self, square, removal_transformation):
        super().__init__()
        self.square = square
        self.removal_transformation = removal_transformation

    def apply(self, board):
        assert board[self.square].piece is None
        super().apply(board)
        self.piece = self.removal_transformation.piece
        board[self.square].set_piece(self.piece)


class RemovalTransformation(Transformation):
    def __init__(self, square):
        super().__init__()
        self.square = square

    def apply(self, board):
        assert board[self.square].piece is not None
        super().apply(board)
        self.piece = board[self.square].piece
        board[self.square].remove_piece()


class Move:
    def __init__(self, number, colour, from_square, to_square):
        assert valid_square_coordinates(from_square)
        assert valid_square_coordinates(to_square)
        self.number = number
        self.colour = colour
        self.from_square = from_square
        self.to_square = to_square
        self.transformations = []

    def apply(self, board):
        assert board[self.from_square].piece is not None
        assert board[self.from_square].piece.colour == self.colour
        for t in self.transformations:
            t.apply(board)


class OrdinaryMove(Move):
    def __init__(self, number, colour, from_square, to_square):
        super().__init__(number, colour, from_square, to_square)
        self.from_square = from_square
        self.to_square = to_square
        self.transformations.append(RemovalTransformation(from_square))
        self.transformations.append(SetTransformation(to_square, self.transformations[0]))

    def apply(self, board):
        assert board[self.from_square].piece.valid_change(board[self.to_square], is_capture=False)
        assert board[self.to_square].piece is None
        super().apply(board)


class CaptureMove(Move):
    def __init__(self, number, colour, from_square, to_square):
        super().__init__(number, colour, from_square, to_square)
        self.transformations.append(RemovalTransformation(from_square))
        self.transformations.append(RemovalTransformation(to_square))
        self.transformations.append(SetTransformation(to_square, self.transformations[0]))

    def apply(self, board):
        assert board[self.from_square].piece.valid_change(board[self.to_square], is_capture=True)
        assert board[self.to_square].piece is not None
        assert board[self.to_square].piece.colour != self.colour
        super().apply(board)
