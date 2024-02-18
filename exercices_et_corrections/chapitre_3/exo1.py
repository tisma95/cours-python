#################################################################
#               Author: Ismael Maurice                          #
#               Language: Python                                #
#               Chapter 3                                       #
#               File: exo1.py                                   #
#################################################################

"""
    Objectifs: Réécrire le programme suivant en utilisant les opérateurs logiques.

    username = "Christophe"
    if username == "Christophe":
        print("Bienvenue")
    elif username == "John":
        print("Bienvenue")
    else:
        print("Utilisateur inconnu")
"""

username = "Christophes"
if username == "Christophe" or username == "John":
    print("Bienvenue")
else:
    print("Utilisateur inconnu")
