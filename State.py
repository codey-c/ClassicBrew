# Abstract base class for state objects

class State():
    def __init__ (self, game):
        self.game = game

    def events(self):
        pass

    def update(self):
        pass

    def draw(self):
        pass

    def switch_state(self, state_name):
        self.game.current_state = state_name
