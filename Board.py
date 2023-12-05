import pygame
import sys
import copy
from Cell import Cell
from constants import *
from sudoku_generator import *


# Board class.
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
        self.boards_from_generator = generate_sudoku(9, self.removed_cells)
        self.default_sudoku_board = self.boards_from_generator[0]
        self.solved_sudoku_board = self.boards_from_generator[1]
        self.playable_sudoku_board = copy.deepcopy(self.default_sudoku_board)
        self.outline_surface = pygame.Surface((width, height), pygame.SRCALPHA)
        self.outline_surface.fill((0, 0, 0, 0))  # Transparent fill

    # Creates and draws each cell object on the board.
    def play_sudoku_board(self):
        for i in range(0, 9):
            for j in range(0, 9):
                if self.default_sudoku_board[i][j] != self.playable_sudoku_board[i][j]:
                    cell = Cell(self.playable_sudoku_board[i][j], i, j, self.screen, False)
                    self.board[i][j] = cell
                    cell.draw(cell.initial)
                else:
                    cell = Cell(self.playable_sudoku_board[i][j], i, j, self.screen, True)
                    self.board[i][j] = cell
                    cell.draw(cell.initial)

    # Returns the row and column of where the user has clicked.
    def click(self, x, y):
        if x < self.width and y < self.height:
            row = int(y // self.cell_size)
            col = int(x // self.cell_size)

            self.selected = (row, col)
            return row, col
        else:
            return None

    # Draws the lines of the board, draws the outline, and draws the buttons at the bottom.
    # This function also handles mouse button down to change the selected cell and keyboard input.
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

        # Outline cell in light blue
        if self.selected is not None:
            row, col = self.selected
            cell_rect = pygame.Rect(col*self.cell_size, row*self.cell_size, self.cell_size, self.cell_size)
            pygame.draw.rect(self.screen, OUTLINE_COLOR, cell_rect, width=7)

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

        pygame.display.update()

        restart = False

        while not restart:
            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN:
                    # Outline cell event handling
                    x, y = pygame.mouse.get_pos()
                    row, col = y // self.cell_size, x // self.cell_size
                    self.selected = (row, col)

                    # Buttons on the bottom.
                    if reset_rectangle.collidepoint(event.pos):
                        print("reset")
                        self.playable_sudoku_board = copy.deepcopy(self.default_sudoku_board)
                        return "reset"
                    elif restart_rectangle.collidepoint(event.pos):
                        print("restart")
                        return "restart"
                    elif exit_rectangle.collidepoint(event.pos):
                        print("exit")
                        sys.exit()

                # Keyboard input
                if event.type == pygame.KEYDOWN:
                    x, y = pygame.mouse.get_pos()
                    row, col = int(y // self.cell_size), int(x // self.cell_size)

                    if event.key in [pygame.K_1, pygame.K_2, pygame.K_3, pygame.K_4, pygame.K_5, pygame.K_6, pygame.K_7, pygame.K_8, pygame.K_9]:
                        # Convert the pygame key to the corresponding number
                        number = int(event.unicode) if event.unicode else None
                        print(number)

                        self.playable_sudoku_board[row][col] = number
                        print(self.playable_sudoku_board)

                        # Checks if the board is full.
                        if any(0 in row for row in self.playable_sudoku_board):
                            print("partially filled")
                        elif any(0 not in row for row in self.playable_sudoku_board):
                            return "end"

            pygame.display.update()
            break
