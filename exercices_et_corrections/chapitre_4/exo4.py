#################################################################
#               Author: Ismael Maurice                          #
#               Language: Python                                #
#               Chapter 4                                       #
#               File: exo4.py                                   #
#################################################################

"""
    Objectifs: Ecrire un programme qui demande un nombre compris entre 10 et 20, jusqu’à ce que la réponse convienne. En
    cas de réponse supérieure à 20, on fera apparaître un message: « Plus petit ! », et inversement « Plus grand ! » si
    le nombre est inférieur à 10.
"""

# TODO: Ecrire le code en python ci dessous

nbrSaisi = input("veuillez saisir un nombre compris entre 10 et 20:")
nbrSaisi=int(nbrSaisi)
while nbrSaisi < 10 or nbrSaisi > 20:
    if nbrSaisi >20:
        print(f"Plus petit !")
        nbrSaisi = input("veuillez saisir un nombre compris entre 10 et 20:")
        nbrSaisi=int(nbrSaisi)
    elif nbrSaisi <10:
        print(f"Plus grand !")
        nbrSaisi = input("veuillez saisir un nombre compris entre 10 et 20:")
        nbrSaisi=int(nbrSaisi)
print (f"{nbrSaisi} est bien compris entre 10 et 20.")
