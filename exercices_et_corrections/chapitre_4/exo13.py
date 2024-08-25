#################################################################
#               Author: Ismael Maurice                          #
#               Language: Python                                #
#               Chapter 4                                       #
#               File: exo13.py                                  #
#################################################################

"""
    Objectifs:Ecrire un programme qui demande successivement 20 nombres à l’utilisateur, et qui lui dise ensuite quel était le
    plus grand parmi ces 20 nombres par exemple:
    Entrer le nombre numéro 1: 16
    …
    Entrer le nombre numéro 20: 12
    Le plus grand de ces nombres est 16.
"""

# Définition des variables
S_MAX = 20
maxNombre = None

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
    # # Méthode rapide
    # if maxNombre == None or saisieUtilisateur > maxNombre:
    #     maxNombre = saisieUtilisateur
print(f"\nLe plus grand de ces nombres est {maxNombre}.\n")