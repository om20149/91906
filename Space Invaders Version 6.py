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
pygame.font.init()

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
BG = pygame.transform.scale(pygame.image.load(os.path.join("Space Invaders Game", "bg.png")))

class Ship:
    def __init__(self, x, y, health=100):
        self.x = x
        self.y = y
        self.health = health
        self.ship_img = None
        self.laser_img = None
        self.lasers = []
        self.cool_down_counter = 0

    def draw(self, window):
        pygame.draw.rect(window, (255,0,0), (self.x, self.y, 50, 50))

    def get_width(self):
        return self.ship_img.get_width()

    def get_height(self):
        return self.ship_img.get_height()

class Player(ship):
    def __init__(self, x, y, health=100):
        super().__init__(x, y, health)
        self.ship_img = WHITE_SPACE_SHIP
        self.laser_img = YELLOW_LASER
        self.mask = pygame.mask.from_surface(self.ship_img)
        self.max_health = health
def main():
    run = True
    FPS = 60
    level = 1
    lives = 6
    main_font = pygame.font.SysFont("comicsans", 50)
    player_vel = 5

    player = Player(300, 650)
    
    clock = pygame.time.Clock()

    def redraw_window():
        WIN.blit(BG, (0,0))
        #Draw Text
        lives_label = main_font.render(f"Lives:{lives}", 1, (255,255,255))
        level_label = main_font.render(f"Levels:{levels}", 1, (255,255,255))

        WIN.blit(lives_label, (10, 10))
        WIN.blit(level_label, (WIDTH - level_label.get_width() - 10, 10))

        player.draw(WIN)

        pygame.display.update()

    while run:
        clock.tick(FPS)
        redraw_window()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        keys = pygame.key.get_pressed()
        if keys[pygame.K_a] - player and ship.x - player_vel > 0: # left
            player.x -= player_vel
        if keys[pygame.K_d] and ship.x + player_vel  + player.get_width() < WIDTH: # right
            player.x += player_vel
        if keys [pygame.K_w] and ship.y - player_vel > 0:# up
            player.y -= player_vel
        if keys[pygame.K_s] and ship.y + player.vel + player.get_height() < HEIGHT: # down
            player.y += player_vel
main()
