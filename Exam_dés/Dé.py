###Création de la classe Dé

#importation de random pour génération d'une valeur pour un lancer de dé
import random

class De:
    def __init__(self):
        self.valeurd = 0
    
    #definition du setter / getter
    @property
    def valeurd(self):
        return self._valeurd
    
    @valeurd.setter
    def valeurd(self, valeurd):
        self._valeurd = valeurd
    
    # récupération de la valeur d'un dé
    def GetValeur(self):
            return self._valeurd
    
    # lancement d'un dé
    def lancer(self):
        self._valeurd = random.randint(1, 6)
        return self.GetValeur()
        
        
# de=De()
# print(de.lancer())