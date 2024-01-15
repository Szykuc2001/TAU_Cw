import random
from collections import namedtuple

Position = namedtuple('Position', ['x', 'y'])


class Board:
    def __init__(self, height, width):
        self.height = height
        self.width = width
        self.board = self.generate_board()
        self.start = None
        self.stop = None
        self.player_position = None

    def generate_board(self):
        return [['.' for _ in range(self.width)] for _ in range(self.height)]

    def place_start_stop(self):
        self.start = (random.randint(0, self.height - 1), 0)
        self.stop = (random.randint(0, self.height - 1), self.width - 1)

    def place_obstacles(self):
        for _ in range(self.height * self.width // 4):
            x, y = random.randint(0, self.height - 1), random.randint(0, self.width - 1)
            if self.board[x][y] not in ['A', 'B']:
                self.board[x][y] = 'X'

    def print_board(self):
        for row in self.board:
            print(''.join(row))

    @property
    def player_position(self):
        return self._player_position

    @player_position.setter
    def player_position(self, value):
        self._player_position = value
        self.board[value.x][value.y] = 'P'

    def set_obstacle(self, position):
        self.board[position.x][position.y] = 'X'

    def move_up(self):
        if self.player_position.y > 0 and self.board[self.player_position.x][self.player_position.y - 1] != 'X':
            self.player_position = Position(self.player_position.x, self.player_position.y - 1)
        else:
            self.player_position = Position(self.player_position.x, self.player_position.y)

    def move_down(self):
        if self.player_position.y < self.width - 1 and self.board[self.player_position.x][
            self.player_position.y + 1] != 'X':
            self.player_position = Position(self.player_position.x, self.player_position.y + 1)
        else:
            self.player_position = Position(self.player_position.x, self.player_position.y)

    def move_left(self):
        if self.player_position.x > 0 and self.board[self.player_position.x - 1][self.player_position.y] != 'X':
            self.player_position = Position(self.player_position.x - 1, self.player_position.y)
        else:
            self.player_position = Position(self.player_position.x, self.player_position.y)

    def move_right(self):
        if self.player_position.x < self.height - 1 and self.board[self.player_position.x + 1][
            self.player_position.y] != 'X':
            self.player_position = Position(self.player_position.x + 1, self.player_position.y)
        else:
            self.player_position = Position(self.player_position.x, self.player_position.y)

    def is_game_won(self):
        return self.player_position.x == self.stop.x and self.player_position.y == self.stop.y

    @player_position.setter
    def player_position(self, value):
        self._player_position = value


if __name__ == "__main__":
    board = Board(10, 10)
    board.print_board()
    board.move_right()
    board.print_board()
    print(board.is_game_won())
