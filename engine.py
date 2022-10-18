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

class align:
    @staticmethod
    def middle(obj_x: int, obj_y: int) -> tuple:
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
    print(align.middle(704, 704))
