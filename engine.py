import pygame
import os

RATE  = 60
WIDTH, HEIGHT = 1600, 900
WINDOW = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("ChessFighterz Development")
IKONE = pygame.image.load(os.path.join("Assets", 'favicon.png'))
pygame.display.set_icon(IKONE)

WHITE = (255, 255, 255)
BLACK = (0,   0,   0  )

pygame.init()

def win_init():
    WINDOW.fill(BLACK)
    #pygame.display.update()

class align:
    @staticmethod
    def top(obj_x: int, obj_y: int) -> int:
        ...

    @staticmethod
    def center(obj_x: int, obj_y: int) -> tuple:
        middleX = 0
        middleY = 0
        
        screen_x = WIDTH
        screen_y = HEIGHT

        for curX in range(screen_x + 1):
            margin_left  = curX
            margin_right = screen_x - (margin_left + obj_x)

            if margin_left == margin_right:
                middleX = curX
                break

        for curY in range(screen_y + 1):
            margin_top    = curY
            margin_bottom = screen_y - (margin_top + obj_y)

            if margin_top == margin_bottom:
                middleY = curY
                break

        return middleX, middleY

    @staticmethod
    def bottom(obj_y: int) -> int:
        screen_y = HEIGHT

        for curY in range(screen_y + 1):
            margin_top    = curY
            margin_bottom = screen_y - (margin_top + obj_y)

            if margin_bottom == 0:
                return curY

        return 0

    @staticmethod
    def centerX(obj_x: int) -> int:
        middleX = 0
        
        screen_x = WIDTH

        for curX in range(screen_x + 1):
            margin_left  = curX
            margin_right = screen_x - (margin_left + obj_x)

            if margin_left == margin_right:
                middleX = curX
                break

        return middleX


class Animation:
    def __init__(self, folder) -> None:
        self.folder = folder


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
    #clock = pygame.time.Clock()
    #active = True
    #while active:
    #    clock.tick(RATE)
    #    for event in pygame.event.get():
    #        if event.type == pygame.QUIT:
    #            active = False
    #    win_init()
    #    draw.img("dummy.png", 2, 2)
    #pygame.quit()
    print(align.center(704, 704))
