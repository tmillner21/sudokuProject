import pygame
from constants import *


# Cell class.
class Cell:
    def __init__(self, value, row, col, screen, initial):
        self.value = value
        self.row = row
        self.col = col
        self.screen = screen
        self.sketched_value = 0
        self.selected = False
        self.cell_size = CELL_SIZE
        self.rect = pygame.Rect(self.col * self.cell_size, self.row * self.cell_size, self.cell_size, self.cell_size)
        self.initial = initial

    # Draws the cell and the number inside it, the color of the number depends on the Boolean value passed into the function.
    def draw(self, is_initial):

        font = pygame.font.Font(None, 36)

        text = font.render(str(self.value) if self.value != 0 else "", 1, (255, 255, 255) if is_initial else (0, 0, 0))
        textpos = text.get_rect(centerx=(self.col * CELL_SIZE) + CELL_SIZE // 2, centery=(self.row * CELL_SIZE) + CELL_SIZE // 2)

        pygame.draw.rect(self.screen, BG_COLOR, (self.col * CELL_SIZE, self.row * CELL_SIZE, CELL_SIZE, CELL_SIZE))

        self.screen.blit(text, textpos)
