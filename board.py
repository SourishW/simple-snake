import pygame
from pygame import Rect
from snake import Snake
import random 
import math

UP = 0
DOWN = 1
LEFT = 2
RIGHT = 3

GREEN = 0
BLACK = 1
YELLOW = 2

PPBLOCK = 15
FPS = 15

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
        self.food = [random.randint(0, self.width), random.randint(0, self.height)]
    
    def initialize(self):
        pygame.init()
        self.screen = pygame.display.set_mode((self.width*PPBLOCK, self.height*PPBLOCK))
        self.clock = pygame.time.Clock()

    def create_cell_map(self):
        snake = self.snake
        cells = dict()
        for node in snake.nodes:
            cells[flatten_coor(node, self.width, self.height)] = GREEN
        cells[flatten_coor(self.food, self.width, self.height)] = YELLOW
        return cells
    
    def draw(self):
        self.screen.fill("black")
        pixel_map = self.create_cell_map()
        for coordinates, color in pixel_map.items():
            coordinates = split_coor(coordinates, self.width, self.height)
            rect_color = "yellow" if color == YELLOW else "green"
            square = Rect(coordinates[0]*PPBLOCK, coordinates[1]*PPBLOCK, PPBLOCK, PPBLOCK)
            pygame.draw.rect(self.screen, color=rect_color, rect = square)
        pygame.display.flip()
        self.clock.tick(FPS)

    def handle_input(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False
        keys = pygame.key.get_pressed()
        if keys[pygame.K_w] or keys[pygame.K_UP]:
            self.snake.set_direction(UP)
        if keys[pygame.K_s] or keys[pygame.K_DOWN]:
            self.snake.set_direction(DOWN)
        if keys[pygame.K_a] or keys[pygame.K_LEFT]:
            self.snake.set_direction(LEFT)
        if keys[pygame.K_d] or keys[pygame.K_RIGHT]:
            self.snake.set_direction(RIGHT)
        return not self.snake.game_over()
    

    def continue_playing(self):
        self.generate_new_food()
        while (True):
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    return False
            keys = pygame.key.get_pressed()
            if keys[pygame.K_r]:
                self.snake = Snake(self.width, self.height)
                global FPS 
                FPS = 15
                return True
    
    def generate_new_food(self):
        coordinates = [random.randint(2, self.width-2), random.randint(2, self.height-2)]
        while (not self.snake.vet_food(coordinates)):
            coordinates = [random.randint(2, self.width-2), random.randint(2, self.height-2)]
        self.food = coordinates

    
    def update_snake(self):
        self.snake.move()
        if (self.snake.get_head() == self.food):
            global FPS
            FPS += 2
            self.snake.grow_one()
            self.generate_new_food()
    


    