#################################################################
#               Author: Ismael Maurice                          #
#               Language: Python                                #
#               Chapter 3                                       #
#               File: exo3.py                                   #
#################################################################

"""
    Objectifs: Ecrire un programme qui demande deux nombres à l’utilisateur et l’informe ensuite si leur produit est négatif
    ou positif ou nul.
"""

# TODO: Ecrire le code en python ci dessous

saisie1=input ("Nombre 1\n---> ")
saisie2=input ("Nombre 2\n---> ")
nbre1=float(saisie1)
nbre2=float(saisie2)
produit=nbre1*nbre2
print ("Le produit de",saisie1,"X",saisie2,"=",produit,"\n") 


if produit > 0: 
    print (produit,"est un produit POSITIF\n" )
elif produit < 0:
    print (produit,"est un produit NEGATIF\n" )
elif produit == 0:
    print ("MULTIPLIER PAR ZERO N'A PAS DE SENS !\n")

