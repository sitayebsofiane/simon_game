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

    def serie_simon(slef,deficulte):
        import time
        nombre=generer_un_nombre(deficulte)
        #affichage de la serie
        for i in serie:
            time.sleep(nombre[1])
            print(i)
        message=""
        #verification si il a gagné
        for i in serie:
            entrer=int(input("nombre: "))
            if entrez != i:
                message="lose"
                break
        return message


        





