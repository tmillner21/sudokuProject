import pygame
from constants import *


class Cell:
    def __init__(self, value, row, col, screen, is_initial=True):
        self.value = value
        self.row = row
        self.col = col
        self.screen = screen
        self.sketched_value = 0
        self.selected = False
        self.is_initial = is_initial
        self.cell_size = CELL_SIZE
        self.rect = pygame.Rect(self.col * self.cell_size, self.row * self.cell_size, self.cell_size, self.cell_size)

    def set_cell_value(self, value):
        self.value = value

    def set_sketched_value(self, value):
        self.sketched_value = value

    def draw(self, is_initial):
        font = pygame.font.Font(None, 36)
        text_color = (255, 255, 255)

        if not is_initial:
            text_color = (0, 0, 0)

        text = font.render(str(self.value) if self.value != 0 else "", 1, text_color)
        textpos = text.get_rect(centerx=(self.col * CELL_SIZE) + CELL_SIZE // 2,
                                centery=(self.row * CELL_SIZE) + CELL_SIZE // 2)

        pygame.draw.rect(self.screen, BG_COLOR, (self.col * CELL_SIZE, self.row * CELL_SIZE, CELL_SIZE, CELL_SIZE))

        self.screen.blit(text, textpos)
