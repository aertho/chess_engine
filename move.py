class Transformation:
    def __init__(self):
        self.square = None
        self.piece = None
        self.been_applied = False

    def apply(self):
        assert not self.been_applied
        self.been_applied = True


class SetTransformation(Transformation):
    def __init__(self, square, piece):
        super().__init__()
        self.square = square
        self.piece = piece

    def apply(self):
        assert self.square.piece is None
        super().apply()
        self.square.set_piece(self.piece)


class RemovalTransformation(Transformation):
    def __init__(self, square):
        super().__init__()
        self.square = square
        self.piece = self.square.piece

    def apply(self):
        assert self.square.piece is not None
        super().apply()
        self.square.remove_piece()


class Move:
    def __init__(self, number, colour):
        self.number = number
        self.colour = colour
        self.transformations = []

    def apply(self):
        for t in self.transformations:
            t.apply()


class OrdinaryMove(Move):
    def __init__(self, number, from_square, to_square, is_capture=False):
        assert from_square.piece is not None
        assert from_square.piece.valid_change(to_square, is_capture)
        super().__init__(number, from_square.piece.colour)
        self.from_square = from_square
        self.to_square = to_square
        self.piece = from_square.piece
        self.is_capture = is_capture
        self.transformations.append(RemovalTransformation(from_square))
        if is_capture:
            assert to_square.piece is not None
            assert to_square.piece.colour != from_square.piece.colour
            self.transformations.append((RemovalTransformation(to_square)))
        self.transformations.append(SetTransformation(to_square, from_square.piece))
