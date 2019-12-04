from player import Player
class Game:

    def __init__(self,player):
        self.palyer= palyer

    def deficult():
        liste=["facile","moyen","difficile"]
        repense=""
        while repense not in liste:
            repense=input("quel niveau de dificulté vous souhaité parmis {}".format(liste))
        return repense

    
    def generer_un_nombre(self, deficulte):
        import random
        if deficulte=="facile":
            return random.randint(1, 10)
        if deficulte=="moyen":
            return random.randint(0, 20)
        if deficulte=="difficile":
            return random.randint(1, 100)

