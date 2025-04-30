from settings import *
from tetromino import Tetromino
import pygame.freetype as ft

class Tetris:
    def __init__(self, app):
        self.app = app
        self.sprite_group = pg.sprite.Group()
        self.field_array = self.get_field_array()
        self.tetromino = Tetromino(self)
        self.next_tetromino = Tetromino(self)
        self.speed_up = False
        
        self.score = 0
        self.full_lines = 0
        self.points_per_lines = {0: 0, 1: 100, 2: 300, 3: 700, 4: 1500}
        
        self.game_over = False
        self.pause = False
        
        # Setup font
        self.font = ft.Font(None, 40)

    def get_field_array(self):
        return [[0 for x in range(FIELD_W)] for y in range(FIELD_H)]

    def check_full_lines(self):
        lines_cleared = 0
        y = FIELD_H - 1
        while y > 0:
            # Check if line is full
            if all(self.field_array[y][x] for x in range(FIELD_W)):
                # Remove the line
                for x in range(FIELD_W):
                    if self.field_array[y][x]:
                        self.field_array[y][x].alive = False
                        self.field_array[y][x] = 0
                
                # Move all lines above down
                for row in range(y, 0, -1):
                    self.field_array[row] = self.field_array[row - 1]
                    # Update block positions
                    for x in range(FIELD_W):
                        if self.field_array[row][x]:
                            self.field_array[row][x].pos.y = row
                
                # Clear top line
                self.field_array[0] = [0 for _ in range(FIELD_W)]
                lines_cleared += 1
                # Stay on same line to check if new line is also full
            else:
                y -= 1

        # Update score
        self.score += self.points_per_lines[lines_cleared]
        self.full_lines += lines_cleared

    def put_tetromino_blocks_in_array(self):
        for block in self.tetromino.blocks:
            x, y = int(block.pos.x), int(block.pos.y)
            self.field_array[y][x] = block

    def get_current_height(self):
        for y in range(FIELD_H):
            for x in range(FIELD_W):
                if self.field_array[y][x]:
                    return y
        return FIELD_H

    def check_game_over(self):
        if self.get_current_height() <= 0:
            self.game_over = True

    def check_tetromino_landing(self):
        if self.tetromino.landing:
            if self.tetromino.blocks[0].pos.y <= 0:
                self.game_over = True
            else:
                self.speed_up = False
                self.put_tetromino_blocks_in_array()
                self.tetromino = self.next_tetromino  # Use the next tetromino
                self.next_tetromino = Tetromino(self)  # Create new next tetromino
                self.check_full_lines()

    def control(self, pressed_key):
        if pressed_key == pg.K_LEFT:
            self.tetromino.move(direction='left')
        elif pressed_key == pg.K_RIGHT:
            self.tetromino.move(direction='right')
        elif pressed_key == pg.K_UP:
            self.tetromino.rotate()
        elif pressed_key == pg.K_DOWN:
            self.speed_up = True

    def draw_grid(self):
        for x in range(FIELD_W):
            for y in range(FIELD_H):
                pg.draw.rect(self.app.screen, GRID_COLOR,
                           (x * TILE_SIZE, y * TILE_SIZE, TILE_SIZE, TILE_SIZE), 1)

    def draw_score(self):
        score_text = f'Score: {self.score}'
        text_surface, rect = self.font.render(score_text, (255, 255, 255))
        self.app.screen.blit(text_surface, (FIELD_RES[0] + 20, 20))

    def draw_next_tetromino(self):
        next_text = 'Next:'
        text_surface, rect = self.font.render(next_text, (255, 255, 255))
        self.app.screen.blit(text_surface, (FIELD_RES[0] + 20, 100))
        
        for block in self.next_tetromino.blocks:
            pos = block.pos * TILE_SIZE
            pos.x += FIELD_RES[0] + 50
            pos.y += 150
            pg.draw.rect(self.app.screen, COLORS[self.next_tetromino.shape],
                        (pos.x, pos.y, TILE_SIZE, TILE_SIZE))

    def update(self):
        if not self.game_over and not self.pause:
            self.check_tetromino_landing()
            self.check_game_over()
            self.sprite_group.update()

    def draw(self):
        self.draw_grid()
        self.sprite_group.draw(self.app.screen)
        self.draw_score()
        self.draw_next_tetromino()