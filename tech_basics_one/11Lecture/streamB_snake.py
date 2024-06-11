import pygame as pg
import time

# initialize pygame
pg.init()

disp_height = 600
disp_width = 800
screen = pg.display.set_mode((disp_width, disp_height))
pg.display.set_caption("SNAKE")

# create our snake
snake = pg.Surface((20, 20)) # define the width and height of the snake
snake.fill((0, 0, 255))
# snake coordinates
snake_x = 50
snake_y = 50
# snake coordinates change
change_x = 0
change_y = 0

# adjust the speed
clock = pg.time.Clock()
timer = 30

def display_message(screen, height, width):
    # set a font
    font = pg.font.SysFont("Papyrus", 50)

    # create an object with some text
    text = font.render('Game Over', True, (0, 255, 0), (0, 0, 0))
    text_rect = text.get_rect()
    text_rect.center = width/2, height/2

    # place the text
    screen.blit(text, text_rect)


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
        display_message(screen, disp_height, disp_width)
        pg.display.update()
        time.sleep(3)
        pg.quit()
        quit()

    screen.fill((0, 0, 0)) # background colour
    snake_x += change_x
    snake_y += change_y
    screen.blit(snake, (snake_x, snake_y)) # place the snake on the screen
    pg.display.update()
    clock.tick(timer) # update the speed of the snake
