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
# Variables paramètres pour adapter le programme pour d'autres types de valeurs
N_MIN = 10
N_MAX = 20
nbrSaisi = N_MIN - 1
# Execution du programme
while nbrSaisi < N_MIN or nbrSaisi > N_MAX:
    nbrSaisi = input(f"Veuillez saisir un nombre compris entre {N_MIN} et {N_MAX}:")
    nbrSaisi = int(nbrSaisi)
    if nbrSaisi > N_MAX:
        print(f"Plus petit !")
    elif nbrSaisi < N_MIN:
        print(f"Plus grand !")
print (f"{nbrSaisi} est bien compris entre {N_MIN} et {N_MAX}.")
