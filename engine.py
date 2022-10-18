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
    def img(name: str, x: int, y: int):
        """Draws an image with the given name from the assets directory at the specified coordinates (x, y). File extenson is required."""
        img = pygame.image.load(os.path.join("Assets", name))
        WINDOW.blit(img, (x, y))
