#################################################################
#               Author: Ismael Maurice                          #
#               Language: Python                                #
#               Chapter 4                                       #
#               File: exo5.py                                   #
#################################################################

"""
    Objectifs: Ecrire un programme qui demande un nombre de départ à l’utilisateur et qui affiche les dix nombres suivants.
    Par exemple, si l’utilisateur entre le nombre 17, le programme affichera les nombres de 18 à 27.
"""

# TODO: Ecrire le code en python ci dessous

depart = input("Veuillez entrer un nombre de départ pour en afficher les dix nombres suivants: ")
depart = int(depart)
for nbSuivants in range(depart+1,depart+11):
    print(nbSuivants)


