import random
import pygame
import sys

# Initialize Pygame
pygame.init()

# Constants
WINDOW_WIDTH = 800
WINDOW_HEIGHT = 700  # Increased height for better spacing
GRID_SIZE = 60
PADDING = 5
MESSAGE_HEIGHT = 100  # Dedicated space for messages

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREY = (128, 128, 128)
GREEN = (106, 170, 100)
YELLOW = (201, 180, 88)
RED = (220, 20, 60)
BACKGROUND = (255, 255, 255)


class WordleGame:
    def __init__(self):
        self.screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
        pygame.display.set_caption("Wordle")
        self.font = pygame.font.Font(None, 48)
        self.message_font = pygame.font.Font(None, 36)
        self.keyword = self.get_random_word()
        self.attempts = len(self.keyword) + 3
        self.guesses = []
        self.current_guess = ""
        self.game_over = False
        self.message = ""
        self.score = self.attempts
        self.status_message = f"Word length: {len(self.keyword)}"

    def get_random_word(self):
        try:
            with open(r"C:\Users\minh\PycharmProjects\wordle\words.txt", 'r', encoding='utf-8') as file:
                words = file.read().splitlines()
                return random.choice(words).lower()
        except FileNotFoundError:
            print("Error: words.txt file not found")
            return "test"
        except Exception as e:
            print(f"Error reading file: {e}")
            return "test"

    def draw_message_box(self):
        # Draw message box at the bottom
        message_box = pygame.Surface((WINDOW_WIDTH, MESSAGE_HEIGHT))
        message_box.fill(WHITE)
        pygame.draw.rect(message_box, GREY, message_box.get_rect(), 2)

        # Draw status message
        status_text = self.message_font.render(self.status_message, True, BLACK)
        status_rect = status_text.get_rect(center=(WINDOW_WIDTH // 2, MESSAGE_HEIGHT // 3))
        message_box.blit(status_text, status_rect)

        # Draw game over message if applicable
        if self.game_over:
            game_text = self.message_font.render(self.message, True, BLACK)
            game_rect = game_text.get_rect(center=(WINDOW_WIDTH // 2, 2 * MESSAGE_HEIGHT // 3))
            message_box.blit(game_text, game_rect)

        self.screen.blit(message_box, (0, WINDOW_HEIGHT - MESSAGE_HEIGHT))

    def draw_grid(self):
        word_length = len(self.keyword)
        start_x = (WINDOW_WIDTH - (word_length * (GRID_SIZE + PADDING))) // 2
        start_y = 80  # Increased starting position

        # Draw title
        title = self.font.render("WORDLE", True, BLACK)
        title_rect = title.get_rect(center=(WINDOW_WIDTH // 2, 40))
        self.screen.blit(title, title_rect)

        # Draw grid and letters
        for row in range(self.attempts):
            for col in range(word_length):
                x = start_x + col * (GRID_SIZE + PADDING)
                y = start_y + row * (GRID_SIZE + PADDING)

                color = WHITE
                if row < len(self.guesses):
                    guess = self.guesses[row]
                    if guess[col] == self.keyword[col]:
                        color = GREEN
                    elif guess[col] in self.keyword:
                        color = YELLOW
                    else:
                        color = GREY

                pygame.draw.rect(self.screen, color, (x, y, GRID_SIZE, GRID_SIZE))
                pygame.draw.rect(self.screen, BLACK, (x, y, GRID_SIZE, GRID_SIZE), 2)

                if row < len(self.guesses):
                    letter = self.font.render(self.guesses[row][col].upper(), True, WHITE)
                    letter_rect = letter.get_rect(center=(x + GRID_SIZE // 2, y + GRID_SIZE // 2))
                    self.screen.blit(letter, letter_rect)

        # Draw current guess
        if not self.game_over and self.current_guess:
            row = len(self.guesses)
            for col, letter in enumerate(self.current_guess):
                x = start_x + col * (GRID_SIZE + PADDING)
                y = start_y + row * (GRID_SIZE + PADDING)
                letter_surface = self.font.render(letter.upper(), True, BLACK)
                letter_rect = letter_surface.get_rect(center=(x + GRID_SIZE // 2, y + GRID_SIZE // 2))
                self.screen.blit(letter_surface, letter_rect)

    def run(self):
        while True:
            self.screen.fill(BACKGROUND)
            self.draw_grid()
            self.draw_message_box()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

                if not self.game_over:
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_RETURN and len(self.current_guess) == len(self.keyword):
                            self.guesses.append(self.current_guess)

                            if self.current_guess == self.keyword:
                                self.game_over = True
                                self.message = f"You won! Score: {self.score}"
                            else:
                                self.score -= 1
                                self.status_message = f"Attempts left: {self.attempts - len(self.guesses)}"
                                if len(self.guesses) >= self.attempts:
                                    self.game_over = True
                                    self.message = f"Game Over! The word was: {self.keyword}"

                            self.current_guess = ""

                        elif event.key == pygame.K_BACKSPACE:
                            self.current_guess = self.current_guess[:-1]
                        elif len(self.current_guess) < len(self.keyword) and event.unicode.isalpha():
                            self.current_guess += event.unicode.lower()

            pygame.display.flip()


if __name__ == "__main__":
    game = WordleGame()
    game.run()