import pygame as pg
import time
import random

# What we have done so far
# 1. created the screen
# 2. create the snake
# 3. move the snake
# 4. Added some logic to end the game when the snake dies
# 5. Place the food

# initialize pygame
pg.init()

disp_height = 600
disp_width = 800
size = disp_width, disp_height
screen = pg.display.set_mode(size)
pg.display.set_caption("SNAKE")
# add a clock function to control the speed
clock = pg.time.Clock()

# create our snake
snake_size = 20
snake_length = 1
snake = pg.Surface((snake_size, snake_size))  # define the width and height of the snake
snake.fill((0, 0, 255))  # defining the colour
# define the starting position
x = 50
y = 50
# define the change
x1_change = 0
y1_change = 0

# create our food
# randomize the x and y coordinates and make sure it does not overlap the snake
food_x = round(random.randrange(snake_size+10, disp_width - snake_size)/10)*10
food_y = round(random.randrange(snake_size+10, disp_height - snake_size)/10)*10

def display_message(display_text, screen, width, height):
    # set the font
    font = pg.font.SysFont("Papyrus", 60)
    # create a text surface object, on which text is drawn on it. The last argument is the background colour.
    text = font.render(display_text, True, (0, 255, 0), (0, 0, 0))
    # convert this into a rectangular object
    text_rect = text.get_rect()
    text_rect.center = width/2, height/2
    # place the message in the center of the screen
    screen.blit(text, text_rect)


while True:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            quit()
        if event.type == pg.KEYDOWN:
            # (0,0 is in the corner of the screen)
            if event.key == pg.K_LEFT:
                x1_change = -10
                y1_change = 0
            elif event.key == pg.K_RIGHT:
                x1_change = 10
                y1_change = 0
            elif event.key == pg.K_UP:
                x1_change = 0
                y1_change = -10
            elif event.key == pg.K_DOWN:
                x1_change = 0
                y1_change = 10

    # exit the game if x or y reaches the boundaries of the screen
    if x < 0 or y < 0 or x >= disp_width or y >= disp_height:
        # CAN YOU ADD SOME MUSIC WHEN IT DIES?!
        display_message("GAME OVER!!!!!!!!", screen, disp_width, disp_height)
        pg.display.update()
        time.sleep(4)
        pg.quit()
        quit()

    # this is our game
    x += x1_change
    y += y1_change
    screen.fill((0, 0, 0))  # background colour
    screen.blit(snake, (x, y))  # places the snake
    # place the food
    apple_image = pg.image.load("images/Apple.png")
    screen.blit(apple_image, (food_x, food_y))

    # what happens when the snake eats the food
    if x == food_x and y == food_y:
        snake_length += 1
        print(snake_length)
        # PLAY SOME MUSIC
        pg.mixer.music.load("music/explosion-6801.mp3")
        pg.mixer.music.play()
        # change the position of the food
        food_x = round(random.randrange(snake_size + 10, disp_width - snake_size) / 10) * 10
        food_y = round(random.randrange(snake_size + 10, disp_height - snake_size) / 10) * 10

    pg.display.update()
    clock.tick(30)
