
nombre = input("Entrer un nombre:")
try:
    nombre = int(nombre)
    print("Vous avez saisi le nombre:", nombre)
except ValueError as exception:
    print("Voici l'exception:", exception)



