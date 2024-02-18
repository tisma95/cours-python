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

# Demander un nombre à l'utilisateur
nbre = input("Entrer un nombre svp:")
nbre = int(nbre)
print("Vous avez saisi le nombre:", nbre)
# Vérifions le signe du nombre
if nbre < 0:
    print(f"Le nombre {nbre} est un nombre négatif.")
elif nbre > 0:
    print(f"Le nombre {nbre} est un nombre positif.")
else:
    print(f"Le nombre {nbre} est un nombre nul.")