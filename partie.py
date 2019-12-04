from player import Player
from game import Game

class Partie:

    def __init__(self,player):
        # instanciation of game
        self.player=player
        self.player.choix_deficulte()
        self.game=Game(self.player)

    
    def partie(self):
        
        message=""
        while message !="lose":
            message=self.game.serie_simon()
        self.game.player.score=len(self.game.serie)-1
        return " a un  score de {} avec le niveau {} .".format(self.game.player.score,self.game.player.deficulte)


        



