import random

import tkinter as tk
 
import pygame
from pygame import mixer
from pygame.locals import *
import random
from tkinter import messagebox

#Math Section

class MathQuestionWindow(tk.Tk):
    def __init__(app, bullet):
        super().__init__()

        num = [1, 2, 3, 4, 5, 6, 7, 8, 9]

        # Function to submit the answer and give feedback

        def on_closing():
            messagebox.showwarning(title="Sorry!", message="Please answer the question to progress.")

        app.protocol("WM_DELETE_WINDOW", on_closing)

        def submit_answer(entry):

            try:

                user_answer = int(entry.get())

                correct_answer = calculate_result()

                if user_answer == correct_answer:

                    feedback_label.config(text="Correct!", fg="green")

                    explosion_fx.play()
                    explosion = Explosion(bullet.rect.centerx, bullet.rect.centery, 2)
                    explosion_group.add(explosion)
                    pygame.sprite.spritecollide(bullet, alien_group, True)

                    app.destroy()

                else:

                    feedback_label.config(text=f"Wrong! The correct answer was {correct_answer}.", fg="red")
                    spaceship.health_remaining -= 1
                    app.answered_correctly = False
                    app.destroy()

            except ValueError:

                feedback_label.config(text="Please enter a valid number.", fg="red")

        

        # Function to generate a new question

        def generate_question():

            generate_question.num1 = random.choice(num)

            generate_question.num2 = random.choice(num)

            operation = operation_var.get()

        

            if operation == '+':

                question_text = f"{generate_question.num1} + {generate_question.num2}"

            elif operation == '-':

                question_text = f"{generate_question.num1} - {generate_question.num2}"

            elif operation == '*':

                question_text = f"{generate_question.num1} * {generate_question.num2}"

            elif operation == '/':

                generate_question.num2 = random.choice([n for n in num if n != 0])  # Avoid division by zero

                question_text = f"{generate_question.num1} / {generate_question.num2}"

        

            question_label.config(text=question_text)

            feedback_label.config(text="")  # Clear previous feedback

        

        # Function to calculate the correct answer

        def calculate_result():

            operation = operation_var.get()

        

            if operation == '+':

                return generate_question.num1 + generate_question.num2

            elif operation == '-':

                return generate_question.num1 - generate_question.num2

            elif operation == '*':

                return generate_question.num1 * generate_question.num2

            elif operation == '/':

                return generate_question.num1 // generate_question.num2  # Integer division

            else:

                return None  # Handle unexpected operations

        

        # Initialize the main application window

        app.title("Math4Kids")

        app.geometry("240x300")

        app.resizable(False, False)

        

        # Dropdown menu for selecting the operation

        operation_var = tk.StringVar(app)

        operation_var.set('+')  # Default value

        

        operation_menu = tk.OptionMenu(app, operation_var, '+', '-', '*', '/')

        operation_menu.place(relx=0.35, rely=0.05, relwidth=0.34, relheight=0.1)

        

        # Start button to generate the first question

        start_button = tk.Button(app, text="Start", command=generate_question)

        start_button.place(relx=0.35, rely=0.17, relwidth=0.34, relheight=0.1)

        

        # Entry field for the user to submit their answer

        solving_entry = tk.Entry(app)

        solving_entry.place(relx=0.35, rely=0.3, relwidth=0.34, relheight=0.1)

        

        # Submit button to check the answer

        submit_button = tk.Button(app, text="Submit", command=lambda: submit_answer(solving_entry))

        submit_button.place(relx=0.35, rely=0.43, relwidth=0.34, relheight=0.1)

        

        # Try again button to generate a new question

        try_again_button = tk.Button(app, text="Try Again", command=generate_question)

        try_again_button.place(relx=0.35, rely=0.56, relwidth=0.34, relheight=0.1)

        

        # Label to display the generated math question

        question_label = tk.Label(app, text="", font=("Courier", 16))

        question_label.place(relx=0.1, rely=0.7, relwidth=0.8, relheight=0.1)

        

        # Label to provide feedback to the user

        feedback_label = tk.Label(app, text="", font=("Courier", 16))

        feedback_label.place(relx=0.1, rely=0.83, relwidth=0.8, relheight=0.1)

        

        # Run the main loop

        app.mainloop()

#Game Section

pygame.mixer.pre_init(44100, -16, 2, 512)
mixer.init()
pygame.init()

# Define fps
clock = pygame.time.Clock()
fps = 60

screen_width = 450
screen_height = 600

screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Space Invaders Math Game')

# Define fonts
font30 = pygame.font.SysFont('Constantia', 30)
font40 = pygame.font.SysFont('Constantia', 40)

