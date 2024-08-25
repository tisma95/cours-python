#################################################################
#               Author: Ismael Maurice                          #
#               Language: Python                                #
#               Chapter 4                                       #
#               File: exo11.py                                  #
#################################################################

"""
    Objectifs: Soit un utilisateur dont le code de carte bancaire est 1234. Demander à l’utilisateur de saisir son code secret
    avec un nombre limite de 3 essais maximum. Au bout de 3 échecs arrêter le programme en affichant « Carte
    bloquée » sinon afficher « Paiement accepté ».
"""

codeSecret = "1234"
limiteSaisies = 3
saisieCode = ''

while saisieCode != codeSecret and limiteSaisies > 0:
    saisieCode = input(f"\nVeuillez entrer votre code secret ({limiteSaisies} essais restants):")
    if saisieCode == codeSecret:
        print("\nPaiement accepté")
    else:
        limiteSaisies = limiteSaisies - 1
        print("\nCode incorrect")
        if limiteSaisies == 0:
            print("\nCarte bloquée...\n")
            #break # Pour sortir de la boucle si on utilise qu'une seule condition while saisieCode != codeSecret:
