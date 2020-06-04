import pygame

from constants import NO_COLS, NO_ROWS, WHITE, FIELD_WIDTH
from Cell import Cell

class Generator:
    def __init__(self, display):
        self.display = display
        self.cells = []


    def build_grid(self):
        x = y = 0
        for i in range(NO_ROWS):
            x = FIELD_WIDTH
            y += FIELD_WIDTH

            for j in range(NO_COLS):
                pygame.draw.line(self.display, WHITE, [x, y], [x + FIELD_WIDTH, y])
                pygame.draw.line(self.display, WHITE, [x + FIELD_WIDTH, y], [x + FIELD_WIDTH, y + FIELD_WIDTH])
                pygame.draw.line(self.display, WHITE, [x + FIELD_WIDTH, y + FIELD_WIDTH], [x , y + FIELD_WIDTH])
                pygame.draw.line(self.display, WHITE, [x, y + FIELD_WIDTH], [x , y])

                pygame.display.update()

                self.cells.append(Cell(x, y))

                x += FIELD_WIDTH

        pygame.display.update()

    def generate(self):
        pass





