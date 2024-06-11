import pygame as pg
import time
import random

# so far we have done the following
# 1. set up the display screen
# 2. create the snake
# 3. move the snake
# 4. end the game when snake reaches boundaries
# 5. display a game over message
# 6. place the food in random locations
# 7. Display the score


# initialize pygame
pg.init()

disp_height = 600
disp_width = 800
screen = pg.display.set_mode((disp_width, disp_height))
pg.display.set_caption("SNAKE")

# create our snake
snake_length = 1  # keep track of the score and the number of squares
snake_size = 20  # this is the size of the square
#snake = pg.Surface((snake_size, snake_size))  # define the width and height of the snake
#snake.fill((0, 0, 255))
snake_colour = (0, 0, 255)
# snake coordinates
snake_x = 50
snake_y = 50
snake_coordinates = []

def display_snake(snake_coordinates):
    for coordinates in snake_coordinates:
        pg.draw.rect(screen, snake_colour, [coordinates[0], coordinates[1], snake_size, snake_size])


# snake coordinates change
change_x = 0
change_y = 0

# randomize the placement of the food
food_x = round(random.randrange(snake_size + 10, disp_width - snake_size) / 10) * 10
food_y = round(random.randrange(snake_size + 10, disp_height - snake_size) / 10) * 10

# adjust the speed
clock = pg.time.Clock()
timer = 30


def display_message(screen, height, width):
    # set a font
    font = pg.font.SysFont("Papyrus", 50)

    # create an object with some text
    text = font.render('Game Over', True, (0, 255, 0), (0, 0, 0))
    text_rect = text.get_rect()
    text_rect.center = width / 2, height / 2

    # place the text
    screen.blit(text, text_rect)


def play_explosion_music():
    # play some music
    pg.mixer.music.load("music/explosion-6801.mp3")
    pg.mixer.music.play()


def display_score(screen, snake_length):
    # set a font
    font = pg.font.SysFont("Papyrus", 25)

    # create an object with some text
    text = font.render(f'Score: {snake_length - 1}', True, (255, 255, 0), (0, 0, 0))

    screen.blit(text, (0, 0))

def end_game(screen, disp_height, disp_width):
    display_message(screen, disp_height, disp_width)
    pg.display.update()
    play_explosion_music()
    time.sleep(3)
    pg.quit()
    quit()



while True:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            quit()
        if event.type == pg.KEYDOWN:
            if event.key == pg.K_LEFT:
                change_x = -10
                change_y = 0
            elif event.key == pg.K_RIGHT:
                change_x = 10
                change_y = 0
            elif event.key == pg.K_DOWN:
                change_x = 0
                change_y = 10
            elif event.key == pg.K_UP:
                change_x = 0
                change_y = -10

    # your game
    # what happens when the snake hits the "walls"
    if snake_x < 0 or snake_y < 0 or snake_x >= disp_width or snake_y >= disp_height:
        # CHALLENGE: CAN YOU ADD SOME MUSIC HERE?
        end_game(screen, disp_height, disp_width)

    screen.fill((0, 0, 0))  # background colour
    snake_x += change_x
    snake_y += change_y

    # display the snake and track the coordinates
    snake_head = [snake_x, snake_y]
    snake_coordinates.append(snake_head)

    if len(snake_coordinates) > snake_length:
        del snake_coordinates[0]

    display_snake(snake_coordinates)

    # game over when snake head hits the tail
    for coordinates in snake_coordinates[:-1]:
        if snake_head == coordinates:
            end_game(screen, disp_height, disp_width)

    # place your food
    apple_image = pg.image.load("images/Apple.png")
    screen.blit(apple_image, (food_x, food_y))

    # when the snake eats the food
    if snake_x == food_x and snake_y == food_y:
        snake_length += 1
        # play some music
        play_explosion_music()
        # update the x and y coordinates of the food
        food_x = round(random.randrange(snake_size + 10, disp_width - snake_size) / 10) * 10
        food_y = round(random.randrange(snake_size + 10, disp_height - snake_size) / 10) * 10

    display_score(screen, snake_length)
    pg.display.update()
    clock.tick(timer)  # update the speed of the snake
