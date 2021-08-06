from Settings import *
from Classes import *
import pygame as pg

class Pointer(pg.sprite.Sprite):
    def __init__(self, game, x, y):
        pg.sprite.Sprite.__init__(self)
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
        pg.sprite.Sprite.__init__(self)
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