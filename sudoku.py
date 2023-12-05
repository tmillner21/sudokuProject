import pygame
import sys
from constants import *
from Board import Board


# Draws the welcome screen and has some event handling based on user's input.
def draw_game_start(screen):
    pygame.display.set_caption("Play Sudoku!")

    # Initialize fonts.
    start_title_font = pygame.font.Font(None, 70)
    subtext_font = pygame.font.Font(None, 40)
    button_font = pygame.font.Font(None, 60)

    # Color background.
    screen.fill(BG_COLOR)

    # Initialize and draw title and subtext.
    title_surface = start_title_font.render("Welcome to Sudoku", 0, LINE_COLOR)
    title_rectangle = title_surface.get_rect(center=(WIDTH // 2, HEIGHT // 2 - 170))
    screen.blit(title_surface, title_rectangle)

    subtext_surface = subtext_font.render("Please choose a difficulty level:", 0, LINE_COLOR)
    subtext_rectangle = subtext_surface.get_rect(center=(WIDTH // 2, HEIGHT // 2 - 100))
    screen.blit(subtext_surface, subtext_rectangle)

    # Initialize buttons
    # Initialize text first
    easy_text = button_font.render("Easy", 0, (255, 255, 255))
    medium_text = button_font.render("Medium", 0, (255, 255, 255))
    hard_text = button_font.render("Hard", 0, (255, 255, 255))

    # Initialize button background color and text
    easy_surface = pygame.Surface((easy_text.get_size()[0] + 20, easy_text.get_size()[1] + 20))
    easy_surface.fill(LINE_COLOR)
    easy_surface.blit(easy_text, (10, 10))

    medium_surface = pygame.Surface((medium_text.get_size()[0] + 20, medium_text.get_size()[1] + 20))
    medium_surface.fill(LINE_COLOR)
    medium_surface.blit(medium_text, (10, 10))

    hard_surface = pygame.Surface((hard_text.get_size()[0] + 20, hard_text.get_size()[1] + 20))
    hard_surface.fill(LINE_COLOR)
    hard_surface.blit(hard_text, (10, 10))

    # Initialize button rectangle
    easy_rectangle = easy_surface.get_rect(center=(WIDTH // 3 + 100, HEIGHT // 3 + 100))
    medium_rectangle = medium_surface.get_rect(center=(WIDTH // 3 + 100, HEIGHT // 3 + 200))
    hard_rectangle = hard_surface.get_rect(center=(WIDTH // 3 + 100, HEIGHT // 3 + 300))

    # Draw buttons
    screen.blit(easy_surface, easy_rectangle)
    screen.blit(medium_surface, medium_rectangle)
    screen.blit(hard_surface, hard_rectangle)

    difficulty = None

    while difficulty is None:
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                # Set removed cells based on user choice.
                if easy_rectangle.collidepoint(event.pos):
                    print("easy")
                    removed_cells = 30
                    difficulty = "easy"
                    return removed_cells, difficulty
                elif medium_rectangle.collidepoint(event.pos):
                    print("med")
                    removed_cells = 40
                    difficulty = "medium"
                    return removed_cells, difficulty
                elif hard_rectangle.collidepoint(event.pos):
                    print("hard")
                    removed_cells = 50
                    difficulty = "hard"
                    return removed_cells, difficulty
        pygame.display.update()


# Draws the end screen and has event handling for user's input.
def draw_game_over(screen, board):
    game_over_font = pygame.font.Font(None, 80)
    screen.fill(BG_COLOR)

    # If the board is filled in correctly, the message that gets displayed is different.
    if board.playable_sudoku_board == board.solved_sudoku_board:
        end_text = 'Game Won!'
    else:
        end_text = "Game Lost"
    game_over_surface = game_over_font.render(end_text, 0, LINE_COLOR)
    game_over_rect = game_over_surface.get_rect(
        center=(WIDTH // 2, HEIGHT // 2 - 100))
    screen.blit(game_over_surface, game_over_rect)

    button_font = pygame.font.Font(None, 60)

    # Initialize buttons
    # Initialize text first
    restart_text = button_font.render("Restart", 0, (255, 255, 255))
    exit_text = button_font.render("Exit", 0, (255, 255, 255))

    # Initialize button background color and text
    restart_surface = pygame.Surface((restart_text.get_size()[0] + 20, restart_text.get_size()[1] + 20))
    restart_surface.fill(LINE_COLOR)
    restart_surface.blit(restart_text, (10, 10))

    exit_surface = pygame.Surface((exit_text.get_size()[0] + 20, exit_text.get_size()[1] + 20))
    exit_surface.fill(LINE_COLOR)
    exit_surface.blit(exit_text, (10, 10))

    # Initialize button rectangle
    restart_rectangle = restart_surface.get_rect(center=(WIDTH // 2 - 150, HEIGHT // 3+200))
    exit_rectangle = exit_surface.get_rect(center=(WIDTH // 2 + 150, HEIGHT // 3 + 200))

    # Draw buttons
    screen.blit(restart_surface, restart_rectangle)
    screen.blit(exit_surface, exit_rectangle)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                if restart_rectangle.collidepoint(event.pos):
                    print("restart")
                    return "restart"
                elif exit_rectangle.collidepoint(event.pos):
                    print("exit")
                    exit()
        pygame.display.update()


# Main function.
def main():
    bottom_button_input = None
    end_screen_input = None

    pygame.init()

    # This first while loop creates the welcome screen and the board.
    while True:
        screen = pygame.display.set_mode((WIDTH, HEIGHT))

        screen.fill(BG_COLOR)

        removed_cells, difficulty = draw_game_start(screen)

        draw_board = Board(WIDTH, HEIGHT, screen, removed_cells, difficulty)

        # This second while loop controls the in-progress game screen.
        # The event handling for this screen is in the draw function of the board class.
        while True:
            for event in pygame.event.get():
                print(event)  # Add this line to check if events are being registered
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            bottom_button_input = draw_board.draw()

            # If the user clicks restart, the game goes back to the welcome screen.
            if bottom_button_input == "restart":
                break

            # If the board is full, the bottom_button_input is end.
            if bottom_button_input == "end":
                print('end')
                # This third while loop handles the game over screen.
                while True:
                    end_screen_input = draw_game_over(screen, draw_board)
                    pygame.display.update()

                    if end_screen_input == "restart":
                        break

            # This if statement transports the user back to the welcome screen and resets the inputs.
            if end_screen_input == "restart":
                bottom_button_input = None
                end_screen_input = None
                break

            pygame.display.update()


# Running main.
if __name__ == "__main__":
    main()
