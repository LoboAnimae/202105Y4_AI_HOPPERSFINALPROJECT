import numpy as np
from os import system
from constants import GameParameters, colors


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
        current_board += "\t"
        for i in range(0, 10):
            current_board += f"{i + self.offset} "
        current_board += "\n"
        current_board += "\t"
        for i in range(0, len(current_board) - 1):
            current_board += "="
        current_board += "\n"

        for index, y in enumerate(self.board):
            current_board += f"{index + self.offset}\t|"
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

    def show_gridline_section(self, variant=1):
        if variant == 1:
            for i in range(0, 20):
                index = "{}{}".format('\t' if i == 0 else '', '=')
                end = "{}".format('' if i != 20 - 1 else '\n')
                print(index, end=end)
        else:
            for i in range(0, 10):
                index = "{}{}".format('\t' if i == 0 else '', i + self.offset)
                end = "{}".format(' ' if i != 10 - 1 else '\n')
                print(index, end=end)

    def print_grid(self, inverse=False):
        if not inverse:
            self.show_gridline_section(2)
            self.show_gridline_section()
        else:
            self.show_gridline_section()
            self.show_gridline_section(2)

    def show_position(self, coords):
        self.print_grid()

        coords = (coords[0] - self.offset, coords[1] - self.offset)
        for count_y, value_y in enumerate(self.board):
            print(count_y + self.offset,
                  end=f"{' ' if len(str(count_y + self.offset)) == 1 else ''}|\t")
            for count_x, value_x in enumerate(value_y):
                if (count_x, count_y) == coords:
                    print(self.colors.fg.red + str(value_x)
                          [0] + self.colors.reset, end=" ")
                else:
                    print(str(value_x)[0], end=" ")
            print(f"\t|{count_y + self.offset}")

        self.print_grid(inverse=True)


game = StartGame(GameParameters.PLAY_WITH_OFFSET)
system(GameParameters.CLEAR_SCREEN_COMMAND)
game.check_around((3, 3))
# print(game)
