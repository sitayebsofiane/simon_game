from player import Player
from game import Game

class Partie:

    @classmethod
    def partie(cls,player):
        game=Game(player)
        game.player.choix_deficulte()
        message=game.generer_une_serie(game.palyer.deficulte)
        while message !="lose":
            nombre=game.palyer.jouer()
            message=generer_une_serie(game.palyer.deficulte)
        game.player.score=len(game.serie)-1

        



