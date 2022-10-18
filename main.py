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
        en.draw.img("board1024.png", *en.align.middle(704, 704), scale_x=704, scale_y=704)
        pygame.display.flip()
        clock.tick(en.RATE)

    pygame.quit()

if __name__ == '__main__':
    main()
