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

tableMultiplication = input("Entrer le nombre dont vous voulez afficher la table de multiplication:")
tableMultiplication = int(tableMultiplication)
N_END = 10
N_START = 0
for multiplicateur in range(N_START, N_END + 1):
    print(f"{multiplicateur} x {tableMultiplication} = {multiplicateur*tableMultiplication}")
