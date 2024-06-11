import pygame as pg
import time
import random

# What we have done so far
# 1. created the screen
# 2. create the snake
# 3. move the snake
# 4. Added some logic to end the game when the snake dies
# 5. Place the food
# 6. Eat the food
# 7. Display the score
# 8. Increase the size of the snake

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
snake_size = 20  # the length and width of the snake itself
snake_length = 1  # how many squares you have
snake_coordinates = [] # variable to keep track of the coordinates
snake_colour = (0, 0, 255)
#snake = pg.Surface((snake_size, snake_size))  # define the width and height of the snake
#snake.fill((0, 0, 255))  # defining the colour
# define the starting position
x = 50
y = 50
# define the change
x1_change = 0
y1_change = 0

def display_snake(screen, snake_coordinates, snake_colour, snake_size):
    for coordinates in snake_coordinates:
        pg.draw.rect(screen, snake_colour, [coordinates[0], coordinates[1], snake_size, snake_size])


# create our food
# randomize the x and y coordinates and make sure it does not overlap the snake
food_x = round(random.randrange(snake_size + 10, disp_width - snake_size) / 10) * 10
food_y = round(random.randrange(snake_size + 10, disp_height - snake_size) / 10) * 10


def display_message(display_text, screen, width, height):
    # set the font
    font = pg.font.SysFont("Papyrus", 60)
    # create a text surface object, on which text is drawn on it. The last argument is the background colour.
    text = font.render(display_text, True, (0, 255, 0), (0, 0, 0))
    # convert this into a rectangular object
    text_rect = text.get_rect()
    text_rect.center = width / 2, height / 2
    # place the message in the center of the screen
    screen.blit(text, text_rect)


def display_score(display_text, screen, x, y):
    # set the font
    font = pg.font.SysFont("Papyrus", 20)
    # create a text surface object, on which text is drawn on it. The last argument is the background colour.
    text = font.render(display_text, True, (255, 255, 0), (0, 0, 0))
    # place the message in the center of the screen
    screen.blit(text, (x, y))

def end_game(screen, disp_width, disp_height):
    # CAN YOU ADD SOME MUSIC WHEN IT DIES?!
    display_message("GAME OVER!!!!!!!!", screen, disp_width, disp_height)
    pg.display.update()
    time.sleep(4)
    pg.quit()
    quit()

timer = 30

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
        end_game(screen, disp_width, disp_height)

    # this is our game
    x += x1_change
    y += y1_change
    screen.fill((0, 0, 0))  # background colour
    #screen.blit(snake, (x, y))  # places the snake
    # placing the snake
    snake_head = [x, y]
    snake_coordinates.append(snake_head)
    # prevents the snake from placing another square each iteration
    if len(snake_coordinates) > snake_length:
        del snake_coordinates[0]
    display_snake(screen, snake_coordinates, snake_colour, snake_size)


    # end the game when the snake eats it tail
    for coordinates in snake_coordinates[:-1]:
        if coordinates == snake_head:
            end_game(screen, disp_width, disp_height)

    # place the food
    apple_image = pg.image.load("images/Apple.png")
    screen.blit(apple_image, (food_x, food_y))

    # what happens when the snake eats the food
    if x == food_x and y == food_y:
        snake_length += 1
        # PLAY SOME MUSIC
        pg.mixer.music.load("music/explosion-6801.mp3")
        pg.mixer.music.play()
        # change the position of the food
        food_x = round(random.randrange(snake_size + 10, disp_width - snake_size) / 10) * 10
        food_y = round(random.randrange(snake_size + 10, disp_height - snake_size) / 10) * 10
        timer = timer+5

    display_score(f"The score is: {snake_length - 1}", screen, 0, 0)
    pg.display.update()
    clock.tick(timer)
