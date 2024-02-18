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

# TODO: Ecrire le code en python ci dessous

username = input ("Votre nom d'utilisateur ?")

passwd = input ("Votre mot de passe :")


if username == "Christophe" and passwd == "chris1234":
    print ("\nBienvenue",username,"\n")
elif username != "Christophe":
    print ("\nNom d’utilisateur incorrect\n" )
elif passwd != "chris1234":
    print ("\nMot de passe Incorrect\n" )
