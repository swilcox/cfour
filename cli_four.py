from cfour import Board

PLAYER1_CHR = 'Y'
PLAYER2_CHR = 'R'


class GameDisplay(object):
    """Game Display class. Initializes a board and displays status of the board."""

    def __init__(self):
        self.board = Board()
    
    def display(self):
        """display the current status of the board"""
        lines = []
        lines.append(' '.join([str(x + 1) for x in range(self.board.columns)]))
        for row in self.board.board:
            new_row = ''.join([c for c in row])
            new_row = new_row.replace('0', '  ')
            new_row = new_row.replace('1', f'{PLAYER1_CHR} ')
            new_row = new_row.replace('2', f'{PLAYER2_CHR} ')
            lines.append(new_row)
        return '\n'.join(lines)


def main():
    game = GameDisplay()
    print(game.display())
    while not game.board.is_game_over:
        col = input(f'player {game.board.turn} enter column selection:')
        game.board.move(int(col) - 1)
        print(game.display())
    print('Game Over')
    if game.board.winner:
        print(f'Winner is Player {game.board.winner}')
    else:
        print(f'Ended in a draw')


if __name__ == "__main__":
    main()
