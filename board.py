import pygame
class SnakeBoard:
    def __init__(self, width, height):
        self.width = width
        self.height = height
    
    def initialize(self):
        pygame.init()
        self.screen = pygame.display.set_mode((self.width, self.height))
        self.clock = pygame.time.Clock()


    