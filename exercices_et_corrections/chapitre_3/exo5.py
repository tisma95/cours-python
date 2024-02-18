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

# TODO: Ecrire le code en python ci dessous

username = input ("Votre nom d'utilisateur ?")

passwd = input ("Votre mot de passe :")


if username == "Christophe" and passwd == "chris1234":
    print ("\nBienvenue",username)
else:
    print ("\nNom d’utilisateur et/ou mot de passe incorrect(s)\n" )