import pygame
import random
import time

from constants import NO_COLS, NO_ROWS, WHITE, BLACK, GREEN, FIELD_WIDTH
from Cell import Cell

class Generator:
    def __init__(self, display):
        self.display = display
        self.cells = []
        self.stack = []


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

                self.cells.append(Cell(x, y, j, i))

                x += FIELD_WIDTH

        pygame.display.update()

    def clear_square(self, cell):
        pygame.draw.rect(self.display, BLACK, (cell.x + 1, cell.y + 1, FIELD_WIDTH - 2, FIELD_WIDTH - 2))
        pygame.display.update()

    def draw_square(self, cell):
        pygame.draw.rect(self.display, GREEN, (cell.x + 1, cell.y + 1, FIELD_WIDTH - 2, FIELD_WIDTH - 2))
        pygame.display.update()

    def del_right_wall(self, cell):
        pygame.draw.rect(self.display, BLACK, (cell.x + 1, cell.y + 1, FIELD_WIDTH + 1, FIELD_WIDTH - 1))
        pygame.display.update()

    def del_left_wall(self, cell):
        pygame.draw.rect(self.display, BLACK, (cell.x - FIELD_WIDTH + 1, cell.y + 1, FIELD_WIDTH + 1, FIELD_WIDTH - 1))
        pygame.display.update()

    def del_up_wall(self, cell):
        pygame.draw.rect(self.display, BLACK, (cell.x + 1, cell.y - FIELD_WIDTH + 1, FIELD_WIDTH - 1, FIELD_WIDTH + 1))
        pygame.display.update()

    def del_down_wall(self, cell):
        pygame.draw.rect(self.display, BLACK, (cell.x + 1, cell.y + 1, FIELD_WIDTH - 1, FIELD_WIDTH + 1))
        pygame.display.update()

    def generate_maze(self, cell):
        cell.visited = True #mark as visited
        self.stack.append(cell) #push crnt cell to the stack

        while(len(self.stack) > 0):
            curr_cell = self.stack.pop()
            self.draw_square(curr_cell)

            time.sleep(0.1)

            row = curr_cell.row
            col = curr_cell.col

            directions = []
            #Check if right is available
            if col + 1 < NO_COLS and not self.cells[row * NO_COLS + col + 1].visited:
                directions.append("right")

            #Check if left is available
            if col - 1 >= 0 and not self.cells[row * NO_COLS + col - 1].visited:
                directions.append("left")

            # Check if up is available
            if row - 1 >= 0 and not self.cells[(row - 1) * NO_COLS + col].visited:
                directions.append("up")

            # Check if down is available
            if row + 1 < NO_ROWS and not self.cells[(row + 1) * NO_COLS + col].visited:
                directions.append("down")

            if len(directions) > 0:
                self.stack.append(curr_cell)

                rand_dir = random.choice(directions)

                if rand_dir == "right":
                    next_cell = self.cells[row * NO_COLS + col + 1]

                    self.del_right_wall(curr_cell)
                    next_cell.visited = True
                    self.stack.append(next_cell)

                if rand_dir == "left":
                    next_cell = self.cells[row * NO_COLS + col - 1]

                    self.del_left_wall(curr_cell)
                    next_cell.visited = True
                    self.stack.append(next_cell)

                if rand_dir == "up":
                    next_cell = self.cells[(row - 1) * (NO_COLS) + col]

                    self.del_up_wall(curr_cell)
                    next_cell.visited = True
                    self.stack.append(next_cell)

                if rand_dir == "down":
                    next_cell = self.cells[(row + 1) * NO_COLS + col]

                    self.del_down_wall(curr_cell)
                    next_cell.visited = True
                    self.stack.append(next_cell)

            self.clear_square(curr_cell)