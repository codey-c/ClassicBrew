#################################
## Game settings and Constants ##
#################################
import pygame as pg
# Constants
TITLE = 'CLASSIC BREW'
WIDTH = 1080
HEIGHT = 720
FPS = 60
TILE_SIZE = 24
GRID_WIDTH = 1080 / TILE_SIZE # 45 
GRID_HEIGHT = 720 / TILE_SIZE # 30 

# Game Properties
MENU_LAYER = 3
POINTER_LAYER = 1 
PLAYER_LAYER = 2

# Colors
WHITE = pg.Color('white')
BLACK = pg.Color('black')
RED = pg.Color('red')
GREEN = pg.Color('green')
BLUE = pg.Color('blue')
GREY = pg.Color('grey')
YELLOW = pg.Color('yellow')