import pygame

from constants import SCREEN_WIDTH, SCREEN_HEIGHT
from Generator import Generator

def init_screen(): # draw grid
    pygame.init()
    pygame.display.set_caption("Maze Generator")

    display = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    display.fill(pygame.Color("Black"))
    pygame.display.update()

    return display


display = init_screen()

def main():
    generator = Generator(display)

    generator.build_grid()
    running = True
    while(running):
        generator.generate()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()

if __name__ == "__main__":
    main()