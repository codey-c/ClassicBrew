###################
## CLASSIC BREW ###
###################

# This module is the main game loop for ClassicBrew.  It runs the main loop, calling 
# states update functions to achieve game functionality. 

import pygame
import random
import BaseGameplay 
from Settings2 import *
from Sprites import *
from math import sqrt
import Classes2
import Title

class Game:
    def __init__(self):
        # Initialize game window, etc
        self.running = True
        pygame.init()
        pygame.mixer.init()
        pygame.key.set_repeat(150, 150)
        self.screen = pygame.display.set_mode((WIDTH +1 , HEIGHT + 1))
        pygame.display.set_caption(TITLE)
        self.clock = pygame.time.Clock()
        self.states = {"Title": Title.Title(self), "BaseGameplay": BaseGameplay.BaseGameplay(self)}
        self.current_state = "Title"
        self.menu = Menu(self, 50, 50)

    def new(self):
        # Start new game. 'Initiates' each game by creating instances of all 
        # objects needed to run game. 
        self.menu_running = False   # TD: change hover-menu into an object(sprite?)
        self.all_sprites = pygame.sprite.LayeredUpdates()
        self.player_characters = pygame.sprite.Group()
        self.pointer = Pointer(self, 20, 18)
        self.player = Player_Character(self, 20, 20, Classes2.Footman)

    def run(self):
        # Game loop 
        self.clock.tick(FPS)
        self.playing = True
        while self.playing:
            self.clock.tick(FPS)
            self.states[self.current_state].events()
            self.states[self.current_state].update()
            self.states[self.current_state].draw()

    # def update(self):                 Legacy code: Game class no longer updates - states and sprites update
    #     # Game loop - Update
    #     self.all_sprites.update() 
    #     self.selection_check()  

    # def events(self):                Legacy code: Game class no longer seeks events - states and sprites update                         
    #     # Game loop - Events
    #     for event in pygame.event.get():
    #         # Check for closing window
    #         if event.type == pygame.QUIT:
    #             if self.playing:
    #                 self.playing = False
    #             self.running = False
    #         if event.type == pygame.KEYDOWN:
    #             if event.key == pygame.K_ESCAPE:
    #                 self.running = False
    #             if event.key == pygame.K_DOWN:
    #                 self.pointer.move(y = 1)
    #             if event.key == pygame.K_UP:
    #                 self.pointer.move(y = -1)
    #             if event.key == pygame.K_RIGHT:
    #                 self.pointer.move(x = 1)
    #             if event.key == pygame.K_LEFT:
    #                 self.pointer.move(x = -1)
    
    def draw(self):
        # Game loop - Draw
        self.screen.fill(RED)
        self.draw_grid()
        self.all_sprites.draw(self.screen)
        pygame.display.flip()

    def draw_grid(self):
        # Draws a grey grid over the screen 
        for x in range(0, WIDTH, TILE_SIZE):
            pygame.draw.line(self.screen, GREY, (x,0), (x, HEIGHT))
        for y in range(0, HEIGHT, TILE_SIZE):
            pygame.draw.line(self.screen, GREY, (0, y), (WIDTH, y))
        pygame.draw.line(self.screen, GREY, (WIDTH, 0), (WIDTH , HEIGHT))
        pygame.draw.line(self.screen, GREY, (0, HEIGHT), (WIDTH, HEIGHT))

### GAME FUNCTIONS

    # selection_check checks whether the cursor is over a character 
    def selection_check(self):
        select = pygame.sprite.spritecollide(self.pointer, self.player_characters, False, collided = None)
        if select:
            self.pointer.image.fill(YELLOW)
            if self.menu_running is not True:
                self.menu = Menu(self, select[0], self.pointer.x / TILE_SIZE + 1.5, self.pointer.y / TILE_SIZE + 0.5)
                self.menu_running = True
        else:
            self.pointer.image.fill(GREEN)
            if self.menu_running is True:
                self.menu_running = False

    def move_selection(self, player):
        for x in range(GRID_WIDTH):
            for y in range(GRID_HEIGHT):
                Highlight_Rect(self, x, y)

    def menu_run(self):
        self.menu = Menu(self, self.pointer.x + 1, self.pointer.y)
        self.all_sprites.add(self.menu)

###

    def show_start_screen(self):
        # Game splash/start screen
        pass

    def show_go_screen(self):
        # Game over/continue screen
        pass

g = Game()
g.show_start_screen()
while g.running:
    g.run()
    g.show_go_screen()

pygame.quit()