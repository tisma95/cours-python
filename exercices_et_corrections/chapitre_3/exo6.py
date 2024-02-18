#################################################################
#               Author: Ismael Maurice                          #
#               Language: Python                                #
#               Chapter 3                                       #
#               File: exo6.py                                   #
#################################################################

"""
    Objectifs: Reprendre le programme de l’exercice 5 mais cette fois-ci donner une indication sur l’erreur de l’utilisateur
    comme « Nom d’utilisateur incorrect ! » ou « Mot de passe incorrect ! » ou « Nom d’utilisateur et mot de
    passe incorrects ! ».
"""

# Saisie des secrets => pour éviter de modifier dans le code les valeurs
secretUtilisateur = "Christophe"
secretMotDePasse = "chris1234"

# Demander à l'utilisateur son nom d'utilisateur et son mot de passe
nomUtilisateur = input("Entrer votre nom d'utilisateur:")
motDePasse = input("Entrer votre mot de passe:")
print("Vous avez saisi comme nom d'utilisateur:", nomUtilisateur)
print("Vous avez saisi comme mot de passe:", motDePasse)

# Méthode 1: sans imbrication
if nomUtilisateur == secretUtilisateur and motDePasse == secretMotDePasse:
    print("Bienvenue", secretUtilisateur)
elif nomUtilisateur != secretUtilisateur and motDePasse != secretMotDePasse:
    print("Nom d’utilisateur et mot de passe incorrects")
elif nomUtilisateur != secretUtilisateur:
    print("Nom d’utilisateur incorrect")
else:
    print("Mot de passe incorrect")

# Méthode 2: avec imbrication
if nomUtilisateur == secretUtilisateur and motDePasse == secretMotDePasse:
    print("Bienvenue", secretUtilisateur)
else:
    if nomUtilisateur != secretUtilisateur and motDePasse != secretMotDePasse:
        print("Nom d’utilisateur et mot de passe incorrects")
    elif nomUtilisateur != secretUtilisateur:
        print("Nom d’utilisateur incorrect")
    else:
        print("Mot de passe incorrect")

# Méthode 3: avec multiple imbrications
if nomUtilisateur == secretUtilisateur and motDePasse == secretMotDePasse:
    print("Bienvenue", secretUtilisateur)
else:
    if nomUtilisateur != secretUtilisateur and motDePasse != secretMotDePasse:
        print("Nom d’utilisateur et mot de passe incorrects")
    else:
        if nomUtilisateur != secretUtilisateur:
            print("Nom d’utilisateur incorrect")
        else:
            print("Mot de passe incorrect")