# state file that contains base gameplay state
from State import State
import Settings2 
import pygame
import GameFunctions

class BaseGameplay(State):
    def __init__(self,game):
        State.__init__ (self, game)

    def events(self):
        for event in pygame.event.get():
            # Check for closing window
            GameFunctions.check_quit(event, self.game)
            # Check if any keys are pressed down
            if event.type == pygame.KEYDOWN:
                # Check for pressed escape button
                if event.key == pygame.K_ESCAPE:
                    self.game.running = False
                # Check for cursor direction inputs
                if event.key == pygame.K_DOWN:
                    self.game.pointer.move(y = 1)
                if event.key == pygame.K_UP:
                    self.game.pointer.move(y = -1)
                if event.key == pygame.K_RIGHT:
                    self.game.pointer.move(x = 1)
                if event.key == pygame.K_LEFT:
                    self.game.pointer.move(x = -1)

    def update(self):
        self.game.all_sprites.update() 
        self.game.selection_check() 

    def draw(self):
        # Gameplay loop
        self.game.screen.fill(Settings2.BLACK)
        GameFunctions.draw_grid(self.game)
        self.game.all_sprites.draw(self.game.screen)
        pygame.display.flip()
