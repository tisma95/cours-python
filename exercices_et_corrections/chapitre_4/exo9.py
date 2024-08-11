#################################################################
#               Author: Ismael Maurice                          #
#               Language: Python                                #
#               Chapter 4                                       #
#               File: exo9.py                                   #
#################################################################

"""
    Objectifs: Soit un utilisateur de nom d’utilisateur Christophe et mot de passe chris1234. Ecrire un programme qui va
    demander le nom d’utilisateur et le mot de passe tant que le nom d’utilisateur et mot de passe sont incorrects.
    Sinon Afficher « Bienvenue Christophe ».
"""

nomUtilisateur = "Christophe"
motDePasse = "chris1234"
saisieUtilisateur = ''
saisieMotDePasse = ''
while saisieUtilisateur != nomUtilisateur or saisieMotDePasse != motDePasse:
    saisieUtilisateur = input("Votre identifiant:")
    saisieMotDePasse = input("Mot de passe:")
    if saisieUtilisateur != nomUtilisateur or saisieMotDePasse != motDePasse:
        print("\nNom d'utilisateur ou mot de passe Incorrect\n")
print("\nBienvenue " + nomUtilisateur)
