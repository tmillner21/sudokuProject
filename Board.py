import pygame
import sys
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
        self.cell_size = CELL_SIZE
        self.board = [[0 for i in range(9)] for i in range(9)]
        self.rows = len(self.board)
        self.cols = len(self.board[0])
        self.sudoku_board = generate_sudoku(9, self.removed_cells)
        self.outline_surface = pygame.Surface((width, height), pygame.SRCALPHA)
        self.outline_surface.fill((0, 0, 0, 0))  # Transparent fill

    # Creates each cell object on the board.
    def play_sudoku_board(self):
        for i in range(0, 9):
            for j in range(0, 9):
                cell = Cell(self.sudoku_board[i][j], i, j, self.screen)
                self.board[i][j] = cell
                cell.draw()

    # Draws the lines of the board (hot pink for the box lines and white for the other lines)
    def draw(self):
        self.play_sudoku_board()

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

        # A bottom rectangle so the reset, restart, and exit buttons have a place to be displayed.
        bottom_rect = pygame.Rect(0, HEIGHT - 100, WIDTH, 100)
        pygame.draw.rect(self.screen, LINE_COLOR, bottom_rect)

        button_font = pygame.font.Font(None, 40)

        # Initialize buttons
        # Initialize text first
        reset_text = button_font.render("Reset", 0, (255, 255, 255))
        restart_text = button_font.render("Restart", 0, (255, 255, 255))
        exit_text = button_font.render("Exit", 0, (255, 255, 255))

        # Initialize button background color and text
        reset_surface = pygame.Surface((reset_text.get_size()[0] + 20, reset_text.get_size()[1] + 20))
        reset_surface.fill(LINE_COLOR)
        reset_surface.blit(reset_text, (10, 10))

        restart_surface = pygame.Surface((restart_text.get_size()[0] + 20, restart_text.get_size()[1] + 20))
        restart_surface.fill(LINE_COLOR)
        restart_surface.blit(restart_text, (10, 10))

        exit_surface = pygame.Surface((exit_text.get_size()[0] + 20, exit_text.get_size()[1] + 20))
        exit_surface.fill(LINE_COLOR)
        exit_surface.blit(exit_text, (10, 10))

        # Initialize button rectangle
        reset_rectangle = reset_surface.get_rect(center=(WIDTH - 500, HEIGHT // 3 + 415))
        restart_rectangle = restart_surface.get_rect(center=(WIDTH // 3 + 100, HEIGHT // 3 + 415))
        exit_rectangle = exit_surface.get_rect(center=(WIDTH - 100, HEIGHT // 3 + 415))

        # Draw buttons
        self.screen.blit(reset_surface, reset_rectangle)
        self.screen.blit(restart_surface, restart_rectangle)
        self.screen.blit(exit_surface, exit_rectangle)

        restart = False

        while not restart:
            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN:
                    # Set removed cells based on user choice.
                    if reset_rectangle.collidepoint(event.pos):
                        print("reset")
                        return "reset"
                    elif restart_rectangle.collidepoint(event.pos):
                        print("restart")
                        return "restart"
                    elif exit_rectangle.collidepoint(event.pos):
                        print("exit")
                        sys.exit()

            pygame.display.update()


    def select(self, row, col):
        self.selected = (row, col)

    def click(self, x, y):
        if x < self.width and y < self.height:
            row = int(y // self.cell_size)
            col = int(x // self.cell_size)

            if self.selected is not None:
                prev_row, prev_col = self.selected
                self.board[prev_row][prev_col] = False

            self.selected = (row, col)
            self.board[row][col].selected = True

            return row, col
        else:
            return None

    def sketch(self, value):
        if self.selected:
            row, col = self.selected
            self.board[row][col] = value

    def place_number(self, value):
        if self.selected:
            row, col = self.selected
            self.board[row][col].place_number(value)

    def reset_to_original(self):
        self.play_sudoku_board()

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
