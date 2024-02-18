#################################################################
#               Author: Ismael Maurice                          #
#               Language: Python                                #
#               Chapter 3                                       #
#               File: exo5.py                                   #
#################################################################

"""
    Objectifs: Soit un utilisateur dont le nom d’utilisateur est « Christophe » et son mot de passe « chris1234 ».
    Ecrire un programme qui demande à l’utilisateur son nom d’utilisateur et son mot de passe, le programme
    doit afficher « Nom d’utilisateur et/ou mot de passe incorrect(s) » si l’une des deux valeurs est incorrecte
    sinon afficher « Bienvenue Christophe ! ».
"""

# Saisie des secrets => pour éviter de modifier dans le code les valeurs
secretUtilisateur = "Christophe"
secretMotDePasse = "chris1234"

# Demander à l'utilisateur son nom d'utilisateur et son mot de passe
nomUtilisateur = input("Entrer votre nom d'utilisateur:")
motDePasse = input("Entrer votre mot de passe:")
print("Vous avez saisi comme nom d'utilisateur:", nomUtilisateur)
print("Vous avez saisi comme mot de passe:", motDePasse)

if nomUtilisateur == secretUtilisateur and motDePasse == secretMotDePasse:
    print("Bienvenue", secretUtilisateur)
else:
    print("Nom d’utilisateur et/ou mot de passe incorrect(s)")