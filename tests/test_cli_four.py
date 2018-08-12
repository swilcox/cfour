from cli_four import GameBoard


def test_display_game_board():
    g = GameBoard()
    g.gb.board = [
        "       ",
        "       ",
        "1     2",
        "2122121",
        "1211222",
        "2122212",
    ]
    good_output = '\n'.join([
        "1 2 3 4 5 6 7",
        "              ",
        "              ",
        "®           ¤ ",
        "¤ ® ¤ ¤ ® ¤ ® ",
        "® ¤ ® ® ¤ ¤ ¤ ",
        "¤ ® ¤ ¤ ¤ ® ¤ ",
    ])
    assert g.display() == good_output
