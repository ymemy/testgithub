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
    screen = pygame.display.set_mode((screen_width, screen_height))
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
    """Display the instructions screen."""
    # Clear the screen
    screen.fill((255, 255, 255))
    
    # Render the title
    text_title = font_title.render("Instructions", True, (0, 0, 0))
    screen.blit(text_title, (screen.get_width() // 2 - text_title.get_width() // 2, 50))  # Positioned at the top
    
    # List of instructions
    instructions = [
        "1. Each player gets 1 minute to play.",
        "2. Translate as many words as possible correctly.",
        "3. Press ENTER to submit your answer.",
        "4. Each correct answer earns you a point.",
        "5. The player with the most points wins!"
    ]
    
    # Render and display each instruction line
    y_offset = 150  # Starting Y position for instructions
    line_spacing = 50  # Space between lines
    for i, instruction in enumerate(instructions):
        text = font_subtitle.render(instruction, True, (0, 0, 0))
        screen.blit(text, (screen.get_width() // 2 - text.get_width() // 2, y_offset + i * line_spacing))
    
    # Update the display
    pygame.display.flip()
    
    # Wait for user input or timeout
    pygame.time.wait(10000)  # Wait for 10 seconds before proceeding


if __name__ == "__main__":
    main()

