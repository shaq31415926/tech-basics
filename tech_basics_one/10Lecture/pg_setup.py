import pygame as pg

# initialize pygame
pg.init()

screen = pg.display.set_mode((800, 800))
pg.display.set_caption("SETTING UP")

# create our snake
surface1 = pg.Surface((20, 20)) # define the width and height of the snake
surface1.fill((0, 0, 255))

# create the food
surface2 = pg.Surface((10, 10)) # define the width and height of the snake
surface2.fill((255, 0, 0))

while True:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            quit()
    screen.fill((0, 0, 0)) # background colour
    screen.blit(surface1, (50, 50))
    screen.blit(surface2, (150, 150))
    pg.display.update()
