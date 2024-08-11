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


nomUtilisateur = "Christophe"
motDePasse = "chris1234"
saisieUtilisateur = ''
saisieMotDePasse = ''
while saisieUtilisateur != nomUtilisateur:
    saisieUtilisateur = input("Votre identifiant:")
    if saisieUtilisateur != nomUtilisateur:
        print("Nom d'utilisateur incorrect")
while saisieMotDePasse != motDePasse:
    saisieMotDePasse = input("Mot de passe:")
    if saisieMotDePasse != motDePasse:
        print(f"Mote de passe de {nomUtilisateur} incorrect")
print("\nBienvenue " + nomUtilisateur)
