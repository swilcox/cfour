from cfour import Board


class GameDisplay(object):
    def __init__(self):
        self.board = Board()
    
    def display(self):
        lines = []
        lines.append(' '.join([str(x + 1) for x in range(self.board.columns)]))
        for row in self.board.board:
            new_row = row.replace(' ', '  ')
            new_row = new_row.replace('1', '\xAE ')
            new_row = new_row.replace('2', '\xA4 ')
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