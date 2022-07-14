#################################
## Game settings and Constants ##
#################################
import pygame as pygame
# Constants
TITLE = 'CLASSIC BREW'
WIDTH = 1080
HEIGHT = 720
FPS = 30
TILE_SIZE = 24
GRID_WIDTH = 45 # 1080 / TILE_SIZE 
GRID_HEIGHT = 30 # 720 / TILE_SIZE  

# Game Properties
MENU_LAYER = 3
POINTER_LAYER = 1 
PLAYER_LAYER = 2
SELECTION_LAYER = 0

# Colors
WHITE = pygame.Color('white')
BLACK = pygame.Color('black')
RED = pygame.Color('red')
GREEN = pygame.Color('green')
BLUE = pygame.Color('blue')
GREY = pygame.Color('grey')
YELLOW = pygame.Color('yellow')