#################################################################
#               Author: Ismael Maurice                          #
#               Language: Python                                #
#               Chapter 4                                       #
#               File: exo12.py                                  #
#################################################################

"""
    Objectifs: Ecrire un programme qui demande une phrase ou mot à l’utilisateur et ensuite affichera la saisie de l’utilisateur
    en capitalisation avec en lettre majuscule le premier caractère et tout le reste en lettre minuscule.
    Exemple l’utilisateur entre « TOTO » ou « toTO » le programme doit afficher « Toto ».
"""

# Méthode avec la boucle While
print("\nMéthode utilisant la boucle while:\n")
phraseMot = input("Entrez une phrase ou une mot: ")
totalCaracteres = len(phraseMot)
index = 0
while index < totalCaracteres:
    caractereActuel = phraseMot[index]
    if index == 0:
        print(caractereActuel.upper(), end="")
    else:
        print(caractereActuel.lower(), end="")
    index = index + 1

# Méthode avec la boucle For
print("\n\nMéthode utilisant la boucle For:\n")
phraseMot = input("Entrez une phrase ou une mot: ")
for index, lettre in enumerate(phraseMot):
    if index == 0:
        print(lettre.upper(), end="")
    else:
        print(lettre.lower(), end="")

# Méthode avec l'aide du chapitre 8
print("\n\nMéthode utilisant les fonctions de la classe str:\n")
saisieUtilisateur = input("Veuillez entrer une phrase ou un mot:")
saisieUtilisateur = saisieUtilisateur.capitalize()
print(saisieUtilisateur)