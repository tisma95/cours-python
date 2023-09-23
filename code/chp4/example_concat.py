"""
    Concaténation avec formatage
"""

# Initialisation des variables
nom = "Christophe"
postal = 29

# Avec {}
print(f"Message 1: {nom} habite le {postal}")
print(F"Message 2: {nom} habite le {postal}")

# Avec string.format => l'ordre dans format a de l'importance
print("Message 3: {0} habite le {1}".format(nom, postal))
print("Message 4: {0} habite le {1}".format(postal, nom)) #=> Si on inverse on obtient un autre résultat

# Avec affichage du nom des variable
print(f"Message 5: {nom=} habite le {postal=}")
print(F"Message 6: {nom=} habite le {postal=}")


