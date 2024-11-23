#usernames input
def get_usernames(screen, font_title, font_subtitle):
    usernames = [" ", " "]
    active_player = 0 
    input_done = False

    while not input_done:
        screen.fill(WHITE)


        title_text = font_title.render("Enter Player Names", True, BLACK)
        screen.blit(title_text, (screen_width // 2 - title_text.get_width() // 2,100))

        for i, username in enumerate(usernames):
            prompt = f"Player {i + 1} Name: {username}"
            prompt_text = font_subtitle.render(prompt, True, BLACK)
            screen.blit(prompt_text, (screen_width // 2 - prompt_text.get_width() // 2, 300 + i*100))

        pygame.display.flip()

        for event in pygame.even.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    if usernames[active_player].strip():
                        active_player += 1
                        if active_player == len(usernames):
                            input_done = True

                elif event.key == pygame.K_BACKSPACE:
                    usernames[active_player] = usernames[active_player][:-1]
                
                else:
                    usernames[active_player] += event.unicode

    return usernames



