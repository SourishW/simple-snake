import pygame
from pygame import Rect
from snake import Snake
import math

UP = 0
DOWN = 1
LEFT = 2
RIGHT = 3

GREEN = 0
BLACK = 1
YELLOW = 2

PPBLOCK = 10
FPS = 10

def flatten_coor(xytuple, width, height):
    x = xytuple[0]
    y = xytuple[1]
    return y*width +x

def split_coor(flattened, width, height):
    return [flattened % width, flattened // width]

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
            cells[flatten_coor(node, self.width, self.height)] = GREEN
        # for x in range(self.width):
        #     for y in range(self.height):
        #         bg = [x, y]
        #         bg = flatten_coor(bg, self.width, self.height)
        #         if bg not in cells.keys():
        #             cells[bg] = BLACK
        return cells
    
    def draw(self):
        self.screen.fill("black")
        pixel_map = self.create_cell_map()
        for coordinates, color in pixel_map.items():
            coordinates = split_coor(coordinates, self.width, self.height)
            rect_color = "black" if color == BLACK else "green"
            square = Rect(coordinates[0]*PPBLOCK, coordinates[1]*PPBLOCK, PPBLOCK, PPBLOCK)
            pygame.draw.rect(self.screen, color=rect_color, rect = square)
        pygame.display.flip()
        self.clock.tick(FPS)

    def handle_input(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False
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
            self.snake.grow_one()
        return not self.snake.game_over()
    
    
    
    def update_snake(self):
        self.snake.move()
    


    