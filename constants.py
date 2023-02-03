import pygame
import os

WIDTH, HEIGHT = 1000, 750

# Load images
RED_SPACE_SHIP = pygame.image.load(os.path.join("assets", "pixel_ship_red_small.png"))
GREEN_SPACE_SHIP = pygame.image.load(os.path.join("assets", "pixel_ship_green_small.png"))
BLUE_SPACE_SHIP = pygame.image.load(os.path.join("assets", "pixel_ship_blue_small.png"))

# Player player
YELLOW_SPACE_SHIP = pygame.image.load(os.path.join("assets", "pixel_ship_yellow.png"))

# Lasers
RED_LASER = pygame.image.load(os.path.join("assets", "pixel_laser_red.png"))
GREEN_LASER = pygame.image.load(os.path.join("assets", "pixel_laser_green.png"))
BLUE_LASER = pygame.image.load(os.path.join("assets", "pixel_laser_blue.png"))
YELLOW_LASER = pygame.image.load(os.path.join("assets", "pixel_laser_yellow.png"))

# Background
BG = pygame.transform.scale(pygame.image.load(os.path.join("assets", "background-black.png")), (WIDTH, HEIGHT))

INTRO_TEXT = "In a galaxy not so far away, Vega IT faced a great challenge. A villainous colleague, known only as Bojan, threatened the stability of the company with his greed for power - a raise. As the Dev Lead, you were tasked with saving the company from ruin, and restoring balance to the workplace.With the fate of Vega IT and the galaxy hanging in the balance, you embarked on a journey to uncover the truth about Bojan and his motivations. Armed with your skills as a developer, and guided by the wisdom of those who came before you, you set out to defeat the evil Bojan and bring peace back to the workplace."
