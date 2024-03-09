#################################################################
#               Author: Ismael Maurice                          #
#               Language: Python                                #
#               Chapter 3                                       #
#               File: exo2.py                                   #
#################################################################

"""
    Objectifs: Ecrire un programme qui demande un nombre à l’utilisateur, et l’informe ensuite si ce nombre est positif ou
    négatif. On prendra en compte le cas où le nombre est nul.
"""

# TODO: Ecrire le code en python ci dessous

saisie=input ("Veuillez entrer un nombre au hazard\n---> ")
nbre=int(saisie)

if nbre > 0: 
    print (nbre,"est POSITIF" )
elif nbre < 0:
    print (nbre,"est NEGATIF" )
elif nbre == 0:
    print ("ZERO est NUL")

