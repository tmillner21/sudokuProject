import pygame
from Cell import Cell
from constants import *
from sudoku_generator import *


class Board:
    def __init__(self, width, height, screen, removed_cells, difficulty):
        self.width = width
        self.height = height
        self.screen = screen
        self.removed_cells = removed_cells
        self.difficulty = difficulty

    def play_sudoku_board(self):
        self.sudoku_board = generate_sudoku(9, self.removed_cells)
        for i in range(0, 9):
            for j in range(0, 9):
                Cell(self.sudoku_board[i][j], i, j, self.screen).draw()

    def draw(self):
        self.play_sudoku_board()

        while True:
            for i in range(1, 9):
                pygame.draw.line(self.screen, (255, 255, 255), (0, SQUARE_SIZE * i / 3), (WIDTH, SQUARE_SIZE * i / 3),
                                 5)

            for i in range(1, 9):
                pygame.draw.line(self.screen, (255, 255, 255), (SQUARE_SIZE * i / 3, 0), (SQUARE_SIZE * i / 3, HEIGHT),
                                 5)

            for i in range(1, 3):
                pygame.draw.line(self.screen, LINE_COLOR, (0, SQUARE_SIZE * i), (WIDTH, SQUARE_SIZE * i), LINE_WIDTH)

            for i in range(1, 3):
                pygame.draw.line(self.screen, LINE_COLOR, (SQUARE_SIZE * i, 0), (SQUARE_SIZE * i, HEIGHT), LINE_WIDTH)

            pygame.display.update()

    def select(self, row, col):
        pass

    def click(self, x, y):
        pass

    def clear(self):
        pass

    def sketch(self, value):
        pass

    def place_number(self, value):
        pass

    def reset_to_original(self):
        pass

    def is_full(self):
        pass

    def update_board(self):
        pass

    def find_empty(self):
        pass

    def check_board(self):
        pass
