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
        self.selected = None
        self.cell_size = self.width // 9
        self.board = [[0 for i in range(9)] for i in range(9)]
        self.rows = len(self.board)
        self.cols = len(self.board[0])
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
        self.selected = (row, col)

    def click(self, x, y):
        if x < self.width and y < self.height:
            row = y // self.cell_size
            col = x // self.cell_size
            return (row, col)
        else:
            return None

    def clear(self):
        if self.selected:
            row, col = self.selected
            self.board[row][col] = 0

    def sketch(self, value):
        if self.selected:
            row, col = self.selected
            self.board[row][col] = value

    def place_number(self, value):
        if self.selected:
            row, col = self.selected
            self.board[row][col] = value

    def reset_to_original(self):
        self.board = [[0 for i in range(9)] for i in range(9)]

    def is_full(self):
        for i in range(self.rows):
            for j in range(self.cols):
                if self.board[i][j] == 0:
                    return False
        return True

    def update_board(self):
        for i in range(self.rows):
            for j in range(self.cols):
                self.board[i][j] = self.board[i][j]

    def find_empty(self):
        for i in range(self.rows):
            for j in range(self.cols):
                if self.board[i][j] == 0:
                    return (i, j)
        return None

    def check_board(self):
        for i in range(self.rows):
            for j in range(self.cols):
                if self.board[i][j] == 0:
                    return False
