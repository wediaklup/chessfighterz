from operator import xor
from xxlimited import Str
import pygame
import os

RATE  = 60
WIDTH, HEIGHT = 1600, 900
WINDOW = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Hello World")

WHITE = (255, 255, 255)

def win_init():
    WINDOW.fill(WHITE)
    pygame.display.update()

class draw:
    @staticmethod
    def img(name: str, x: int, y: int, scale_x = None, scale_y = None, rotate = None):
        """Draws an image with the given name from the assets directory at the specified coordinates (x, y). File extenson is required."""
        img = pygame.image.load(os.path.join("Assets", name))

        if scale_x or scale_y:
            img = pygame.transform.scale(img, (scale_x, scale_y))
        if rotate:
            img = pygame.transform.rotate(img, rotate)

        WINDOW.blit(img, (x, y))
