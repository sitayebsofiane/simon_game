from player import Player
class Game:

    def __init__(self,player):
        self.serie=list()
        self.player= player

    # retourn random number and time of each livel deficulte 
    def generate_number(self, deficulte):
        import random
        if deficulte=="facile":
            return random.randint(1, 10),3 
        if deficulte=="moyen":
            return random.randint(1, 20),2
        if deficulte=="difficile":
            return random.randint(1, 100),1

    def serie_simon(self):
        import time,os
        nombre=self.generate_number(self.player.deficulte)
        self.serie.append(nombre[0])
        #display seris
        print(" ".join(str(x) for x in self.serie))
        time.sleep(nombre[1])
        os.system("clear")
        message=""
        #check if he win
        for i in self.serie:
            entrer=self.player.play()
            if entrer != i:
                message="lose"
                break
        return message

    
        