# Load sounds
explosion_fx = pygame.mixer.Sound("explosion.wav")
explosion_fx.set_volume(0.75)

explosion2_fx = pygame.mixer.Sound("explosion2.wav")
explosion2_fx.set_volume(0.75)

laser_fx = pygame.mixer.Sound("laser.wav")
laser_fx.set_volume(0.75)

# Define game variables
rows = 5
cols = 5
alien_cooldown = 1000  # bullet cooldown in milliseconds
last_alien_shot = pygame.time.get_ticks()
countdown = 3
last_count = pygame.time.get_ticks()
game_over = 0  # 0 is no game over, 1 means player has won, -1 means player has lost

# Define colors
red = (255, 0, 0)
green = (0, 255, 0)
white = (255, 255, 255)
blue = (0, 0, 255)

# Load and scale background image
bg = pygame.image.load("bg.png")
bg = pygame.transform.scale(bg, (screen_width, screen_height))

def draw_bg():
    screen.blit(bg, (0, 0))

# Define function for creating text
def draw_text(text, font, text_col, x, y):
    img = font.render(text, True, text_col)
    screen.blit(img, (x, y))

# Create Button class
class Button():
    def __init__(self, x, y, image):
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)
        self.clicked = False

    def draw(self):
        action = False
        # get mouse position
        pos = pygame.mouse.get_pos()

        # check mouseover and clicked conditions
        if self.rect.collidepoint(pos):
            if pygame.mouse.get_pressed()[0] == 1 and not self.clicked:
                self.clicked = True
                action = True
        if pygame.mouse.get_pressed()[0] == 0:
            self.clicked = False

        # draw button
        screen.blit(self.image, (self.rect.x, self.rect.y))

        return action

# Load button images
replay_img = pygame.image.load("replay.png")
replay_img = pygame.transform.scale(replay_img, (150, 50))
quit_img = pygame.image.load("quit.png")
quit_img = pygame.transform.scale(quit_img, (150, 50))

