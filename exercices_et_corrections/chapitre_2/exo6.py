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

# TODO: Ecrire le code en python et afficher le contenu des variables


print ("Que contient A ?")
A=input()
print ("Ok dans A ",A,"\nEt maintenant que contient B ?")
B=input()
#A="Premier"
#B="Deuxième"
print ("A contient:",A,"et B contient:",B,"Avant inversion des valeurs")
TMP=A
A=B
B=TMP
print ("Après inversion des valeurs A contient maintenant",A,"et B",B)