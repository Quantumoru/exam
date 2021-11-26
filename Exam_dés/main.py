### Script du lancement du jeu

from Partie import Partie

def jeu(): 
        print("Bienvenue dans ce jeu de dés (un genre de cul de chouette)")
        a = int(input("Combien de joueur êtes-vous ?\n"))
        b = int(input("Combien de tour voulez-vous faire ?\n"))
        c = int(input("Combien de dés voulez-vous dans votre gobelet?\n"))
        partie = Partie(a,b,c)
        partie.lancer()
#         rejoue()
        
# def rejoue():
#     jouer = True
#     while jouer == True:
#         rejoue = str(input("Voulez-vous rejouer ? Y or N \n"))
#         if rejoue not in  ("Oui", "oui", "O", "o", "Y", "y", "Yes", "yes"):
#             jouer = False
#             return jouer        
#         else :
#             jouer = True
#             return jouer
jeu()