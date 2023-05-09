import pygame
from snake import Snake
from main import UP, DOWN, LEFT, RIGHT, names

GREEN = 0
BLACK = 1
YELLOW = 2

PPBLOCK = 32

class SnakeBoard:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.snake = Snake(width, height)
    
    def initialize(self):
        pygame.init()
        self.screen = pygame.display.set_mode((self.width*PPBLOCK, self.height*PPBLOCK))
        self.clock = pygame.time.Clock()

    def create_cell_map(self):
        snake = self.snake
        cells = dict()
        for node in snake.nodes:
            cells[node] = GREEN
        for x in range(self.width):
            for y in range(self.height):
                bg = [x, y]
                if bg not in cells.keys():
                    cells[bg] = BLACK
        return cells
    
    def draw(self):
        self.screen.fill("purple")
        pixel_map = self.create_cell_map()
        for coordinates, color in pixel_map.items():
            pygame.draw.rect(self.screen, color="black" if color == BLACK else "green", )
        pygame.display.flip()
        self.clock.tick(10)
        
    def update_snake(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_w]:
            self.snake.set_direction(UP)
        if keys[pygame.K_s]:
            self.snake.set_direction(DOWN)
        if keys[pygame.K_a]:
            self.snake.set_direction(LEFT)
        if keys[pygame.K_d]:
            self.snake.set_direction(RIGHT)
        if keys[pygame.K_SPACE] or keys[pygame.K_g]:
            self.snake.grow()
        
        self.snake.move()
    


    