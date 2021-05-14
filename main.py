from typing import Set
import numpy as np
from os import system, name

CLEAR_SCREEN_COMMAND = 'cls' if name == 'nt' else 'clear'
PLAY_WITH_OFFSET = True


class colors:
    reset = '\033[0m'

    class fg:
        red = '\033[31m'


class StartGame:
    def __init__(self, play_with_offset) -> None:
        self.offset = 1 if play_with_offset else 0
        self.size = 10
        self.board = np.zeros((10, 10))
        self.fill_rows()
        self.colors = colors()

    def fill_rows(self) -> bool:
        """ Fills the rows of the board in a symmetrical manner

        """
        recurrence = 5
        offset = 0
        while recurrence != 0 and offset != 5:
            for x in range(0, recurrence):
                position_y = 9 - x
                tuple_y = 9 - offset
                self.board[offset][x] = 1
                self.board[tuple_y][position_y] = 2
            recurrence = recurrence - 1
            offset = offset + 1

        return True

    def __repr__(self) -> str:
        current_board = ""
        for y in self.board:
            for x in y:
                current_board += str(x)[0] + " "
            current_board += "\n"
        return current_board

    def make_move(self) -> bool:
        pass

    def check_around(self, coords):
        around = np.array(
            [
                [-1, -1], [0, -1], [1, -1],
                [-1,  0],          [1,  0],
                [-1,  1], [0,  1], [1,  1]
            ]
        )
        x, y = coords
        for i in around:
            pos_y = y + i[1] - self.offset
            pos_x = x + i[0] - self.offset
            print(
                f"Position: [\t{i[0]},\t{i[1]}\t];\tActual Coords: [{pos_x}, {pos_y}];\tValue: {str(self.board[pos_y][pos_x])[0]}")

        self.show_position(coords)

    def valid_position(self, new_coords: tuple) -> bool:
        """Checks if a move is landing on a valid position

        Parameters: 
            new_coords (tuple): The coordinates for the move

        Returns:
            bool: False if invalid. True if valid. 

        """
        x, y = new_coords
        min_allowed_value = self.offset
        max_allowed_value = 10 - self.offset

        # If the value is outside of the board on the left or up, return false
        if x < min_allowed_value or y < min_allowed_value:
            return False
        # If the value is outside of the board on the right or down sides, return false
        if x > max_allowed_value or y > max_allowed_value:
            return False

        # If the position is taken by any piece, return false
        if self.board[y][x] != 0:
            print("Error: Position taken by %d" % self.board[y][x])
            return False
        return True

    def show_position(self, coords):
        coords = (coords[0] - self.offset, coords[1] - self.offset)
        for count_y, value_y in enumerate(self.board):
            for count_x, value_x in enumerate(value_y):
                if (count_x, count_y) == coords:
                    print(self.colors.fg.red + str(value_x)
                          [0] + self.colors.reset, end=" ")
                else:
                    print(str(value_x)[0], end=" ")
            print()


game = StartGame(PLAY_WITH_OFFSET)
system(CLEAR_SCREEN_COMMAND)
game.check_around((3, 3))
