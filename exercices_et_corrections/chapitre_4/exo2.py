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

# L'utilisateur fournit son nom
nom = input("Entrer votre nom:")
# Calcul du nombre de caractères
totalCaracteres = len(nom)
index = 0
totalConsonne = 0
totalVoyelle = 0
print(f"\nLe nom {nom} contient les lettres suivantes:\n")
while index < totalCaracteres:
    caractereActuel = nom[index]
    if caractereActuel in "AEIOUYaeiouy":
        print(f"La voyelle: {caractereActuel}")
        totalVoyelle += 1 #=> Equivalent à totalVoyelle = totalVoyelle + 1
    else:
        print(f"La consonne: {caractereActuel}")
        totalConsonne += 1 #=> Equivalent à totalConsonne = totalConsonne + 1
    index = index + 1
print(f"\n'{nom}' contient donc {totalVoyelle} voyelle(s) et {totalConsonne} consonne(s) pour un total de {totalCaracteres} lettres.\n")
