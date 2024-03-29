from cfour import Board


def test_board_init():
    board = Board()
    assert board.board == [
        ["0", "0", "0", "0", "0", "0", "0"],
        ["0", "0", "0", "0", "0", "0", "0"],
        ["0", "0", "0", "0", "0", "0", "0"],
        ["0", "0", "0", "0", "0", "0", "0"],
        ["0", "0", "0", "0", "0", "0", "0"],
        ["0", "0", "0", "0", "0", "0", "0"],
    ]
    board = Board(columns=3, rows=3, to_win=3)
    assert board.board == [
        ["0", "0", "0"],
        ["0", "0", "0"],
        ["0", "0", "0"],
    ]


def test_board_move():
    board = Board()
    assert board.turn == board.player_1
    board.move(1)
    assert board.board[-1] == ["0", "1", "0", "0", "0", "0", "0"]
    assert board.turn == board.player_2


def test_board_history():
    board = Board()
    board.move(1)
    assert board.board[-1] == ["0", "1", "0", "0", "0", "0", "0"]
    assert len(board.history()) == 1
    assert board.history()[0][-1] == ["0", "0", "0", "0", "0", "0", "0"]
    board.move(2)
    assert board.board[-1] == ["0", "1", "2", "0", "0", "0", "0"]
    assert board.history()[0][-1] == ["0", "1", "0", "0", "0", "0", "0"]


def test_board_bad_move():
    board = Board()
    board.move(8)
    assert board.board[-1] == ["0", "0", "0", "0", "0", "0", "0"]
    assert len(board.history()) == 0


def test_check_row_win():
    board = Board()
    board.board = [
        ["0", "0", "0", "0", "0", "0", "0"],
        ["1", "1", "1", "1", "0", "0", "0"],
        ["2", "1", "2", "1", "2", "2", "2"],
        ["1", "2", "1", "2", "1", "2", "1"],
        ["2", "1", "2", "1", "2", "2", "1"],
        ["2", "2", "1", "2", "1", "1", "1"],
    ]
    assert board._check_row_win() == "1"
    board.board = [
        ["0", "0", "0", "0", "0", "0", "0"],
        ["0", "0", "0", "0", "0", "0", "0"],
        ["2", "1", "2", "1", "2", "0", "2"],
        ["1", "2", "1", "2", "1", "0", "1"],
        ["2", "2", "1", "2", "1", "0", "1"],
        ["2", "2", "1", "1", "1", "1", "2"],
    ]
    assert board._check_row_win() == "1"


def test_check_column_win():
    board = Board()
    board.board = [
        ["0", "0", "0", "0", "0", "0", "0"],
        ["1", "1", "2", "0", "0", "0", "0"],
        ["1", "1", "2", "1", "2", "2", "2"],
        ["1", "2", "1", "2", "1", "2", "1"],
        ["1", "1", "2", "1", "2", "2", "1"],
        ["2", "2", "1", "2", "1", "1", "1"],
    ]
    assert board._check_column_win() == "1"
    board.board = [
        ["0", "0", "0", "0", "0", "0", "0"],
        ["1", "1", "2", "0", "0", "1", "0"],
        ["2", "1", "2", "1", "2", "2", "2"],
        ["1", "2", "1", "2", "1", "2", "2"],
        ["1", "1", "2", "1", "2", "2", "2"],
        ["2", "2", "1", "2", "1", "1", "2"],
    ]
    assert board._check_column_win() == "2"


def test_diagonal_win():
    board = Board()
    board.board = [
        ["0", "0", "0", "0", "0", "0", "0"],
        ["0", "0", "0", "0", "0", "0", "0"],
        ["1", "0", "0", "0", "0", "0", "2"],
        ["2", "1", "2", "2", "1", "2", "1"],
        ["2", "2", "1", "2", "1", "2", "2"],
        ["2", "1", "2", "1", "2", "1", "2"],
    ]
    assert board._check_diag_win() == "1"


def test_rev_diagonal_win():
    board = Board()
    board.board = [
        ["0", "0", "0", "0", "0", "0", "0"],
        ["0", "0", "0", "0", "0", "0", "0"],
        ["1", "0", "0", "0", "0", "0", "2"],
        ["2", "1", "2", "2", "1", "2", "1"],
        ["1", "2", "1", "1", "2", "2", "2"],
        ["2", "1", "2", "2", "2", "1", "2"],
    ]
    assert board._check_diag_win() == "2"
    board._check_game_over()
    assert board.is_game_over is True


def test_no_win():
    board = Board()
    assert board._check_column_win() == ""
    assert board._check_row_win() == ""
    assert board._check_diag_win() == ""
    board.board = [
        ["0", "0", "0", "0", "0", "0", "0"],
        ["0", "0", "0", "0", "0", "0", "0"],
        ["0", "0", "0", "0", "0", "0", "0"],
        ["2", "1", "2", "2", "1", "2", "1"],
        ["1", "2", "1", "1", "2", "2", "2"],
        ["2", "1", "2", "2", "2", "1", "2"],
    ]
    assert board._check_column_win() == ""
    assert board._check_row_win() == ""
    assert board._check_diag_win() == ""
    board.board = [
        ["1", "2", "1", "2", "1", "2", "1"],
        ["2", "1", "2", "1", "2", "1", "2"],
        ["2", "1", "2", "1", "2", "1", "2"],
        ["2", "1", "2", "2", "1", "1", "1"],
        ["1", "2", "1", "1", "2", "2", "2"],
        ["2", "1", "2", "2", "2", "1", "2"],
    ]
    assert board._check_column_win() == ""
    assert board._check_row_win() == ""
    assert board._check_diag_win() == ""


def test_board_as_str():
    board = Board()
    board.board = [
        ["0", "0", "0", "0", "0", "0", "0"],
        ["0", "0", "0", "0", "0", "0", "0"],
        ["1", "0", "0", "0", "0", "0", "2"],
        ["2", "1", "2", "2", "1", "2", "1"],
        ["1", "2", "1", "1", "2", "2", "2"],
        ["2", "1", "2", "2", "2", "1", "2"],
    ]
    assert (
        board.board_as_str()
        == """
0000000
0000000
1000002
2122121
1211222
2122212
""".strip()
    )
