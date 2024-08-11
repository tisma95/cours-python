#################################################################
#               Author: Ismael Maurice                          #
#               Language: Python                                #
#               Chapter 4                                       #
#               File: exo10.py                                  #
#################################################################

"""
    Objectifs: Faire une variance du programme 9 mais cette fois-ci demander le nom d’utilisateur tant que la saisie n’est pas
    correcte ensuite si correcte demander le mot de passe si la saisie est correcte afficher le message de bienvenue.
"""

# TODO: Ecrire le code en python ci dessous

utilisateur = "Christophe"
motDePasse = "chris1234"
saisieUtilisateur = input("Votre identifiant: ")
while saisieUtilisateur != utilisateur:
    saisieUtilisateur = input("\nVotre identifiant: ")
saisieMotDePasse = input("Mot de passe: ")
while saisieMotDePasse != motDePasse:
    saisieMotDePasse = input("Mot de passe: ")
print("\nBienvenue "+utilisateur)
