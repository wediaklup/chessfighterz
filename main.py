import pygame
import engine as en
import game   as gm

def main():
    clock = pygame.time.Clock()
    active = True
    while active:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                active = False

        en.win_init()
        game = gm.Game("root/test", "mangus")
        game.run()
        print("exited")
        pygame.display.flip()
        clock.tick(en.RATE)

    pygame.quit()

if __name__ == '__main__':
    main()
