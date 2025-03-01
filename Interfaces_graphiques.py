import pygame
import time
import random

# Initialisation de Pygame
pygame.init()

# Paramètres de la fenêtre
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Menu Principal")

# Charger les images de fond
backgrounds = [
    pygame.image.load("background/background1.jpg"),
    pygame.image.load("background/background2.jpg"),
    pygame.image.load("background/background3.jpg"),
    pygame.image.load("background/background4.jpg"),
    pygame.image.load("background/background5.jpg"),
    pygame.image.load("background/background6.jpg"),
    pygame.image.load("background/background7.jpg"),
]
backgrounds = [pygame.transform.scale(bg, (WIDTH, HEIGHT)) for bg in backgrounds]

# Variables de gestion du fond
background_index = 0
change_time = pygame.time.get_ticks()

# Couleurs
WHITE = (255, 255, 255)
text_color = (0, 0, 0)
BLUE = (100, 100, 255)
#current_background_color = WHITE

# Police
font = pygame.font.Font(None, 50)
input_font = pygame.font.Font(None, 40)

# Modes de couleurs
MODES = {
    "Clair": {"background": (255, 255, 255), "text": (0, 0, 0)},
    "Sombre": {"background": (30, 30, 30), "text": (255, 255, 255)},
    "Bleu Nuit": {"background": (10, 10, 50), "text": (200, 200, 255)}
}

# Mode actuel
default_mode = "Sombre"
current_mode = default_mode
current_background_color = MODES[current_mode]["background"]
text_color = MODES[current_mode]["text"]

# Options du menu
options = ["Choisir un automate", "Options", "Aide", "Quitter"]
selected = 0
choosing_automate = False
chosen_automate = None
choosing_options = False
input_text = ""
showing_help = False
clock = pygame.time.Clock()
mode_options = list(MODES.keys())
selected_mode = 0


def draw_menu():
    """Affiche le menu avec le fond dynamique."""
    global background_index, change_time

    # Vérifier si 5 secondes sont écoulées
    if pygame.time.get_ticks() - change_time >= 3000:
        background_index = (background_index + 1) % len(backgrounds)
        change_time = pygame.time.get_ticks()  # Mettre à jour le temps

    # Afficher l'image de fond
    screen.blit(backgrounds[background_index], (0, 0))

    # Afficher le titre
    title = font.render("Bienvenue!", True, text_color)
    screen.blit(title, (WIDTH // 2 - title.get_width() // 2, 50))

    # Afficher les options du menu
    for i, option in enumerate(options):
        color = BLUE if i == selected else text_color
        text = font.render(option, True, color)
        screen.blit(text, (WIDTH // 2 - text.get_width() // 2, 200 + i * 60))

    pygame.display.flip()


def draw_help():
    screen.fill(current_background_color)

    help_text = [
        "Le but de ce code est de manipuler ",
        "des automates en déterminant s'ils ",
        "sont déterministes, standards, complets ",
        "ou non, ou de les transformer, de les",
        "minimaliser ou d'obtenir leur complémentaire."
    ]

    y_offset = HEIGHT // 3  # Position de départ
    for line in help_text:
        rendered_text = font.render(line, True, text_color)
        screen.blit(rendered_text, (5, y_offset))
        y_offset += 50  # Espacement entre les lignes

    back_text = font.render("Appuyez sur Retour pour revenir", True, BLUE)
    screen.blit(back_text, (10, y_offset + 15))

    pygame.display.flip()


def draw_input_box():
    screen.fill(current_background_color)
    prompt = font.render("Entrez un numéro entre 1 et 45:", True, text_color)
    screen.blit(prompt, (WIDTH // 2 - prompt.get_width() // 2, HEIGHT // 3))

    input_surface = input_font.render(input_text, True, BLUE)
    screen.blit(input_surface, (WIDTH // 2 - input_surface.get_width() // 2, HEIGHT // 2))

    pygame.display.flip()


def draw_automate_menu():
    screen.fill(current_background_color)
    title = font.render(f"Automate {chosen_automate}", True, text_color)
    screen.blit(title, (WIDTH // 2 - title.get_width() // 2, 50))
    sub_options = ["Afficher l'automate", "Afficher sa table", "Transformer l'automate", "Aide",
                   "Retour au menu principal", "Quitter"]

    for i, option in enumerate(sub_options):
        color = BLUE if i == selected else text_color
        text = font.render(option, True, color)
        screen.blit(text, (WIDTH // 2 - text.get_width() // 2, 200 + i * 60))

    pygame.display.flip()


def draw_options_menu():
    screen.fill(current_background_color)
    title = font.render("Choisir un Mode:", True, text_color)
    screen.blit(title, (WIDTH // 2 - title.get_width() // 2, 50))

    for i, mode in enumerate(mode_options):
        color = (100, 100, 255) if i == selected_mode else text_color
        text = font.render(mode, True, color)
        screen.blit(text, (WIDTH // 2 - text.get_width() // 2, 200 + i * 60))

    pygame.display.flip()
