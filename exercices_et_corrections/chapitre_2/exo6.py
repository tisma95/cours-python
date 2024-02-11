#################################################################
#               Author: Ismael Maurice                          #
#               Language: Python                                #
#               Chapter 2                                       #
#               File: exo6.py                                   #
#################################################################

"""
    Objectifs: Ecrire un algorithme permettant d’échanger les valeurs de deux variables A et B, et ce quelque soit
    leur contenu préalable.
"""

# Méthode 1
print ("Méthode 1")
print ("Que contient A ?")
A = input()
print ("Ok dans A ", A, "\nEt maintenant que contient B ?")
B = input()
print ("A contient:", A, "et B contient:", B, "Avant inversion des valeurs")
TMP = A
A = B
B = TMP
print ("Après inversion des valeurs A contient maintenant", A, "et B", B)

# Méthode 2 (Python)
print ("\nMéthode 2 (Python) => A, B = B, A")
print ("Que contient A ?")
A = input()
print ("Ok dans A ", A, "\nEt maintenant que contient B ?")
B = input()
A, B = B, A
print ("Après inversion des valeurs A contient maintenant", A, "et B", B)