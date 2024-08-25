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

# TODO: Ecrire le code en python ci dessous

#Methode chapitre 4
print("\nMethode TOF seul:")
phraseMot = input("Entrez votre phrase ou votre mot: ")
totalCaracteres = len(phraseMot)
index = 0
while index < totalCaracteres:
    caractereActuel = phraseMot[index]
    if index == 0:
        print(caractereActuel.upper(),end="")
    else:
        print(caractereActuel.lower(),end="")
    index = index + 1

#Methode chapitre 4 TEST TOF
print("\n\nMethode TEST TOF:") # \n\n pour sauter une ligne du fait que le programme TOF seul ai un end=""
phraseMot = input("Entrez votre phrase ou votre mot en mélangeant MAJUSCULES et minuscules:\n-> ")
totalCaracteres = len(phraseMot)
index = 0
print("\nUne phrase commence par une majuscule et fini par un point.\nVoici votre phrase corrigée:\n-> ",end="")
while index < totalCaracteres:
    caractereActuel = phraseMot[index]
    if index == 0:
        print(caractereActuel.upper(),end="")
    else:
        print(caractereActuel.lower(),end="")
    index = index + 1
print(".")

#Methode avec l'aide du chapitre 8 
print("\nMethode chapitre 8: (Les méthodes de bases de la classe str)")
saisieUtilisateur = input("Veuillez entrer une phrase ou un mot:")
saisieUtilisateur = saisieUtilisateur.capitalize()
print(saisieUtilisateur,end=".")