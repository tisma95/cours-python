#################################################################
#               Author: Ismael Maurice                          #
#               Language: Python                                #
#               Chapter 4                                       #
#               File: exo1.py                                   #
#################################################################

"""
    Objectifs: Sachant que chaine[n] permet de renvoyer le n-ième caractère de la chaine par exemple chaine[0] renverra le
    premier caractère de chaine pour nom="Toto", nom[0] est T et nom[3] le dernier « o ».
    Sachant aussi que len(chaine) renvoie la taille d’une chaine exemple len(nom) renverra 4 si nom="Toto".
    Ecrire un programe avec la boucle while qui affiche la liste des caractères d'une chaine.
"""
# L'utilisateur fournit son nom
nom = input("Entrer votre nom:")
# Calcul du nombre de caractères
totalCaracteres = len(nom)
index = 0
print(f"\n{nom} contient {totalCaracteres} caractères qui sont:\n")
while index < totalCaracteres:
    print(nom[index])
    index = index + 1