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

# TODO: Ecrire le code en python ci dessous


codeSecret = "1234"
limiteSaisies = 3
saisieCode = ''
while saisieCode != codeSecret:
    saisieCode = input(f"Veuillez entrer votre code secret ({limiteSaisies} essais restants)")
    if saisieCode == codeSecret:
        print("Paiement accepté")
    else:
        limiteSaisies = limiteSaisies - 1
        if limiteSaisies == 0:
            print("Carte bloquée...")
            break # AFIN DE NE PAS CONTINUER -1 -2  





