#################################################################
#               Author: Ismael Maurice                          #
#               Language: Python                                #
#               Chapter 2                                       #
#               File: exo7.py                                   #
#################################################################

"""
    Objectifs: Soit trois variables A, B et C de valeurs respectives 12, 13, 3.
    Ecrire un algorithme qui transfère à B la valeur de A, à C la valeur de B et à A la valeur de C.
    Tester l’algorithme avec différentes valeurs de A, B, et C.
"""

# Résultat attendu A = 3, B = 12, C =13
print ("Méthode 1")
A = 12
B = 13
C = 3
# Méthode 1
print(f"Avant A={A}, B={B}, C={C}")
tmp = A
A = C
C = B
B = tmp
print(f"Après A={A}, B={B}, C={C}")

# Méthode 2
print ("\nMéthode 2 (Python) => A, B = B, A")
A = 12
B = 13
C = 3
print(f"Avant A={A}, B={B}, C={C}")
A, B, C = C, A, B
print(f"Après A={A}, B={B}, C={C}")