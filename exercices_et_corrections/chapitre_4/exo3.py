#################################################################
#               Author: Ismael Maurice                          #
#               Language: Python                                #
#               Chapter 4                                       #
#               File: exo3.py                                   #
#################################################################

"""
    Objectifs: Ecrire un programme qui demande à l’utilisateur un nombre compris entre 1 et 3 jusqu’à ce que la réponse
    convienne.
"""

# TODO: Ecrire le code en python ci dessous
import random
nbMystere = random.randint(1,3)
compteurChance = 1
print (f"{nbMystere} choisi par RANDOM pour verif") 
entree = input ("Quel est le nombre mystère entre 1 et 3? ")
while entree != nbMystere:
    compteurChance = compteurChance +1
    entree = input (f"Pour une {compteurChance}ème chance, quel est le nombre mystère ? ")
print (f"Coup de chance! c'est bien {nbMystere} ...")

