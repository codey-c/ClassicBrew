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
    def __init__(self, game, x, y):
        self._layer = MENU_LAYER
        # self.groups = game.all_sprites
        # pygame.sprite.Sprite.__init__(self, self.groups)
        self.game = game
        # self.player = player
        self.x = x
        self.y = y 
        self.rect = pygame.Rect(self.x * TILE_SIZE, self.y * TILE_SIZE, TILE_SIZE * 6, TILE_SIZE * 4)
        self.image = pygame.Surface((TILE_SIZE * 4.25, TILE_SIZE * 4.25))
        self.image.fill(GREY)

        # # Check for events                                # Legacy code: Menu no longer utilizes a scrolling selection mechanism
        # for event in pygame.event.get():
        #     if event.type == pygame.KEYDOWN:
        #         if event.key == pygame.K_1:                       
        #             self.game.move_selection(self.player)

    def update(self):
        # if pointer over character, relocate menu position
        select = pygame.sprite.spritecollide(self.game.pointer, self.game.player_characters, False, collided = None)
        if select:                  
            self.x = (select[-1].x + 1.5 ) * TILE_SIZE          
            self.y = (select[-1].y + .5 ) * TILE_SIZE

    def draw(self):
        # Menu displayed while pointer is hovering over player character
        select = pygame.sprite.spritecollide(self.game.pointer, self.game.player_characters, False, collided = None)
        if select:
            # print(select[-1].x)
            self.game.screen.blit(self.image, (self.x, self.y))
            draw_text(self.image, BLACK, select[-1].class_name, 16, 10, 10)
            draw_text(self.image, BLACK, "HP: " + str(select[-1].getHealth()), 16, 10, 30)
            draw_text(self.image, BLACK, '1) Move', 16, 30, 50)
            draw_text(self.image, BLACK, '2) Attack', 16, 30, 70)

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