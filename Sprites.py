from Settings2 import *
from Classes2 import *
import pygame
from math import sqrt

### utility variables and functions
font_name = pygame.font.match_font('arial')

def draw_text(surface, color, text, size, x, y):
    # x and y are in pixels for this function
    font = pygame.font.Font(font_name, size)
    text_surface = font.render(text, True, color)
    text_rect = text_surface.get_rect()
    text_rect.x = x
    text_rect.y = y
    surface.blit(text_surface, text_rect)

# Pointer is a cursor for the user to select charaters
class Pointer(pygame.sprite.Sprite):
    def __init__(self, game, x, y):
        self._layer = POINTER_LAYER 
        self.groups = game.all_sprites 
        pygame.sprite.Sprite.__init__(self, self.groups)
        self.game = game
        self.x = x * TILE_SIZE
        self.y = y * TILE_SIZE
        self.rect = pygame.Rect(self.x, self.y, TILE_SIZE, TILE_SIZE)
        self.image = pygame.Surface((TILE_SIZE, TILE_SIZE))
        self.image.fill(GREEN)

    def move(self, x=0, y=0):
        self.x += x * TILE_SIZE
        self.y += y * TILE_SIZE

    def update(self):
        self.rect.x = self.x
        self.rect.y = self.y 

class Player_Character(pygame.sprite.Sprite, Character):
    def __init__(self, game, x, y, player_class = Character):
        self._layer = PLAYER_LAYER
        self.groups = game.all_sprites, game.player_characters
        pygame.sprite.Sprite.__init__(self, self.groups)
        player_class.__init__(self)
        self.game = game
        self.x = x 
        self.y = y 
        self.rect = pygame.Rect(self.x, self.y, TILE_SIZE, TILE_SIZE)
        self.image = pygame.Surface((TILE_SIZE, TILE_SIZE))
        self.image.set_colorkey(BLACK)

    def move(self, x=0, y=0):
        self.x += x * TILE_SIZE
        self.y += y * TILE_SIZE

    def update(self):
        pygame.draw.circle(self.image, BLUE, (self.image.get_width() //2, self.image.get_height() // 2), TILE_SIZE // 2 - 1)
        self.rect.x = self.x * TILE_SIZE
        self.rect.y = self.y * TILE_SIZE
    
    def distance_check(self, point_x, point_y):
        # if distance from point is less than scope, returns true.
        if sqrt((self.y - point_y)**2 + (self.x - point_x)**2) < self.getScope():
            return True
        else:
            return False

class Menu(pygame.sprite.Sprite):
    def __init__(self, game, player, x, y):
        self._layer = MENU_LAYER
        self.groups = game.all_sprites
        pygame.sprite.Sprite.__init__(self, self.groups)
        self.game = game
        self.player = player
        self.x = x
        self.y = y 
        self.rect = pygame.Rect(self.x * TILE_SIZE, self.y * TILE_SIZE, TILE_SIZE * 6, TILE_SIZE * 4)
        self.image = pygame.Surface((TILE_SIZE * 6, TILE_SIZE * 4))
        self.image.fill(GREY)

    def menu_selection1(self):
        # Menu displayed while hovering over player character
        draw_text(self.image, BLACK, '1) Move', 16, 10, 10)
        draw_text(self.image, BLACK, '2) Attack', 16, 10, 30)
        draw_text(self.image, BLACK, '3) Select other', 16, 10, 50)
        # Check for events
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_1:
                    self.game.move_selection(self.player)

    def update(self):
        self.menu_selection1()
        if self.game.menu_running is False:
            self.kill()

class Highlight_Rect(pygame.sprite.Sprite):
    def __init__(self, game, x, y):
        self._layer = SELECTION_LAYER
        self.groups = game.all_sprites
        pygame.sprite.Sprite.__init__(self, self.groups)
        self.game = game
        self.x = x 
        self.y = y 
        self.rect = pygame.Rect(self.x * TILE_SIZE, self.y * TILE_SIZE, TILE_SIZE, TILE_SIZE)
        self.image = pygame.Surface((TILE_SIZE - 1, TILE_SIZE - 1))
        self.image.fill(BLUE)

    def update(self):
        self.rect.x = self.x * TILE_SIZE
        self.rect.y = self.y * TILE_SIZE