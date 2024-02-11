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

# TODO: Ecrire le code en python et afficher le contenu des variables

A = 12
B = 13
C = 3
print ("A est définit comme",A,"\nB est définit comme",B,"\nC est deffinit comme",C)
B = A
print ("si B=A alors B devient:",B)
C = B
print ("si C=B alors C devient",C)
A = C
print ("et si A=C alors A devient", A,"\nPS: J'ai fait l'exercice avec A, B et C de valeurs respectives 12, 13, 3 et j'en ai compris le concept")
