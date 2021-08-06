###################
## CLASSIC BREW ###
###################

import pygame as pg
import random 
from Settings import *
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
        self.pointer = Pointer(self, 20, 15)
        self.player = Player_Character(self, 20, 20)
        self.all_sprites = pg.sprite.Group()
        self.all_sprites.add(self.player)
        self.all_sprites.add(self.pointer)
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
        self.all_sprites.draw(self.screen)
        self.draw_grid()
        pg.display.flip()

    def draw_grid(self):
        # Draws a grey grid over the screen 
        for x in range(0, WIDTH, TILE_SIZE):
            pg.draw.line(self.screen, GREY, (x,0), (x, HEIGHT))
        for y in range(0, HEIGHT, TILE_SIZE):
            pg.draw.line(self.screen, GREY, (0, y), (WIDTH, y))
        pg.draw.line(self.screen, GREY, (WIDTH, 0), (WIDTH , HEIGHT))
        pg.draw.line(self.screen, GREY, (0, HEIGHT), (WIDTH, HEIGHT))

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