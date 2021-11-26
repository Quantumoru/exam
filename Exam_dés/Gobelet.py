### Création de la classe Gobelet (représentant un gobelet avec des dés dedans)
# import Dé pour récupérer les méthodes
from Dé import De


class Gobelet:
    def __init__(self, nb_des):
        self.nb_des = nb_des
        self._val_gob = 0
        # créé une lsite et ajoute du nombre de dés à ma liste
        self.des = []
        self.ajoutliste()
        
    # Ajoute un nombre de dés à ma liste
    def ajoutliste(self):
        for i in range(self.nb_des):
            (self.des).append(i)
        
    @property
    def nb_des(self):
        return self._nb_des

    @nb_des.setter
    def nb_des(self, nb_des):
        self._nb_des = nb_des
        
    @property
    def val_gob(self):
        return self._val_gob
    
    @val_gob.setter
    def val_gob(self, val_gob):
        self._val_gob = val_gob
        
    # récupération de la valeur d'un gobelet
    def GetValeur(self):
        return self._val_gob
    
    # lancement d'un gobelet (avec un certains nombres de dés)
    def lancer(self):
        for i in range(self.nb_des):
            a = De().lancer()
            print(a)
            self.val_gob = self.val_gob + a
        self.AfficherScore()
        return self.GetValeur()
        
    #Affichage du score total du lancer
    def AfficherScore(self):
        print(f"Le score de ce lancer est de {self.val_gob}")
    
#gob = Gobelet(3).lancer()