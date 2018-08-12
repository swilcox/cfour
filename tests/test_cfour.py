from cfour import Board


def test_board_init():
    board = Board()
    assert board.board == [
        "       ",
        "       ",
        "       ",
        "       ",
        "       ",
        "       ",
    ]
    board = Board(columns=3, rows=3, to_win=3)
    assert board.board == [
        "   ",
        "   ",
        "   ",
    ]


def test_board_move():
    board = Board()
    assert board.turn == board.player_1
    board.move(1)
    assert board.board[-1] == " 1     "
    assert board.turn == board.player_2


def test_board_bad_move():
    board = Board()
    board.move(8)
    assert board.board[-1] == "       "


def test_check_row_win():
    board = Board()
    board.board = [
        "       ",
        "1111   ",
        "2121222",
        "1212121",
        "2121221",
        "2212111",
    ]
    assert board._check_row_win() == '1'
    board.board = [
        "       ",
        "       ",
        "21212 2",
        "12121 1",
        "22121 1",
        "2211112",
    ]
    assert board._check_row_win() == '1'


def test_check_column_win():
    board = Board()
    board.board = [
        "       ",
        "112    ",
        "1121222",
        "1212121",
        "1121221",
        "2212111",
    ]
    assert board._check_column_win() == '1'
    board.board = [
        "       ",
        "112  1 ",
        "2121222",
        "1212122",
        "1121222",
        "2212112",
    ]
    assert board._check_column_win() == '2'


def test_diagonal_win():
    board = Board()
    board.board = [
        "       ",
        "       ",
        "1     2",
        "2122121",
        "2212122",
        "2121212",
    ]
    assert board._check_diag_win() == '1'


def test_rev_diagonal_win():
    board = Board()
    board.board = [
        "       ",
        "       ",
        "1     2",
        "2122121",
        "1211222",
        "2122212",
    ]
    assert board._check_diag_win() == '2'


def test_no_win():
    board = Board()
    assert board._check_column_win() == ''
    assert board._check_row_win() == ''
    assert board._check_diag_win() == ''
    board.board = [
        "       ",
        "       ",
        "       ",
        "2122121",
        "1211222",
        "2122212",
    ]
    assert board._check_column_win() == ''
    assert board._check_row_win() == ''
    assert board._check_diag_win() == ''
    board.board = [
        "1212121",
        "2121212",
        "2121212",
        "2122111",
        "1211222",
        "2122212",
    ]
    assert board._check_column_win() == ''
    assert board._check_row_win() == ''
    assert board._check_diag_win() == ''
