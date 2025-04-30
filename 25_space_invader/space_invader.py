import pygame 
import random

# Initialize Pygame
pygame.init()

# Change window size to be consistent
win = pygame.display.set_mode((750, 750))
pygame.display.set_caption("Space Invader by Mazz Ather!")

# After pygame initialization, scale the background to fit the window
bg = pygame.image.load('bg-img.png')
bg = pygame.transform.scale(bg, (750, 750))  # Scale background to window size

white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)
green = (0, 255, 0)
score = 0  # Add score tracking

# Modify the redraw function
def redraw():
    win.blit(bg, (0, 0))
    
    # Create a semi-transparent bottom panel only for score
    bottom_surface = pygame.Surface((200, 40))
    bottom_surface.set_alpha(128)
    bottom_surface.fill(black)
    win.blit(bottom_surface, (550, 700))

    # Score only
    font = pygame.font.Font(None, 36)
    score_text = font.render(f"Score: {score}", True, white)
    win.blit(score_text, (570, 710))

    # Game title
    title = font.render("Space Invader by Mazz Ather", True, white)
    win.blit(title, (250, 10))

    # Draw objects
    ship.draw()
    enemy_list.draw(win)
    missile_list.draw(win)
    bomb_list.draw(win)

    pygame.display.update()

# Modify bunker creation (reduce number of bunkers)
# First define all classes
class Ship(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("ship.png")  # Changed from .jpeg to .png
        self.image = pygame.transform.scale(self.image, (50, 50))
        self.original_image = self.image.copy()
        self.rect = self.image.get_rect()
        self.lives = 3
        self.invulnerable = False
        self.invulnerable_timer = 0

    def draw(self):
        if self.invulnerable:
            if pygame.time.get_ticks() % 200 < 100:
                self.image.fill((255, 0, 0, 128), special_flags=pygame.BLEND_RGBA_MULT)
            else:
                self.image = self.original_image.copy()
        win.blit(self.image, (self.rect.x, self.rect.y))

class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("enemy.jpeg")  # Changed from .jpeg to .png
        self.image = pygame.transform.scale(self.image, (40, 40))
        self.rect = self.image.get_rect()
        self.direction = 5

    def update(self):
        self.rect.x += self.direction
        if self.rect.right >= 750 or self.rect.left <= 0:
            self.direction *= -1
            self.rect.y += 20

class Missile(pygame.sprite.Sprite):
    def __init__(self, x, y):  # Added x, y parameters
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("missile.png")  # Changed from .jpeg to .png
        self.image = pygame.transform.scale(self.image, (10, 20))
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
        self.direction = -10

    def update(self):
        self.rect.y += self.direction
        if self.rect.bottom < 0:
            self.kill()

class Bomb(pygame.sprite.Sprite):
    def __init__(self, x, y):  # Added x, y parameters
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("bomb.jpeg")  # Changed from .jpeg to .png
        self.image = pygame.transform.scale(self.image, (15, 15))
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)

    def update(self):
        self.rect.y += 10
        if self.rect.top >= 750:
            self.kill()

