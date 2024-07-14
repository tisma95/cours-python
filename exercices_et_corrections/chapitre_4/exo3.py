#################################################################
#               Author: Ismael Maurice                          #
#               Language: Python                                #
#               Chapter 4                                       #
#               File: exo3.py                                   #
#################################################################

"""
    Objectifs: Ecrire un programme qui demande à l’utilisateur un nombre compris entre 1 et 3 jusqu’à ce que la réponse
    convienne.
"""

# TODO: Ecrire le code en python ci dessous
nbrSaisi = input ("Entrer un nombre entre 1 et 3")
nbrSaisi = int(nbrSaisi)
while nbrSaisi < 1 or nbrSaisi >3 :
    print ("essaye encore")
    nbrSaisi = input ("Entrer un nombre entre 1 et 3")
    nbrSaisi = int(nbrSaisi)
print (f"{nbrSaisi} est bien compris entre 1 et 3")