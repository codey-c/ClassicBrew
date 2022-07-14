# state file that contains the title screen
from State import State
import Settings2 
import pygame

class Title(State):
    def __init__ (self, game):
        State.__init__(self, game)

    def events(self):
        for event in pygame.event.get():
            # Check for closing window
            if event.type == pygame.QUIT:
                if self.playing:
                    self.playing = False
                self.running = False

    def update(self):
        pass
    
    
    def draw_text(surface, color, text, size, x, y):
    # x and y are in pixels for this function
        font_name = pygame.font.match_font('arial')
        font = pygame.font.Font(font_name, size)
        text_surface = font.render(text, True, color)
        text_rect = text_surface.get_rect()
        text_rect.x = x
        text_rect.y = y
        surface.blit(text_surface, text_rect)

    def draw(self):
        self.game.screen.fill(Settings2.GREEN)
        pygame.display.flip()
    

