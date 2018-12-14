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
        assert square.piece is None
        super().__init__()
        self.square = square
        self.piece = piece

    def apply(self):
        super().apply()
        self.square.set_piece(self.piece)


class RemovalTransformation(Transformation):
    def __init__(self, square):
        assert square.piece is not None
        super().__init__()
        self.square = square
        self.piece = self.square.piece

    def apply(self):
        super().apply()
        self.square.remove_piece()


class Move:
    def __init__(self):
        self.transformations = []

    def apply(self):
        for t in self.transformations:
            t.apply()
