class Player:
    
    def __init__(self):
        self.score=0 #initialisation of score  zero
        self.deficulte="" #initialisation of deficulté  null
        name="" 
        while not name.isalpha() or len(name)<2:
            name=input("entrez votre nom: ")
        print("bienvenue {} ".format(name))
        self.name=name
    # slect difficult of game
    def choix_deficulte(self):
        liste=["facile","moyen","difficile"]
        repense=""
        while repense not in liste:
            repense=input("quel niveau de dificulté vous souhaité parmis {}".format(liste))
        self.deficulte=repense

    # the method to ask number for play 
    def play(self):
        import os
        try:
            number=int(input("entrez la serie de nombre affiché a l'écran: "))
            os.system("clear")
            return number
        except:
            return -1
    # the method represente of palyer
    def __str__(self):
        """when we ask our object palyer we have informations"""
        return " nom({}), deficulte({}), score({})".format(
                self.name, self.deficulte, self.score)
    