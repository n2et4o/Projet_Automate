from Interfaces_graphiques import *

state = State()  # Crée un objet contenant les états
# Boucle principale
running = True
while running:
    if state.choosing_options:
        draw_options_menu(screen, state)
    elif state.showing_help:
        draw_help(screen, state)
    elif state.choosing_automate:
        draw_input_box(screen, state)
    else:
        draw_menu(screen, state)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        elif event.type == pygame.KEYDOWN:
            if state.showing_help:
                if event.key == pygame.K_BACKSPACE:
                    state.showing_help = False

            elif state.choosing_automate:
                if event.key == pygame.K_RETURN:
                    try:
                        state.chosen_automate = int(state.input_text)
                        if 1 <= state.chosen_automate <= 45:
                            state.choosing_automate = False
                            state.options = ["Afficher l'automate", "Afficher sa table", "Transformer l'automate", "Aide", "Retour au menu principal", "Quitter"]
                            state.selected = 0
                            state.input_text = ""
                        else:
                            state.input_text = ""
                    except ValueError:
                        state.input_text = ""
                elif event.key == pygame.K_BACKSPACE:
                    state.input_text = state.input_text[:-1]
                else:
                    state.input_text += event.unicode

            elif state.choosing_options:
                if event.key == pygame.K_DOWN:
                    state.selected_mode = (state.selected_mode + 1) % len(state.mode_options)
                elif event.key == pygame.K_UP:
                    state.selected_mode = (state.selected_mode - 1) % len(state.mode_options)
                elif event.key == pygame.K_RETURN:
                    state.current_mode = state.mode_options[state.selected_mode]
                    state.current_background_color = MODES[state.current_mode]["background"]
                    state.text_color = MODES[state.current_mode]["text"]
                    state.choosing_options = False
                elif event.key == pygame.K_BACKSPACE:
                    state.choosing_options = False

            else:  # Gestion du menu principal
                if event.key == pygame.K_DOWN:
                    state.selected = (state.selected + 1) % len(state.options)
                elif event.key == pygame.K_UP:
                    state.selected = (state.selected - 1) % len(state.options)
                elif event.key == pygame.K_RETURN:
                    if state.chosen_automate is None:  # Menu principal
                        if state.selected == 0:
                            state.choosing_automate = True
                        elif state.selected == 1:
                            state.choosing_options = True
                        elif state.selected == 2:
                            state.showing_help = True
                        elif state.selected == 3:  # Quitter depuis le menu principal
                            running = False

                    elif state.chosen_automate is not None:  # Sous-menu après choix d'un automate
                        if state.selected == 0:
                            print(f"Affichage de l'automate {state.chosen_automate}")
                        elif state.selected == 1:
                            print(f"Affichage de la table de l'automate {state.chosen_automate}")
                        elif state.selected == 2:
                            print(f"Transformation de l'automate {state.chosen_automate}")
                        elif state.selected == 3:
                            state.showing_help = True
                        elif state.selected == 4:
                            state.chosen_automate = None
                            state.options = ["Choisir un automate", "Options", "Aide", "Quitter"]
                        elif state.selected == 5:  # Quitter depuis le sous-menu
                            running = False

    state.clock.tick(60)  # Limite à 60 FPS

pygame.quit()
exit()
