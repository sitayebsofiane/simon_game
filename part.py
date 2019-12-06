from player import Player
from game import Game

class Part:

    def __init__(self,player):
        # instanciation of game
        self.player=player
        self.player.choix_deficulte()
        self.game=Game(self.player)

    
    def part(self):
        
        while self.game.serie_simon():pass
        self.game.player.score=len(self.game.serie)-1
        return self.player


        



