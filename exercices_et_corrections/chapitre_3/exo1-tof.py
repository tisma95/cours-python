#################################################################
#               Author: Ismael Maurice                          #
#               Language: Python                                #
#               Chapter 3                                       #
#               File: exo1.py                                   #
#################################################################

"""
    Objectifs: Réécrire le programme suivant en utilisant les opérateurs logiques.

    username = "Christophe"
    if username == "Christophe":
        print("Bienvenue")
    elif username == "John":
        print("Bienvenue")
    else:
        print("Utilisateur inconnu")
"""

# TODO: Ecrire le code en python ci dessous

# print ("Votre nom d'utilisateur ?")
# username = input()
# if username == "Christophe":
#     print ("Bienvenue",username,"!")
# elif username == "John":
#     print ("Bienvenue",username,"!")
# else:
#     print (username,"inconnu...")

tentativ=3
print ("Votre nom d'utilisateur ?\n(",tentativ,"tentatives restantes )")
username = input("---> ")
while tentativ !=1 and username != "Christophe" and username != "John":
    tentativ=tentativ-1
    print ("\nIl vous reste", tentativ, "tentatives avant BLOCAGE DU SYSTEME !\n" )
    username=input("---> ")
if username == "Christophe":
    print ("\nBienvenue",username,"!\n")
elif username == "John":

    print ("\nBienvenue",username,"!\n")
else:
    print ("\nSUITE AUX 3 ERREURS, VOUS N'AVEZ PLUS LE DROIT DE VOUS CONNECTER, VEUILLEZ CONTATCTER NOTRE S.A.V.\n" )
