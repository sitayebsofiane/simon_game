class Player:
    
    def __init__(self):
        self.score=0 #initialisation du score a zero
        nom=""
        while not (nom.isalpha or len(nom)>2):
            self.nom=input("entrez votre nom")

    
    def jouer():
        try:
            nombre=int(input("entrez la serie du nombre afficher a l'écran"))
        except:
            "print vous avez tapez autre chose q'un nombre entier"