#################################################################
#               Author: Ismael Maurice                          #
#               Language: Python                                #
#               Chapter 4                                       #
#               File: exo15.py                                  #
#################################################################

"""
    Objectifs: Reprendre l’exercice 14 mais cette fois-ci demander à l’utilisateur la quantité de nombres qu’il veut saisir et
    ensuite exécuter le programme en fonction de la quantité de nombres que l’utilisateur veut saisir. Attention aux
    fausses saisies sur la quantité par exemple s’il saisit un nombre négatif ou 0 afficher une erreur et redemander
    combien de nombres il veut saisir.
"""

# TODO: Ecrire le code en python ci dessous

# Définition des variables + choix du nombre d'entrées par l utilisateur
S_MAX = input("\nVeuillez choisir la quantité de nombres à saisir: ")
S_MAX = int(S_MAX)
if S_MAX <=0:
    print("Saisie Incorecte")
else:
    maxNombre = None
    positionNbre = 1
    # Démarrage du programme
    print(f"+++++++++++++ SAISIE DES {S_MAX} NOMBRES +++++++++++++++++++\n")
    for ind in range(S_MAX):
        saisieUtilisateur = input(f"Entrer le nombre numéro {ind + 1}: ")
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