### Création de la classe Joueur
# import de gobelet pour récuperer les méthodes
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
    
    # méthode qui permet de jouer (en lancant un gobelet avec un certain nombre de dés ici 3)
    def jouer(self, gobelet : Gobelet):
        gobelet.lancer()
        self.score = self.score + gobelet.GetValeur()
        self.AfficherScore()
    
    #Affiche le score du joueur avec son nom    
    def AfficherScore(self):
        print(f"Le score de {self.nom} est de {self.score}")
        
# joueur = Joueur("Jean")
# joueur.jouer()


        