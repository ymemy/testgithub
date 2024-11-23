import pygame

def round_display(screen, font_title, font_subtitle, player, round_number):
    """Display the round screen followed by countdown"""
    screen.fill((255, 255, 255))
    
    # Render the title (Round Number)
    text_title = font_title.render(f"Round {round_number}", True, (0, 0, 0))
    screen.blit(text_title,(screen.get_width() // 2 - text_title.get_width() // 2, screen.get_height() // 3))
    
    # Display Player's Name
    text_name = font_subtitle.render(player, True, (0, 0, 0))
    screen.blit(text_name,(screen.get_width() // 2 - text_name.get_width() // 2, screen.get_height() // 1.5))
    
    # Update the display to show the title and player name
    pygame.display.flip()

    # Wait for 3 seconds
    pygame.time.wait(3000)
    
    # Countdown before the round begins
    countdown = ["3", "2", "1", "Begin!"]
    for count in countdown:
        screen.fill((255, 255, 255))
        
        # Countdown
        text_count = font_title.render(str(count), True, (0, 0, 0))
        screen.blit(text_count,(screen.get_width() // 2 - text_count.get_width() // 2, screen.get_height() // 2))
        
        # Update the display for each countdown
        pygame.display.flip()
        pygame.time.wait(1000)  # Wait for 1 second
