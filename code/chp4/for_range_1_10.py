"""
    Programme 1: Nombre de 0 à 10
"""

print("Programme 1: Nombre de 0 à 10:\n")
# On peut ignorer ici le 0 en utilisant range(11)
for n in range(0, 11):
    print(n)

print("\n\n")


"""
    Programme 2: Nombre de 10 à 1
"""

print("Programme 2: Nombre de 10 à 1:\n")
# On peut pas ignorer ici le 0 car c'est le stop
for n in range(10, 0, -1):
    print(n)

print("\n\n")

"""
    Programme 3: Nombre de 0 à 10 en sautant un nombre
"""

print("Programme 3: Nombre de 0 à 10 en sautant un nombre:\n")
# On peut pas ignorer ici le 0
for n in range(0, 10, 2):
    print(n)


