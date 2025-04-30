import pygame as pg

# Game dimensions
FIELD_W, FIELD_H = 10, 20
TILE_SIZE = 35
FIELD_RES = (FIELD_W * TILE_SIZE, FIELD_H * TILE_SIZE)
FIELD_SCALE = 1.7
WINDOW_RES = (FIELD_RES[0] * FIELD_SCALE, FIELD_RES[1])

# Colors
BG_COLOR = (40, 40, 40)
FIELD_COLOR = (20, 20, 20)
GRID_COLOR = (50, 50, 50)

# Movement directions
MOVE_DIRECTIONS = {
    'left': pg.math.Vector2(-1, 0),
    'right': pg.math.Vector2(1, 0),
    'down': pg.math.Vector2(0, 1)
}

# Game settings
FPS = 60
ANIM_TIME_INTERVAL = 150  # milliseconds
FAST_ANIM_TIME_INTERVAL = 15

# Tetromino shapes and colors
TETROMINOES = {
    'T': [(0, 0), (-1, 0), (1, 0), (0, -1)],
    'O': [(0, 0), (0, -1), (1, 0), (1, -1)],
    'J': [(0, 0), (-1, 0), (0, -1), (0, -2)],
    'L': [(0, 0), (1, 0), (0, -1), (0, -2)],
    'I': [(0, 0), (0, 1), (0, -1), (0, -2)],
    'S': [(0, 0), (-1, 0), (0, -1), (1, -1)],
    'Z': [(0, 0), (1, 0), (0, -1), (-1, -1)]
}

COLORS = {
    'T': (128, 0, 128),  # Purple
    'O': (255, 255, 0),  # Yellow
    'J': (0, 0, 255),    # Blue
    'L': (255, 127, 0),  # Orange
    'I': (0, 255, 255),  # Cyan
    'S': (0, 255, 0),    # Green
    'Z': (255, 0, 0)     # Red
}