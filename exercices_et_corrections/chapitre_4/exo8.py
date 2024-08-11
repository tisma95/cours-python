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

# TODO: Ecrire le code en python ci dessous

# #-----------------------TOF tout seul sans aide d'internet -------------------------------
# choixUtilisateur = input("Veuillez entrez le nombre dont vous souhaitez connaitre le factoriel \n(Ex: Pour 3 on aura 3! = 3 x 2 x 1 = 6)")
# choixUtilisateur = int(choixUtilisateur)
# # Afficher la multiplication allignées depuis le choixUtilisateur jusqu'a 2 
# for afficherMultiples in range(choixUtilisateur , 0 , -1):
#     if afficherMultiples > 1:
#         print(afficherMultiples, end=" x ")
# # Lorsque la multiplication est arrivée à 1 on remplace " x " par " = " et cela reste aligné 
#     elif afficherMultiples == 1:
#         print(afficherMultiples,end=" = ")
# print("PAS DE BONNES BASES EN MATH TOF !") 

# Avec explications du site https://www.mathweb.fr/euclide/plusieurs-facons-de-calculer-une-factorielle-en-python/ je ne comprends pas tout...

## avec https://www.guru99.com/fr/python-factorial-example.html en exemple mais j'ai besoins d'explications
# print ("Input a number")
# factorialIP = int (input ())
# ffactor23 = 1
# for j in range (1, factorialIP+1):
#    ffactor23 = ffactor23 * j
# print ("The factorial of the number is “, ffactor23)

# #----------------------- FONCTIONNE BIEN EN REPRENANT LE PRINCIPE DU SITE GURU99 -------------------------------
# choixUtilisateur = input("Veuillez entrez le nombre dont vous souhaitez connaitre le factoriel \n(Ex: Pour 3 on aura 3! = 3 x 2 x 1 = 6)\n")
# choixUtilisateur = int(choixUtilisateur)
# multiple = 1
# for resultatMultiple in range (1, choixUtilisateur+1):
#     multiple = multiple * resultatMultiple
# print (f"le facteur de {choixUtilisateur} est {multiple}")

# #----------------------- REVISITÉ POUR AFFICHER LES MULTIPLICATIONS -------------------------------
# choixUtilisateur = input("\nVeuillez entrez le nombre dont vous souhaitez connaitre le factoriel (Ex: Pour 3 on aura 3! = 3 x 2 x 1 = 6)\nVotre choix: ")
# choixUtilisateur = int(choixUtilisateur)
# multiple = 1
# for resultatMultiple in range(1, choixUtilisateur+1):
#     multiple = multiple * resultatMultiple
# # Afficher la multiplication allignées depuis le choixUtilisateur jusqu'a 2 
# for afficherMultiples in range(choixUtilisateur , 0 , -1):
#     if afficherMultiples > 1:
#         print(afficherMultiples, end=" x ")
# # Lorsque la multiplication est arrivée à 1 on remplace " x " par " = " et cela reste aligné 
#     elif afficherMultiples == 1:
#         print (afficherMultiples,end=" = ")
# # On affiche le produit de cette multiplication toujours sur la même ligne 
# print(multiple)
# # On donne le résultat selon la convention mathématique
# print(f"\nle facteur de {choixUtilisateur} s'écrit donc:\n{choixUtilisateur}! = {multiple}\n")

#------------------ Exemple ismael ------------------
nbreSaisi = input("Entrer un nombre:")
nbreSaisi = int(nbreSaisi)
if nbreSaisi < 0:
    print("Il est impossible de calculer le factoriel d'un nombre négatif")
elif nbreSaisi == 0 or nbreSaisi == 1:
    print(f"Le factoriel de {nbreSaisi} sera toujours 1")
else:
    factoriel = 1
    for nbreCompteur in range(1, nbreSaisi+1):
        factoriel = factoriel * nbreCompteur
    print(f"le factoriel de {nbreSaisi} est: {factoriel}")