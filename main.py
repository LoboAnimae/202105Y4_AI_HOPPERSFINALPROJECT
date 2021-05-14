import numpy as np
from os import system, name
CLEAR_SCREEN_COMMAND = 'cls' if name == 'nt' else 'clear'


class colors:
    reset = '\033[0m'
    
    class fg:
        red = '\033[31m'

class StartGame:
    def __init__(self) -> None:
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

    def valid_position(self, new_coords=(0, 0)) -> bool:
        x, y = new_coords
        if x < 0 or y < 0:
            return False
        if x > 9 or y > 9:
            return False
        if self.board[y][x] != 0:
            print("Error: Position taken by %d" % self.board[y][x])
            return False
        print("")

    def show_position(self, coords):
        for count_y, value_y in enumerate(self.board):
            for count_x, value_x in enumerate(value_y):
                if (count_x, count_y) == coords:
                    print(self.colors.fg.red + str(value_x)[0] + self.colors.reset, end=" ")
                else:
                    print(str(value_x)[0], end=" ")
            print()



game = StartGame()
system(CLEAR_SCREEN_COMMAND)
game.show_position((2, 1))
