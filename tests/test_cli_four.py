from cli_four import GameDisplay


def test_display_game_board():
    g = GameDisplay()
    g.board.board = [
        ['0', '0', '0', '0', '0', '0', '0'],
        ['0', '0', '0', '0', '0', '0', '0'],
        ['1', '0', '0', '0', '0', '0', '2'],
        ['2', '1', '2', '2', '1', '2', '1'],
        ['1', '2', '1', '1', '2', '2', '2'],
        ['2', '1', '2', '2', '2', '1', '2'],
    ]
    good_output = '\n'.join([
        "1 2 3 4 5 6 7",
        "              ",
        "              ",
        "Y           R ",
        "R Y R R Y R Y ",
        "Y R Y Y R R R ",
        "R Y R R R Y R ",
    ])
    assert g.display() == good_output
