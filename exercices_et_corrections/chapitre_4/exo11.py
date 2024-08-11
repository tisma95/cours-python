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

codeSecret = 1234
limite = 3
saisieCode = input(f"Veuillez saisir votre code: ({limite} tentatives restantes)")
while saisieCode != codeSecret:
    limite = limite - 1
    if limite >= 1:
        saisieCode = input(f"Veuillez saisir votre code: ({limite} tentatives restantes)")
    else:
        print("Carte bloquéé")
print("paiement accepté")
