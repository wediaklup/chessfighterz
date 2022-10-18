import pygame

RATE  = 60
WIDTH, HEIGHT = 1600, 900
WINDOW = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Hello World")

WHITE = (255, 255, 255)

def win_init():
    WINDOW.fill(WHITE)
    pygame.display.update()