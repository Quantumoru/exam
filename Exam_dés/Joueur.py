### Création de la classe Joueur

from Gobelet import Gobelet



class Joueur():
    def __init__(self, nom, score=0):
        self.nom = nom
        self.score = score
        
    @property
    def nom(self):
        return self._nom

    @nom.setter
    def nom(self, nom):
        self._nom = nom
        
    @property
    def score(self):
        return self._score
    
    @score.setter
    def score(self, score):
        self._score = score
    
    
    def jouer(self):
        gobelet= Gobelet(3)
        gobelet.lancer()
        self.score = self.score + gobelet.GetValeur()
        self.AfficherScore()
        
    def AfficherScore(self):
        print(f"Le score de {self.nom} est de {self.score}")
        
#joueur = Joueur("Jean")
#joueur.jouer()


        