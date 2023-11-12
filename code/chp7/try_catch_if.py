
nbre = input("Entrer un nombre positif:")

try:
    # Convertion en nombre
    nbre = int(nbre)
    # Verification si le nombre est positif ou non
    assert nbre > 0
except ValueError:
    # Si l'on ne saisit pas un nombre
    print("Vous devez saisir un nombre svp !")
except AssertionError:
    # Si l'on ne saisit pas un nombre strictement positif
    print("Vous devez saisir un nombre strictement positif svp !")
else:
    # Affichage du message en cas de non erreur
    print("Merci vous avez saisi le nombre positif:", nbre)




