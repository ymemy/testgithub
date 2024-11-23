import pygame
from buttons import Button

class Language:
    def __init__(self, screen, font_title, font_subtitle):
        self.screen = screen
        self.font_title = font_title
        self.font_subtitle = font_subtitle
        
        self.WHITE = (255, 255, 255)
        self.BLACK = (0, 0, 0)
        self.BLUE = (0, 102, 204)
        self.GRAY = (200, 200, 200)
        
        self.button_1 = Button()
        self.button_2 = Button()
        self.button_3 = Button()
        self.button_4 = Button()
        self.button_5 = Button()

    def draw(self):
        """Draw the home screen."""
        # Fill the screen background
        self.screen.fill(self.WHITE)
        
        # Render and draw title text
        title_text = self.font_title.render("Welcome to", True, self.BLACK)
        self.screen.blit(title_text, (self.screen.get_width() // 2 - title_text.get_width() // 2, 100))

        title_text = self.font_title.render("'Who is the better translator'?", True, self.BLACK)
        self.screen.blit(title_text, (self.screen.get_width() // 2 - title_text.get_width() // 2, 200))
        
        # Draw the button
        pygame.draw.rect(self.screen, self.GRAY, self.button_rect)
        button_text = self.font_subtitle.render("START", True, self.BLACK)
        self.screen.blit(button_text, (self.button_rect.x + self.button_rect.width // 2 - button_text.get_width() // 2,
                                       self.button_rect.y + self.button_rect.height // 2 - button_text.get_height() // 2))
    
    def handle_event(self, event):
        """Handle events for the home screen."""
        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.button_rect.collidepoint(event.pos):  # Check if the button is clicked
                return "start"  # Signal to move to the next screen
        return None