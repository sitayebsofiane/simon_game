from player import Player
class Game:

    def __init__(self,player):
        self.serie=list()
        self.player= player

    # retourne le nombre aleatoire et le temps de sleep
    def generer_un_nombre(self, deficulte):
        import random
        if deficulte=="facile":
            return random.randint(1, 10),3 
        if deficulte=="moyen":
            return random.randint(1, 20),2
        if deficulte=="difficile":
            return random.randint(1, 100),1

    def serie_simon(self):
        import time,os
        nombre=self.generer_un_nombre(self.player.deficulte)
        self.serie.append(nombre[0])
        #affichage de la serie
        print(self.serie)
        time.sleep(nombre[1])
        os.system("clear")
        message=""
        #verification si il a gagné
        for i in self.serie:
            entrer=self.player.jouer()
            if entrer != i:
                message="lose"
                break
        return message

    
        





