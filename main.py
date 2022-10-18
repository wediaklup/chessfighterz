import pygame
import engine as en

def main():
    clock = pygame.time.Clock()
    active = True
    while active:
        clock.tick(en.RATE)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                active = False

        en.win_init()

    pygame.quit()

if __name__ == '__main__':
    main()
