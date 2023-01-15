import pygame
from sys import exit

# Constants
WIDTH  = 1600
HEIGHT = 900

# Initialising Pygame
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("ChessFighterz Development")
clock = pygame.time.Clock()

# Mainloop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    pygame.display.update()
    clock.tick(60)
