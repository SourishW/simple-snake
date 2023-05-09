from board import *

UP = 0
DOWN = 1
LEFT = 2
RIGHT = 3

def initialize():
    pygame.init()
    screen = pygame.display.set_mode(1280, 720)
    clock = pygame.time.Clock()


if __name__ == "__main__":
    board = SnakeBoard(1280, 720)
    board.initialize()
    board.test()