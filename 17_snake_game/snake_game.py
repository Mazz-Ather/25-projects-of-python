import pygame as pg 
from random import randrange

WINDOW = 600
TITLE_SIZE = 50
RANGE = (TITLE_SIZE // 2 , WINDOW - TITLE_SIZE // 2, TITLE_SIZE)
get_random_position = lambda: [randrange(*RANGE), randrange(*RANGE)]
snake = pg.rect.Rect([0, 0, TITLE_SIZE - 2, TITLE_SIZE - 2])
snake.center = get_random_position()
length = 1
segments = [snake.copy()]
snake_dir = (0, 0)
food = snake.copy()
food.center = get_random_position() 
time, time_step = 0, 150  # Adjusted for better speed
screen = pg.display.set_mode([WINDOW] * 2)
clock = pg.time.Clock()
FPS = 30

while True:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            exit()
        if event.type == pg.KEYDOWN:
            if event.key == pg.K_w and snake_dir != (0, TITLE_SIZE):  # Prevent opposite direction
                snake_dir = (0, -TITLE_SIZE)
            if event.key == pg.K_s and snake_dir != (0, -TITLE_SIZE):
                snake_dir = (0, TITLE_SIZE)
            if event.key == pg.K_a and snake_dir != (TITLE_SIZE, 0):
                snake_dir = (-TITLE_SIZE, 0)
            if event.key == pg.K_d and snake_dir != (-TITLE_SIZE, 0):
                snake_dir = (TITLE_SIZE, 0)
    
    screen.fill('black')
    # check selfeating
    self_eating = pg.Rect.collidelist(snake, segments[:-1]) != -1
    if self_eating:
        snake.center = get_random_position()
        length = 1
        segments = [snake.copy()]
    # check borders
    if snake.left < 0 or snake.right > WINDOW or snake.top < 0 or snake.bottom > WINDOW:
        snake.center = get_random_position()
        length = 1
        segments = [snake.copy()]
    # check food
    if snake.center == food.center:
        food.center = get_random_position()
        length += 1
    pg.draw.rect(screen, 'yellow', food)
    [pg.draw.rect(screen, 'green', segment) for segment in segments]
    
    # move snake (removed duplicate movement)
    time_now = pg.time.get_ticks()
    if time_now - time > time_step:
        time = time_now
        snake.move_ip(snake_dir)
        segments.append(snake.copy())
        segments = segments[-length:]

    pg.display.update()
    clock.tick(FPS)