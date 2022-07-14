from Sprites import *
from Classes2 import *
from Settings2 import *
from ClassicBrew import *

def distance_check_TEST():
    game = Game()
    p1 = Player_Character(game, 2, 2)
    p2 = Player_Character(game, 5, 4)
    print(p1.distance_check(p2))

distance_check_TEST()
