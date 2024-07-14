#################################################################
#               Author: Ismael Maurice                          #
#               Language: Python                                #
#               Chapter 4                                       #
#               File: exo2.py                                   #
#################################################################

"""
    Objectifs: Voir enoncé pdf.

Exercice 2
Sachant que chaine[n] permet de renvoyer le n-ième caractère de la chaine par exemple chaine[0] renverra le
premier caractère de chaine pour nom="Toto", nom[0] est T et nom[3] le dernier « o ».
Sachant aussi que len(chaine) renvoie la taille d’une chaine exemple len(nom) renverra 4 si nom="Toto".
Ecrire un programme python équivalent à celui-ci en utilisant cette fois-ci la boucle while.
"""

# TODO: Ecrire le code en python ci dessousname= "christophe"
name= input(f"\nQuel est votre prénom ?\n")
nbCar = len(name)
index= 0
indexV= 0
indexC= 0
print(f"\nle nom '{name}' contient les {nbCar} lettres suivantes\n")
while index < nbCar:
    for letter in name:
        #Verif voyelle ou non
        if letter in "AEIOUYaeiouy":
            print(f"{letter} est une VOYELLE")
            index=index+1
            indexV=indexV+1
        else:
            print(f"{letter} est une CONSONNE")
            index=index+1
            indexC=indexC+1
print(f"\n'{name}' contient donc {indexV} VOYELLES et {indexC} CONSONNES pour un total de {nbCar} lettres.\n")




