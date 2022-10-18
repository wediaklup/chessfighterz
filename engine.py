import pygame
import os

RATE  = 60
WIDTH, HEIGHT = 1600, 900
WINDOW = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Hello World")

WHITE = (255, 255, 255)

def win_init():
    WINDOW.fill(WHITE)
    #pygame.display.update()

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
        #pygame.display.update()

if __name__ == "__main__":
    clock = pygame.time.Clock()
    active = True
    while active:
        clock.tick(RATE)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                active = False

        win_init()
        draw.img("dummy.png", 2, 2)

    pygame.quit()
