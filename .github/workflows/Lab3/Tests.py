import unittest
from Game import Board
from Game import Position


class TestBoard(unittest.TestCase):

    def setUp(self):
        self.board = Board(10, 10)

    # This test case verifies if the player can move to the right by 1 position.
    def test_move_right(self):
        self.board.player_position = Position(1, 1)
        self.board.move_right()
        self.assertEqual(self.board.player_position, Position(2, 1))

    # This test case verifies if the player can move to the left by 1 position.
    def test_move_left(self):
        self.board.player_position = Position(5, 3)
        self.board.move_left()
        self.assertEqual(self.board.player_position, Position(4, 3))

    # This test case verifies if the player can move up by 1 position.
    def test_move_up(self):
        self.board.player_position = Position(5, 3)
        self.board.move_up()
        self.assertEqual(self.board.player_position, Position(5, 2))

    # This test case verifies if the player can move down by 1 position.
    def test_move_down(self):
        self.board.player_position = Position(5, 3)
        self.board.move_down()
        self.assertEqual(self.board.player_position, Position(5, 4))

    # This test case verifies if the player can't move through an obstacle that is positioned above them.
    def test_cannot_move_through_obstacle_up(self):
        self.board.set_obstacle(Position(5, 2))
        self.board.player_position = Position(5, 3)
        self.board.move_up()
        self.assertEqual(self.board.player_position, Position(5, 3))

    # This test case verifies if the player can't move through an obstacle that is positioned to their left.
    def test_cannot_move_through_obstacle_left(self):
        self.board.set_obstacle(Position(4, 3))
        self.board.player_position = Position(5, 3)
        self.board.move_left()
        self.assertEqual(self.board.player_position, Position(5, 3))

    # This test case verifies if the player can't move through an obstacle that is positioned to their right.
    def test_cannot_move_through_obstacle_right(self):
        self.board.set_obstacle(Position(3, 3))
        self.board.player_position = Position(2, 3)
        self.board.move_right()
        self.assertEqual(self.board.player_position, Position(2, 3))

    # This test case verifies if the player can't move through an obstacle that is positioned below them.
    def test_cannot_move_through_obstacle_down(self):
        self.board.set_obstacle(Position(5, 2))
        self.board.player_position = Position(5, 1)
        self.board.move_down()
        self.assertEqual(self.board.player_position, Position(5, 1))

     # This test case verifies if the player can't move outside the playable area of the board.
    def test_move_outside_bounds(self):
        self.board.player_position = Position(0, 5)
        self.board.move_left()
        self.assertEqual(self.board.player_position, Position(0, 5))

        self.board.player_position = Position(9, 5)
        self.board.move_right()
        self.assertEqual(self.board.player_position, Position(9, 5))

        self.board.player_position = Position(5, 0)
        self.board.move_up()
        self.assertEqual(self.board.player_position, Position(5, 0))

        self.board.player_position = Position(5, 9)
        self.board.move_down()
        self.assertEqual(self.board.player_position, Position(5, 9))


if __name__ == "__main__":
    unittest.main()