class Bunker(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("bunker.jpeg")
        self.image = pygame.transform.scale(self.image, (50, 50))
        self.rect = self.image.get_rect()

# Remove these duplicate class definitions
# class Missile(pygame.sprite.Sprite):
#     def __init__(self):
#         pygame.sprite.Sprite.__init__(self)
#         self.image = pygame.image.load("missile.jpeg")
#         self.image = pygame.transform.scale(self.image, (50, 50))
#         self.rect = self.image.get_rect()

# class Bomb(pygame.sprite.Sprite):
#     def __init__(self):
#         pygame.sprite.Sprite.__init__(self)
#         self.image = pygame.image.load("bomb.jpeg")
#         self.image = pygame.transform.scale(self.image, (50, 50))
#         self.rect = self.image.get_rect()

# Then initialize sprite groups
enemy_list = pygame.sprite.Group()
bunker_list = pygame.sprite.Group()
missile_list = pygame.sprite.Group()
bomb_list = pygame.sprite.Group()

# Create the ship
ship = Ship()
ship.rect.x = 350
ship.rect.y = 650

# Then create bunkers
for col in range(4):
    bunker = Bunker()
    bunker.rect.x = 150 + col * 150
    bunker.rect.y = 550
    bunker_list.add(bunker)

# Then create enemies
for row in range(1, 6):
    for col in range(1, 11):
        enemy = Enemy()
        enemy.rect.x = 50 + col * 50
        enemy.rect.y = 50 + row * 50
        enemy_list.add(enemy)

def redraw():
    win.blit(bg, (0, 0))
    bottom = pygame.draw.rect(win, black, (0, 700, 750, 50))

    # Ship lives
    for live in range(ship.lives):
        win.blit(ship.image, (live * 30, 700))

    # Game title
    font = pygame.font.Font(None, 36)
    title = font.render("Space Invader by Mazz Ather", True, white)
    win.blit(title, (300, 10))

    # Draw objects
    ship.draw()
    enemy_list.draw(win)
    bunker_list.draw(win)
    missile_list.draw(win)
    bomb_list.draw(win)

    pygame.display.update()

run = True

# Replace the game loop collision and update section
while run:
    pygame.time.delay(50)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    # Movement
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and ship.rect.left > 0:
        ship.rect.x -= 7

    if keys[pygame.K_RIGHT] and ship.rect.right < 750:
        ship.rect.x += 7

    if keys[pygame.K_SPACE]:
        if len(missile_list) < 5:
            missile = Missile(ship.rect.centerx, ship.rect.top)
            missile_list.add(missile)

    # Update sprites
    missile_list.update()
    bomb_list.update()
    enemy_list.update()

    # Missile hits
    for missile in missile_list:
        # Check enemy hits
        for enemy in enemy_list:
            if missile.rect.colliderect(enemy.rect):
                enemy.kill()
                missile.kill()
                score += 100
                break  # Exit after first hit
        # Check bunker hits
        for bunker in bunker_list:
            if missile.rect.colliderect(bunker.rect):
                missile.kill()
                break

    # Enemy bombs
    if len(enemy_list) > 0:  # Only shoot if enemies exist
        if random.randint(1, 150) <= 5:  # Reduce bomb frequency
            random_enemy = random.choice(enemy_list.sprites())
            bomb = Bomb(random_enemy.rect.centerx, random_enemy.rect.bottom)
            bomb_list.add(bomb)

    # Bomb hits
    for bomb in bomb_list:
        if bomb.rect.colliderect(ship.rect) and not ship.invulnerable:
            ship.lives -= 1
            ship.invulnerable = True
            ship.invulnerable_timer = pygame.time.get_ticks()
            bomb.kill()
            
            # Display life lost message
            font = pygame.font.Font(None, 48)
            life_lost = font.render(f"Lives Left: {ship.lives}!", True, red)
            life_lost_rect = life_lost.get_rect(center=(375, 375))
            win.blit(life_lost, life_lost_rect)
            pygame.display.update()
            pygame.time.delay(1000)
            
            if ship.lives == 0:
                font = pygame.font.Font(None, 74)
                game_over = font.render(f"Game Over! Score: {score}", True, red)
                game_over_rect = game_over.get_rect(center=(375, 375))
                win.blit(game_over, game_over_rect)
                pygame.display.update()
                pygame.time.delay(2000)
                run = False
                break
        
        for bunker in bunker_list:
            if bomb.rect.colliderect(bunker.rect):
                bunker.kill()
                bomb.kill()
                break

    # Update ship invulnerability
    if ship.invulnerable:
        if pygame.time.get_ticks() - ship.invulnerable_timer > 2000:
            ship.invulnerable = False
            ship.image = ship.original_image.copy()

    # Check for win condition
    if len(enemy_list) == 0:
        font = pygame.font.Font(None, 74)
        win_text = font.render(f"You Win! Score: {score}", True, green)
        win_text_rect = win_text.get_rect(center=(375, 375))
        win.blit(win_text, win_text_rect)
        pygame.display.update()
        pygame.time.delay(2000)
        run = False

    redraw()

pygame.quit()