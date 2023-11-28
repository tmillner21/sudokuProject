import pygame


def draw_game_start(screen):
    # Initialize fonts.
    start_title_font = pygame.font.Font(None, 80)
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
    easy_rectangle = easy_surface.get_rect(center=(WIDTH // 3 + 100, HEIGHT // 3 + 70))
    medium_rectangle = medium_surface.get_rect(center=(WIDTH // 3 + 100, HEIGHT // 3 + 170))
    hard_rectangle = hard_surface.get_rect(center=(WIDTH // 3 + 100, HEIGHT // 3 + 270))

    # Draw buttons
    screen.blit(easy_surface, easy_rectangle)
    screen.blit(medium_surface, medium_rectangle)
    screen.blit(hard_surface, hard_rectangle)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                # Set removed cells based on user choice.
                if easy_rectangle.collidepoint(event.pos):
                    print("easy")
                    removed_cells = 30
                elif medium_rectangle.collidepoint(event.pos):
                    print("med")
                    removed_cells = 40
                elif hard_rectangle.collidepoint(event.pos):
                    print("hard")
                    removed_cells = 50
        pygame.display.update()


if __name__ == "__main__":
    game_over = False

    pygame.init()

    # Constants
    BG_COLOR = (255, 149, 203)
    LINE_COLOR = (255, 0, 128)
    WIDTH = 600
    HEIGHT = 600

    screen = pygame.display.set_mode((WIDTH, HEIGHT))

    draw_game_start(screen)
