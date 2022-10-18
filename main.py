import pygame
import engine as en

def main():
    active = True
    while active:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                active = False

        en.win_init()

    pygame.quit()

if __name__ == '__main__':
    main()
