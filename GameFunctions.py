import pygame 
from Settings2 import *

# font_name = pygame.font.match_font('arial')

def draw_text(surface, color, text, size, x, y):
    # x and y are in pixels for this function
        font_name = pygame.font.match_font('arial')
        font = pygame.font.Font(font_name, size)
        text_surface = font.render(text, True, color)
        text_rect = text_surface.get_rect()
        text_rect.x = x
        text_rect.y = y
        surface.blit(text_surface, text_rect)

def check_quit(event, game):
     if event.type == pygame.QUIT:
                if game.playing:
                    game.playing = False
                game.running = False

def draw_grid(game):
        # Draws a grey grid over the screen 
        for x in range(0, WIDTH, TILE_SIZE):
            pygame.draw.line(game.screen, GREY, (x,0), (x, HEIGHT))
        for y in range(0, HEIGHT, TILE_SIZE):
            pygame.draw.line(game.screen, GREY, (0, y), (WIDTH, y))
        pygame.draw.line(game.screen, GREY, (WIDTH, 0), (WIDTH , HEIGHT))
        pygame.draw.line(game.screen, GREY, (0, HEIGHT), (WIDTH, HEIGHT))