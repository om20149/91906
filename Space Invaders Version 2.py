#Created on 24/06/2024
#Author: Omisha Mogre
#Purpose: To help children with their maths using this game

#I have imported pygame
import pygame
#I have imported os
import os
#I have imported time
import time
#I have imported random
import random

#I have added the width for the game
WIDTH = 550
#I have added the height for the game
HEIGHT = 550
#I have added the window for the game including the width and height
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
#I have included the title for this game which is called "Space Invaders Maths Game"
pygame.display.set_caption("Space Invaders Maths Game")

#I am going to load all the images into the game
PURPLE_ALIEN = pygame.image.load(os.path.join("Space Invaders Game", "Space Invaders Purple.png"))
LIGHT_BLUE_ALIEN = pygame.image.load(os.path.join("Space Invaders Game", "Space Invaders Light Blue.png"))
BLACK_ALIEN = pygame.image.load(os.path.join("Space Invaders Game", "Space Invaders black.png"))
RED_ALIEN = pygame.image.load(os.path.join("Space Invaders Game", "Space Invaders Red.png"))
DARK_GREEN_ALIEN = pygame.image.load(os.path.join("Space Invaders Game", "Space Invaders Dark Green.png"))
ORANGE_ALIEN = pygame.image.load(os.path.join("Space Invaders Game", "Space Invaders orange.png"))

#I am going to load the image of the player spaceship
WHITE_SPACE_SHIP = pygame.image.load(os.path.join("Space Invaders Game", "Space Invaders Ship White.png"))

#I am going to load the lasers in the game
DARK_BLUE_LASER = pygame.image.load(os.path.join("Space Invaders Game", "Space Invaders Pixel Laser Dark Blue.png"))
DARK_ORANGE_LASER = pygame.image.load(os.path.join("Space Invaders Game", "Space Invaders Pixel Laser Dark Orange.png"))
DARK_PURPLE_LASER = pygame.image.load(os.path.join("Space Invaders Game", "Space Invaders Pixel Laser Dark Purple.png"))
DARK_RED_LASER = pygame.image.load(os.path.join("Space Invaders Game", "Space Invaders Pixel Laser Dark Red.png"))
LIGHT_GREEN_LASER = pygame.image.load(os.path.join("Space Invaderes Game", "Space Invaders Pixel Laser Light Green.png"))
YELLOW_LASER = pygame.image.load(os.path.join("Space Invaders Game", "Space Invaders Pixel Laser Yellow.png"))

#I am going to load the background Image
BG = pygame.image.load(os.path.join("Space Invaders Game", "bg.png"))

def main():
    run = True
    FPS = 60
    clock = pygame.time.Clock()

    def redraw_window():
        
        pygame.display.update()

    while run:
        clock.tick(FPS)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
main()




