#################################################################
#               Author: Ismael Maurice                          #
#               Language: Python                                #
#               Chapter 4                                       #
#               File: exo5.py                                   #
#################################################################

"""
    Objectifs: Ecrire un programme qui demande un nombre de départ à l’utilisateur et qui affiche les dix nombres suivants.
    Par exemple, si l’utilisateur entre le nombre 17, le programme affichera les nombres de 18 à 27.
"""
nbreDeDepart = input("Veuillez entrer un nombre de départ pour en afficher les dix nombres suivants: ")
nbreDeDepart = int(nbreDeDepart)
# Méthode 1: Affiche les nombres l'un à la suite de l'autre
print(f"\nMéthode 1: Les dix nombres suivant {nbreDeDepart} l'un à la suite de l'autre sont:")
for nbreSuivant in range(nbreDeDepart + 1, nbreDeDepart + 11):
    print(nbreSuivant)

# Méthode 2: Affiche les nombres sur la même ligne utiliser end
print(f"\nMéthode 2: Les dix nombres suivant {nbreDeDepart} sur une seule ligne sont:")
for nbreSuivant in range(nbreDeDepart + 1, nbreDeDepart + 11):
    print(nbreSuivant, end=" | ")