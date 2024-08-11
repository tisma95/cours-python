#################################################################
#               Author: Ismael Maurice                          #
#               Language: Python                                #
#               Chapter 4                                       #
#               File: exo8.py                                   #
#################################################################

"""
    Objectifs:Ecrire un algorithme qui demande un nombre à l’utilisateur et qui calcule le factoriel de ce nombre. Par
    exemple si l’utilisateur saisit 8, le factoriel de 8 noté 8! vaut: 8 x 7 x 6 x 5 x 4 x 3 x 2 x 1 = 40320. Pour 3 on
    aura 3! = 3 x 2 x 1 = 6. Sachant aussi que 1! = 1 et 0! = 1.
"""

# Version 1
nbreSaisi = input("Entrer un nombre:")
nbreSaisi = int(nbreSaisi)
if nbreSaisi < 0:
    print("Il est impossible de calculer le factoriel d'un nombre négatif.")
elif nbreSaisi == 0 or nbreSaisi == 1:
    print(f"Le factoriel de {nbreSaisi} est: 1")
else:
    factoriel = 1
    for nbreCompteur in range(1, nbreSaisi+1):
        factoriel = factoriel * nbreCompteur
    print(f"le factoriel de {nbreSaisi} est: {factoriel}")


# Version 2
nbreSaisi = input("Entrer un nombre:")
nbreSaisi = int(nbreSaisi)
factoriel = 1
if nbreSaisi < 0:
    print("Il est impossible de calculer le factoriel d'un nombre négatif.")
    exit(0)
elif nbreSaisi == 0 or nbreSaisi == 1:
    pass
else:
    for nbreCompteur in range(1, nbreSaisi+1):
        factoriel = factoriel * nbreCompteur
print(f"Le factoriel de {nbreSaisi} est: {factoriel}")