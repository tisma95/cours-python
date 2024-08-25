#################################################################
#               Author: Ismael Maurice                          #
#               Language: Python                                #
#               Chapter 4                                       #
#               File: exo14.py                                  #
#################################################################

"""
    Objectifs: Reprendre l’algorithme de l’exercice 13 mais cette fois-ci il faut afficher la position à laquelle le nombre a été
    saisi.
    Par exemple: le plus grand de ces nombres est 15 et c’est le nombre 2 saisi
"""

# TODO: Ecrire le code en python ci dessous

# Définition des variables
S_MAX = 10
maxNombre = None
positionNbre = 1

# Démarrage du programme
print("+++++++++++++ SAISIE DES 20 NOMBRES +++++++++++++++++++\n")
for ind in range(S_MAX):
    saisieUtilisateur = input(f"Entrer le nombre numéro {ind + 1}:")
        # On suppose que l'utilisateur a entré un nombre
    saisieUtilisateur = int(saisieUtilisateur)
    # Mise à jour de la valeur de max
    if maxNombre == None:
        print(f"Initialisation de la valeur max à {saisieUtilisateur}.")
        maxNombre = saisieUtilisateur
    elif saisieUtilisateur > maxNombre:
        print(f"Changement de la valeur max qui passe de {maxNombre} à {saisieUtilisateur}")
        maxNombre = saisieUtilisateur
        positionNbre = positionNbre + 1
     # # Méthode rapide
    # if maxNombre == None or saisieUtilisateur > maxNombre:
    #     maxNombre = saisieUtilisateur
print(f"\nLe plus grand de ces nombres est {maxNombre} et c'est le nombre {positionNbre} saisi.\n")