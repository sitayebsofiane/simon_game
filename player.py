class Player:
    
    def __init__(self):
        self.score=0 #initialisation du score a zero
        nom=""
        self.deficulte=None #initialisation du deficulté a null
        while not (nom.isalpha or len(nom)>2):
            self.nom=input("entrez votre nom")
    
    def choix_deficulte():
        liste=["facile","moyen","difficile"]
        repense=""
        while repense not in liste:
            repense=input("quel niveau de dificulté vous souhaité parmis {}".format(liste))
        self.deficulte=repense

    
    def jouer():
        try:
            nombre=int(input("entrez la serie du nombre afficher a l'écran"))
            return nombre
        except:
            "print vous avez tapez autre chose q'un nombre entier"