class Perso:
    
    def __init__(self, ici):
        """ici : un tuple (x, y) représentant un point dans l'espace"""
        self.pos = ici

class Joueur(Perso):
    
    def __init__(self, ici, name):
        Perso.__init__(self, ici)
        self.nom = name
        self.vie = 100
        self.vitesse = 1
        self.force = 5
        self.memoire = 30
        self.charisme = 0
        #self.inventaire = Bag()

class Marchand(Perso):
    
    def __init__(self, ici, name):
        Perso.__init__(self, ici)
        self.nom = name
        self.inventaire = Bag()
        
class Monstre(Perso):
    
    def __init__(self, ici, pv, speed, strength, view):
        Perso.__init__(self, ici)
        self.vie = pv
        self.vitesse = speed
        self.force = strength
        self.vision = view
        self.inventaire = Bag()

