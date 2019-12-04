class Player:
    
    def __init__(self):
        self.score=0 #initialisation du score a zero
        self.deficulte="" #initialisation du deficulté a null
        nom=""
        while not nom.isalpha() or len(nom)<2:
            nom=input("entrez votre nom: ")
        self.nom=nom
    
    def choix_deficulte(self):
        liste=["facile","moyen","difficile"]
        repense=""
        while repense not in liste:
            repense=input("quel niveau de dificulté vous souhaité parmis {}".format(liste))
        self.deficulte=repense

    
    def jouer(self):
        try:
            nombre=int(input("entrez la serie du nombre afficher a l'écran: "))
            return nombre
        except:
            "print vous avez tapez autre chose qu'un nombre entier"