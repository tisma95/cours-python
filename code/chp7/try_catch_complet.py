nbre1 = input("Entrer le nombre 1:")
nbre2 = input("Entrer le nombre 2:")

try:
    nbre1 = int(nbre1)
    nbre2 = int(nbre2)
    resultat = nbre1 / nbre2
    print(f"{nbre1} / {nbre2} = {resultat}")
except ValueError:
    print("Vous devez saisir des nombres svp !")
except ZeroDivisionError:
    print("La division par zéro est impossible !")


