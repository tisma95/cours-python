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

# Demander à l'utilisateur le premier nombre
nbre1 = input("Veuillez entrer le nombre 1:")
# Convertion de la saisie de l'utilisateur qui est du type string alors qu'on a besoin du type int
nbre1 = int(nbre1)
print("Vous avez saisi le nombre 1:", nbre1)
# Demander à l'utilisateur le deuxième nombre
nbre2 = input("Veuillez entrer le nombre 2:")
# Convertion de la saisie de l'utilisateur qui est du type string alors qu'on a besoin du type int
nbre2 = int(nbre2)
print("Vous avez saisi le nombre 2:", nbre2)
# Calcul du résultat de la multiplication de nbre1 par nbre2
produit = nbre1 * nbre2
print(f"Le résultat de {nbre1} x {nbre2} donne: {produit}")
# Analyse du signe du produit
if produit < 0:
    print(f"Le produit de {nbre1} par {nbre2} est négatif")
elif produit > 0:
    print(f"Le produit de {nbre1} par {nbre2} est positif")
else:
    print(f"Le produit de {nbre1} par {nbre2} est nul")