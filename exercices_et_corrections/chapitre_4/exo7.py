#################################################################
#               Author: Ismael Maurice                          #
#               Language: Python                                #
#               Chapter 4                                       #
#               File: exo7.py                                   #
#################################################################

"""
    Objectifs: Ecrire un algorithme qui demande un nombre à l’utilisateur et qui ensuite écrit la table de multiplication de ce
    nombre de 0 à 10.
"""

# TODO: Ecrire le code en python ci dessous

tableMultiplication = input(f"Quelle table de multiplication ?")
tableMultiplication = int(tableMultiplication)
for multiplicateur in range(0,11):
    multiplicateur = int(multiplicateur)
    print(f"{multiplicateur} X {tableMultiplication} = {multiplicateur*tableMultiplication}")
