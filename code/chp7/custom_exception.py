
nbre = input("Entrer un nombre positif:")
try:
    # Convertion en nombre
    nbre = int(nbre)
    # Verification si le nombre est positif ou non
    if nbre <= 0:
        # Si l'on ne saisit pas un nombre strictement positif on lève l'exception
        raise NombreNonPositif("Nombre strictement positif attendu !")
except ValueError:
    # Si l'on ne saisit pas un nombre
    print("Vous devez saisir un nombre svp !")
else:
    # Affichage du message en cas de non erreur
    print("Merci vous avez saisi le nombre positif:", nbre)






