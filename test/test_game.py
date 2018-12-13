from board import Board
from game import Game


def test_game():
    game = Game()
    assert len(game.white_pieces) == 16
    assert len(game.black_pieces) == 16
    assert all(game.board[f, r].piece is not None for f in Board.FILES for r in Board.RANKS[:2])
    assert all(game.board[f, r].piece is None for f in Board.FILES for r in Board.RANKS[2:6])
    assert all(game.board[f, r].piece is not None for f in Board.FILES for r in Board.RANKS[6:])
