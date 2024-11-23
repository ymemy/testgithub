import pygame
from home import Home

pygame.init()

screen_width, screen_height = 1000, 1000
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Who is the better translator?")

font_title = pygame.font.Font(None, 60)  # Title font
font_subtitle = pygame.font.Font(None, 48)  # Subtitle or button font

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BLUE = (0, 102, 204)
GRAY = (200, 200, 200)

def main():
    # Initialize Pygame
    pygame.init()
    screen = pygame.display.set_mode((800, 600))
    pygame.display.set_caption("Translation Game")
    
    # Initialize fonts
    font_title = pygame.font.Font(None, 72)
    font_subtitle = pygame.font.Font(None, 48)
    
    # Create Home instance
    home_screen = Home(screen, font_title, font_subtitle)
    
    running = True
    clock = pygame.time.Clock()
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            
            # Handle home screen events
            result = home_screen.handle_event(event)
            if result == "start":
                show_instructions(screen, font_title, font_subtitle)  # Transition to instructions
                running = False  # Exit the home screen loop
        
        # Draw the home screen
        home_screen.draw()
        
        # Update the display
        pygame.display.flip()
        clock.tick(60)
    
    pygame.quit()

def show_instructions(screen, font_title, font_subtitle):
    """Temporary placeholder for instructions screen."""
    screen.fill((255, 255, 255))
    text = font_title.render("Instructions Placeholder", True, (0, 0, 0))
    screen.blit(text, (screen.get_width() // 2 - text.get_width() // 2, screen.get_height() // 2))
    pygame.display.flip()
    pygame.time.wait(2000)  # Pause for 2 seconds to simulate instructions screen

if __name__ == "__main__":
    main()
