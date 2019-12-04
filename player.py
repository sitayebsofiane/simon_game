class Player:
    
    def __init__(self,nom):
        self.score=0 #initialisation du score a zero
        self.nom=nom
    
    def jouer():
        try:
            nombre=int(input("entrez la serie du nombre afficher a l'ecran"))
        except:
            "print vous avez tapez autre chose q'un nombre entier"