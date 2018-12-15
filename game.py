from piece import Colour
from utils import chess_set, set_board


class Game:
    def __init__(self):
        self.board, self.white_pieces, self.black_pieces = chess_set()
        self.reset_game()
        self.white_moves = []
        self.black_moves = []

    @property
    def turn(self):
        if len(self.white_moves) > len(self.black_moves):
            return Colour.BLACK
        return Colour.WHITE

    def reset_game(self):
        set_board(self.board, self.white_pieces, self.black_pieces)