# Create buttons
replay_button = Button(screen_width // 2 - 75, screen_height // 2 + 160, replay_img)
quit_button = Button(screen_width // 2 - 75, screen_height // 2 + 210, quit_img)

# Create spaceship class
class Spaceship(pygame.sprite.Sprite):
    def __init__(self, x, y, health):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("Space Invaders Ship White.png")
        self.image = pygame.transform.scale(self.image, (50, 50))  # Resize image
        self.rect = self.image.get_rect()
        self.rect.center = [x, y]
        self.health_start = health
        self.health_remaining = health
        self.last_shot = pygame.time.get_ticks()

    def update(self):
        speed = 8
        cooldown = 500  # milliseconds
        game_over = 0

        # Get key press
        key = pygame.key.get_pressed()
        if key[pygame.K_LEFT] and self.rect.left > 0:
            self.rect.x -= speed
        if key[pygame.K_RIGHT] and self.rect.right < screen_width:
            self.rect.x += speed

        # Record current time
        time_now = pygame.time.get_ticks()

        # Shoot
        if key[pygame.K_SPACE] and time_now - self.last_shot > cooldown:
            laser_fx.play()
            bullet = Bullets(self.rect.centerx, self.rect.top)
            bullet_group.add(bullet)
            self.last_shot = time_now

        # Update mask
        self.mask = pygame.mask.from_surface(self.image)

        # Draw health bar
        pygame.draw.rect(screen, red, (self.rect.x, (self.rect.bottom + 10), self.rect.width, 15))
        if self.health_remaining > 0:
            pygame.draw.rect(screen, green, (self.rect.x, (self.rect.bottom + 10), int(self.rect.width * (self.health_remaining / self.health_start)), 15))
        elif self.health_remaining <= 0:
            explosion = Explosion(self.rect.centerx, self.rect.centery, 3)
            explosion_group.add(explosion)
            self.kill()
            game_over = -1
        return game_over

# Create Bullets class
class Bullets(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("bullet.png")
        self.image = pygame.transform.scale(self.image, (10, 20))  # Resize image
        self.rect = self.image.get_rect()
        self.rect.center = [x, y]

    def update(self):
        self.rect.y -= 5
        if self.rect.bottom < 0:
            self.kill()
        if pygame.sprite.spritecollide(self, alien_group, False):
            MathQuestionWindow(self)
            self.kill()
            pass

# Create Aliens class
class Aliens(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("alien" + str(random.randint(1, 9)) + ".png")
        self.image = pygame.transform.scale(self.image, (40, 40))  # Resize image
        self.rect = self.image.get_rect()
        self.rect.center = [x, y]
        self.move_counter = 0
        self.move_direction = 1

    def update(self):
        self.rect.x += self.move_direction
        self.move_counter += 1
        if abs(self.move_counter) > 75:
            self.move_direction *= -1
            self.move_counter *= self.move_direction

# Create Alien Bullets class
class Alien_Bullets(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("alien_bullet.png")
        self.image = pygame.transform.scale(self.image, (10, 20))  # Resize image
        self.rect = self.image.get_rect()
        self.rect.center = [x, y]

    def update(self):
        self.rect.y += 2
        if self.rect.top > screen_height:
            self.kill()
        if pygame.sprite.spritecollide(self, spaceship_group, False, pygame.sprite.collide_mask):
            self.kill()
            explosion2_fx.play()
            spaceship.health_remaining -= 1
            explosion = Explosion(self.rect.centerx, self.rect.centery, 1)
            explosion_group.add(explosion)

# Create Explosion class
class Explosion(pygame.sprite.Sprite):
    def __init__(self, x, y, size):
        pygame.sprite.Sprite.__init__(self)
        self.images = []
        for num in range(1, 5):
            img = pygame.image.load(f"exp{num}.png")
            if size == 1:
                img = pygame.transform.scale(img, (20, 20))
            if size == 2:
                img = pygame.transform.scale(img, (40, 40))
            if size == 3:
                img = pygame.transform.scale(img, (80, 80))
            self.images.append(img)
        self.index = 0
        self.image = self.images[self.index]
        self.rect = self.image.get_rect()
        self.rect.center = [x, y]
        self.counter = 0

    def update(self):
        explosion_speed = 3
        self.counter += 1

        if self.counter >= explosion_speed and self.index < len(self.images) - 1:
            self.counter = 0
            self.index += 1
            self.image = self.images[self.index]

        if self.index >= len(self.images) - 1 and self.counter >= explosion_speed:
            self.kill()

# Create sprite groups
spaceship_group = pygame.sprite.Group()
bullet_group = pygame.sprite.Group()
alien_group = pygame.sprite.Group()
alien_bullet_group = pygame.sprite.Group()
explosion_group = pygame.sprite.Group()

def create_aliens():
    for row in range(rows):
        for item in range(cols):
            alien = Aliens(100 + item * 60, 100 + row * 70)  # Adjusted the spacing
            alien_group.add(alien)
create_aliens()

# Create player
spaceship = Spaceship(int(screen_width / 2), screen_height - 100, 6)
spaceship_group.add(spaceship)

def reset_game():
    global game_over, countdown, spaceship, last_count
    game_over = 0
    countdown = 3
    last_count = pygame.time.get_ticks()
    spaceship_group.empty()
    bullet_group.empty()
    alien_group.empty()
    alien_bullet_group.empty()
    explosion_group.empty()
    spaceship = Spaceship(int(screen_width / 2), screen_height - 100, 6)
    spaceship_group.add(spaceship)
    create_aliens()

run = True
while run:
    clock.tick(fps)
    draw_bg()

    if countdown == 0:
        time_now = pygame.time.get_ticks()
        if time_now - last_alien_shot > alien_cooldown and len(alien_bullet_group) < 5 and len(alien_group) > 0:
            attacking_alien = random.choice(alien_group.sprites())
            alien_bullet = Alien_Bullets(attacking_alien.rect.centerx, attacking_alien.rect.bottom)
            alien_bullet_group.add(alien_bullet)
            last_alien_shot = time_now

        if len(alien_group) == 0:
            game_over = 1

        if game_over == 0:
            game_over = spaceship.update()
            bullet_group.update()
            alien_group.update()
            alien_bullet_group.update()
        else:
            if game_over == -1:
                draw_text('YOU LOST!', font40, white, int(screen_width / 2 - 100), int(screen_height / 2 + 110))
                if replay_button.draw():
                    reset_game()
                if quit_button.draw():
                    run = False
            if game_over == 1:
                draw_text('YOU WIN!', font40, white, int(screen_width / 2 - 100), int(screen_height / 2 + 110))
                if replay_button.draw():
                    reset_game()
                if quit_button.draw():
                    run = False
    else:
        draw_text('GET READY!', font40, white, int(screen_width / 2 - 110), int(screen_height / 2 + 110))
        draw_text(str(countdown), font40, white, int(screen_width / 2 - 10), int(screen_height / 2 + 137))
        count_timer = pygame.time.get_ticks()
        if count_timer - last_count > 1000:
            countdown -= 1
            last_count = count_timer

    explosion_group.update()
    spaceship_group.draw(screen)
    bullet_group.draw(screen)
   
    alien_group.draw(screen)
    alien_bullet_group.draw(screen)
    explosion_group.draw(screen)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    pygame.display.update()

pygame.quit()
