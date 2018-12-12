from board import Board


def test_board():
    board = Board()
    assert len(board.squares) == 8
    for rank in range(8):
        assert len(board.squares[rank]) == 8
        for file in range(8):
            assert board.squares[rank][file].rank == chr(ord('1') + rank)
            assert board.squares[rank][file].file == chr(ord('a') + file)


def test___get_item__():
    board = Board()
    for r in Board.RANKS:
        for f in Board.FILES:
            assert board[f, r].rank == r
            assert board[f, r].file == f
            assert board[f+r].rank == r
            assert board[f+r].file == f
