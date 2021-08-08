from Settings2 import *
from Classes2 import *
import pygame as pg

class Pointer(pg.sprite.Sprite):
    def __init__(self, game, x, y):
        self._layer = POINTER_LAYER 
        self.groups = game.all_sprites 
        pg.sprite.Sprite.__init__(self, self.groups)
        self.game = game
        self.x = x * TILE_SIZE
        self.y = y * TILE_SIZE
        self.rect = pg.Rect(self.x, self.y, TILE_SIZE, TILE_SIZE)
        self.image = pg.Surface((TILE_SIZE, TILE_SIZE))
        self.image.fill(GREEN)

    def move(self, x=0, y=0):
        self.x += x * TILE_SIZE
        self.y += y * TILE_SIZE

    def update(self):
        self.rect.x = self.x
        self.rect.y = self.y 

class Player_Character(pg.sprite.Sprite, Character):
    def __init__(self, game, x, y, player_class = Character):
        self._layer = PLAYER_LAYER
        self.groups = game.all_sprites, game.player_characters
        pg.sprite.Sprite.__init__(self, self.groups)
        player_class.__init__(self)
        self.game = game
        self.x = x * TILE_SIZE
        self.y = y * TILE_SIZE
        self.rect = pg.Rect(self.x, self.y, TILE_SIZE, TILE_SIZE)
        self.image = pg.Surface((TILE_SIZE, TILE_SIZE))
        self.image.fill(BLUE)

    def move(self, x=0, y=0):
        self.x += x * TILE_SIZE
        self.y += y * TILE_SIZE

    def update(self):
        self.rect.x = self.x
        self.rect.y = self.y 

class Menu(pg.sprite.Sprite):
    def __init__(self, game, x, y):
        self._layer = MENU_LAYER
        self.groups = game.all_sprites
        pg.sprite.Sprite.__init__(self, self.groups)
        self.game = game
        self.x = x * TILE_SIZE
        self.y = y * TILE_SIZE
        self.rect = pg.Rect(self.x, self.y, TILE_SIZE * 6, TILE_SIZE * 4)
        self.image = pg.Surface((TILE_SIZE * 6, TILE_SIZE * 4))
        self.image.fill(GREY)

    def update(self):
        self.rect.x = self.x
        self.rect.y = self.y 
        if self.game.menu_running is False:
            self.kill()

    