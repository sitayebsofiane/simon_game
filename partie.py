from player import Player
from game import Game

class Partie:

    def __init__(self):
        self.player=Player()
        self.player.choix_deficulte()
        self.game=Game(self.player)

    
    def partie(self):
        
        message=self.game.serie_simon(self.player.deficulte)
        while message !="lose":
            nombre=self.game.palyer.jouer()
            message=serie(self.palyer.deficulte)
        self.game.player.score=len(self.game.serie)-1

        



