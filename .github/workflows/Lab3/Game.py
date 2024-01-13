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
