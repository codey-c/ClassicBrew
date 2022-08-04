# Cookie cutter class for class objects
class Character(object):
    """Cookie cutter for polymorphing charater classes"""

    def __init__(self, health=9, speed=8, offense=6, defense=4, scope=1):
        self.class_name = "Character"
        self.__health = health
        self.__speed = speed
        self.__offense = offense
        self.__defense = defense
        self.__scope = scope
        self.__xaxis = float(0)
        self.__yaxis = float(0)
        
# Representation 
    def __repr__(self):
        return 'characters superclass'

    def __str__(self):
        return type(self).__name__

# Getters
    def getStats(self):
        print('Offense, Defense, Range, Speed')
        return self.__health, self.__speed, self.__offense, self.__defense, self.__scope

    def getHealth(self):
        return self.__health

    def getScope(self):
        return self.__scope

    def getOffense(self):
        return self.__offense

    def getDefense(self):
        return self.__defense

    def getSpeed(self):
        return self.__speed

    def getX(self):
        return self.__xaxis

    def getY(self):
        return self.__yaxis

    def getLocation(self):
        return self.__xaxis, self.__yaxis
    
#Setters
    def setHealth(self, value):
        self.__health = value

    def setScope(self, value):
        self.__scope = value

    def setOffense(self, value):
        self.__offense = value

    def setDefense(self, value):
        self.__defense = value

    def setSpeed(self, value):
        self.__speed = value

    def setX(self, value):
        self.__xaxis = value

    def setY(self, value):
        self.__yaxis = value
        

#initialization
class Footman(Character):
    """Footman character is the vanilla/pawn character of the game - base stats"""

    def __init__(self):
        Character.__init__(self)
        self.class_name = "Footman"

    def __repr__(self):
        return 'Characters Footman Class'
      
class Ranger(Character):
    """Ranger class has high Scope and low Defense"""

    def __init__(self):
        Character.__init__(self, 9, 11, 8, 4, 6)

    def __repr__(self):
        return 'Characters Ranger Class'

class Scout(Character):
    """Scout class has high Speed and low Offense"""

    def __init__(self):
        Character.__init__(self, 9, 13, 6, 6, 4)

    def __repr__(self):
        return 'Characters Scout Class'

class Knight(Character):
    """Knight class has high Defense and low Speed"""

    def __init__(self):
        Character.__init__(self, 9, 8, 9, 9, 3)

    def __repr__(self):
        return 'Characters Knight Class'

class Clansman(Character):
    """Clansman class has high Offense and low Scope"""

    def __init__(self):
        Character.__init__(self, 9, 11, 11, 7, 1)

    def __repr__(self):
        return 'Characters Clansman Class'
        

