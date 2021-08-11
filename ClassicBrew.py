###################
## CLASSIC BREW ###
###################

import pygame as pg
import random 
from Settings2 import *
from Sprites import *

class Game:
    def __init__(self):
        # Initialize game window, etc
        self.running = True
        pg.init()
        pg.mixer.init()
        pg.key.set_repeat(80, 80)
        self.screen = pg.display.set_mode((WIDTH +1 , HEIGHT + 1))
        pg.display.set_caption(TITLE)
        self.clock = pg.time.Clock()

    def new(self):
        # Start new game
        self.menu_running = False
        self.all_sprites = pg.sprite.LayeredUpdates()
        self.player_characters = pg.sprite.Group()
        self.pointer = Pointer(self, 20, 15)
        self.player = Player_Character(self, 20, 20)
        self.run()

    def run(self):
        # Game loop 
        self.clock.tick(FPS)
        self.playing = True
        while self.playing:
            self.clock.tick(FPS)
            self.events()
            self.update()
            self.draw()

    def update(self):
        # Game loop - Update
        self.all_sprites.update() 
        self.selection_check()  

    def events(self):
        # Game loop - Events
        for event in pg.event.get():
            # Check for closing window
            if event.type == pg.QUIT:
                if self.playing:
                    self.playing = False
                self.running = False
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_ESCAPE:
                    self.running = False
                if event.key == pg.K_DOWN:
                    self.pointer.move(y = 1)
                if event.key == pg.K_UP:
                    self.pointer.move(y = -1)
                if event.key == pg.K_RIGHT:
                    self.pointer.move(x = 1)
                if event.key == pg.K_LEFT:
                    self.pointer.move(x = -1)
    
    def draw(self):
        # Game loop - Draw
        self.screen.fill(BLACK)
        self.draw_grid()
        self.all_sprites.draw(self.screen)
        pg.display.flip()

    def draw_grid(self):
        # Draws a grey grid over the screen 
        for x in range(0, WIDTH, TILE_SIZE):
            pg.draw.line(self.screen, GREY, (x,0), (x, HEIGHT))
        for y in range(0, HEIGHT, TILE_SIZE):
            pg.draw.line(self.screen, GREY, (0, y), (WIDTH, y))
        pg.draw.line(self.screen, GREY, (WIDTH, 0), (WIDTH , HEIGHT))
        pg.draw.line(self.screen, GREY, (0, HEIGHT), (WIDTH, HEIGHT))

### GAME FUNCTIONS

    def selection_check(self):
        select = pg.sprite.spritecollide(self.pointer, self.player_characters, False, collided = None)
        if select:
            self.pointer.image.fill(YELLOW)
            if self.menu_running is not True:
                self.menu = Menu(self, self.pointer.x / TILE_SIZE + 1.5, self.pointer.y / TILE_SIZE + 0.5)
                self.menu_running = True
        else:
            self.pointer.image.fill(GREEN)
            if self.menu_running is True:
                self.menu_running = False

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
    g.new()
    g.show_go_screen()

pg.quit()