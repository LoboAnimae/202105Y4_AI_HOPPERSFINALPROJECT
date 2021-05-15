class GameParameters:
    from os import name
    CLEAR_SCREEN_COMMAND = 'cls' if name == 'nt' else 'clear'
    PLAY_WITH_OFFSET = True


class colors:
    reset = '\033[0m'

    class fg:
        red = '\033[31m'
