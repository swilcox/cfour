
class Board(object):

    player_1 = '1'
    player_2 = '2'
    players = [player_1, player_2]

    def __init__(self, columns=7, rows=6, to_win=4):
        self.columns = columns
        self.rows = rows
        self.to_win = to_win
        self.win_str = {p: p * self.to_win for p in self.players}
        self.board = [['0' for x in range(columns)] for y in range(rows)]
        self.turn = self.player_1
        self.winner = ''
        self.is_game_over = False

    @property
    def possible_moves(self) -> list:
        columns = []
        if not self.is_game_over:
            for row in self.board[::-1]:
                columns.extend([x for x, slot in enumerate(row) if slot == '0' and x not in columns])
        return columns

    def _check_row_win(self) -> str:
        for row in self.board:
            for player in self.players:
                if self.win_str[player] in ''.join([c for c in row]):
                    return player
        return ''

    def _check_column_win(self) -> str:
        for column in range(self.columns):
            for player in self.players:
                if self.win_str[player] in ''.join([row[column] for row in self.board]):
                    return player
        return ''

    def _check_diag_win(self) -> str:
        for column in range((self.columns - self.to_win) + 1):
            for row_offset in range((self.rows - self.to_win) + 1):
                for player in self.players:
                    diag = ''.join([row[column + x] for x, row in enumerate(self.board[row_offset:]) if (column + x) < self.columns])
                    rev_diag = ''.join([row[-(column + x + 1)] for x, row in enumerate(self.board[row_offset:]) if -(column + x + 1) > -self.columns])
                    if self.win_str[player] in diag or self.win_str[player] in rev_diag:
                        return player
        return ''

    def _check_game_over(self):
        winner = self._check_row_win() or self._check_column_win() or self._check_diag_win()
        if winner:
            self.turn = ''
            self.winner = winner
            self.is_game_over = True
        if not len(self.possible_moves):
            self.turn = ''
            self.is_game_over = True

    def _switch_turns(self):
        if not self.is_game_over:
            self.turn = self.player_2 if self.turn == self.player_1 else self.player_1
    
    def move(self, column):
        if column in self.possible_moves:
            for row in self.board[::-1]:
                if row[column] == '0':
                    row[column] = self.turn
                    self._check_game_over()
                    self._switch_turns()
                    return
