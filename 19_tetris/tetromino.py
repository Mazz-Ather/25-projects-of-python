from settings import *
import random

class Tetromino:
    def __init__(self, tetris):
        self.tetris = tetris
        self.shape = random.choice(list(TETROMINOES.keys()))
        self.blocks = [Block(self, pos) for pos in TETROMINOES[self.shape]]
        self.landing = False
        self.speed_up = False

    def move(self, direction):
        move_direction = MOVE_DIRECTIONS[direction]
        new_positions = [block.pos + move_direction for block in self.blocks]
        if self.is_valid_position(new_positions):
            for block in self.blocks:
                block.pos += move_direction
            return True
        # Check if the block has landed when moving down
        if direction == 'down':
            self.landing = True
        return False

    def update(self):
        if not self.landing and not self.tetris.game_over:
            # Try to move down
            self.move('down')
            # Check if piece has landed
            if self.landing:
                self.tetris.check_tetromino_landing()
                return

    def rotate(self):
        pivot_pos = self.blocks[0].pos
        new_positions = []
        for block in self.blocks:
            relative_pos = block.pos - pivot_pos
            new_pos = pg.math.Vector2(relative_pos.y, -relative_pos.x) + pivot_pos
            new_positions.append(new_pos)
        
        if self.is_valid_position(new_positions):
            for i, block in enumerate(self.blocks):
                block.pos = new_positions[i]

    def is_valid_position(self, positions):
        return all(map(self.is_valid_block_pos, positions))

    def is_valid_block_pos(self, pos):
        x, y = int(pos.x), int(pos.y)
        return (0 <= x < FIELD_W and y < FIELD_H and 
                (y < 0 or not self.tetris.field_array[y][x]))

class Block(pg.sprite.Sprite):
    def __init__(self, tetromino, pos):
        self.tetromino = tetromino
        self.pos = pg.math.Vector2(pos) + pg.math.Vector2(FIELD_W // 2 - 1, 0)
        self.next_pos = self.pos
        self.alive = True
        
        super().__init__(tetromino.tetris.sprite_group)
        self.image = pg.Surface((TILE_SIZE, TILE_SIZE))
        self.image.fill(COLORS[tetromino.shape])
        self.rect = self.image.get_rect()

    def is_alive(self):
        if not self.alive:
            self.kill()

    def update(self):
        self.rect.topleft = self.pos * TILE_SIZE
        self.is_alive()

    def set_rect_pos(self):
        self.rect.topleft = self.pos * TILE_SIZE