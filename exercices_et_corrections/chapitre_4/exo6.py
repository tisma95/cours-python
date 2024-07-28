#################################################################
#               Author: Ismael Maurice                          #
#               Language: Python                                #
#               Chapter 4                                       #
#               File: exo6.py                                   #
#################################################################

"""
    Objectifs: Ecrire un programme qui demande un nombre de départ à l’utilisateur et qui calcule la somme des entiers jusqu’à
    ce nombre (inclus). Par exemple, si l’utilisateur entre 5, le programme doit calculer 1 + 2 + 3 + 4 + 5 = 15
"""

nbreSaisi = input("Entrer un nombre:")
nbreSaisi = int(nbreSaisi)

# Affichage du total uniquement
total = 0
for nbreCompteur in range(1, nbreSaisi+1):
    total = total + nbreCompteur
print(f"La somme des nombres de 1 à {nbreSaisi} est: {total}")
