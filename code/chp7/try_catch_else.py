
nbre1 = input("Entrer le nombre 1:")
nbre2 = input("Entrer le nombre 2:")

try:
    # Code pouvant générer une erreur
    nbre1 = int(nbre1)
    nbre2 = int(nbre2)
    resultat = nbre1 / nbre2
except ValueError:
    print("Vous devez saisir des nombres svp !")
except ZeroDivisionError:
    print("La division par zéro est impossible !")
else:
    # Afficher le résultat de la division si aucune erreur
    print(f"{nbre1} / {nbre2} = {resultat}")


