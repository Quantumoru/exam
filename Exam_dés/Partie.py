### Création de la classe Partie

from Gobelet import Gobelet
from Joueur import Joueur
#from Gobelet import Gobelet

class Partie:
    def __init__(self, nb_j, nb_tour, nb_des):
        self.joueurs = []
        self.nb_j = nb_j
        self.nb_tour = nb_tour
        self.nb_des = nb_des
        self.ajoutjoueurs()
        self.obj_joueurs = []
        
    @property
    def nb_j(self):
        return self._nb_j
    
    @nb_j.setter
    def nb_j(self, nb_j):
        self._nb_j = nb_j
        
    @property
    def nb_tour(self):
        return self._nb_tour
    
    @nb_tour.setter
    def nb_tour(self, nb_tour):
        self._nb_tour = nb_tour
        
    @property
    def nb_des(self):
        return self._nb_des

    @nb_des.setter
    def nb_des(self, nb_des):
        self._nb_des = nb_des
    
    #ajout des noms des joueurs (en fonction de l'entrée du nombre de joueurs)  dans une liste  
    def ajoutjoueurs(self):
        for i in range(self.nb_j):
            name = input("nom du joueur : ")
            (self.joueurs).append(name)
        
    #Initialise les différents joueurs (de classe joueur) dans une liste
    def Initialiser(self):
        for nom in self.joueurs:
            self.obj_joueurs.append(Joueur(nom))
    
    #jouer le jeu
    def lancer(self):
        self.Initialiser()
        i=0
        #Boucle pour permettre de prendre en compte le nombre de tour
        while i < self.nb_tour:
            #Boucle pour faire jouer les différents joueurs
            for obj in self.obj_joueurs :
                gobelet = Gobelet(self.nb_des)
                a = obj.score
                obj.jouer(gobelet)
                a = a + obj.score
            i = i + 1
        else:
            self.afficherGagnant()
    
    #Vérification de la position des joueurs et affichage du joueur    
    def afficherGagnant(self):
        result = []
        for b in range(0,len(self.obj_joueurs)):
            result.append((self.obj_joueurs[b].score,self.obj_joueurs[b].nom))
        result.sort(reverse=True)
        #En cas d'égalité des 2 premiers joueurs
        if (result[0][0]) == (result[1][0]):
            print("Egalité!")
        else:
            print(f"Le gagnant est : {result[0][1]} avec {result[0][0]} points. \nBravo!")
            


