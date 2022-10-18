import pygame
import engine as en

def main():
    clock = pygame.time.Clock()
    active = True
    while active:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                active = False

        en.win_init()
        en.draw.img("dummy.png", 100, 100)
        en.draw.img("dummy.png", 300, 300, 200, 100, 90)
        pygame.display.update()
        clock.tick(en.RATE)

    pygame.quit()

if __name__ == '__main__':
    main()
