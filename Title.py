# state file that contains the title screen
from State import State
import Settings2 
import pygame
import GameFunctions

class Title(State):
    def __init__ (self, game):
        State.__init__(self, game)
        self.image = pygame.Surface((200,200))
        self.rect = self.image.get_rect()

    def events(self):
        for event in pygame.event.get():
            # Check for closing window
            GameFunctions.check_quit(event, self.game)
            # Check for selection 
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_1:
                    self.game.new()
                    print(self.game.pointer)
                    self.switch_state("BaseGameplay")

    def update(self):
        pass
    
    def draw(self):
        # self.game.screen.fill(Settings2.GREEN)
        # self.game.screen.blit(self.image, (50,50))
        GameFunctions.draw_text(self.game.screen, Settings2.WHITE, "ClassicBrew", 55, (Settings2.WIDTH/2) - 150,  (Settings2.HEIGHT/2)- 95)
        GameFunctions.draw_text(self.game.screen, Settings2.WHITE, "\u2022 Press '1' to start new game", 25, (Settings2.WIDTH/2) - 150,  (Settings2.HEIGHT/2)- 15)
        GameFunctions.draw_text(self.game.screen, Settings2.WHITE, "\u2022 Press 'Esc' at anytime time ", 25, (Settings2.WIDTH/2) - 150,  (Settings2.HEIGHT/2) + 25)
        GameFunctions.draw_text(self.game.screen, Settings2.WHITE, "   to return to main menu", 25, (Settings2.WIDTH/2) - 150,  (Settings2.HEIGHT/2) + 55)

        pygame.display.flip()