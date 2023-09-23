"""
    Afficher le nom Christophe en majuscule et en minuscule
"""

name = "Christophe"

# Convertion en majuscule #=> équivalent à "Christophe".upper()
majuscule = name.upper()
print(name, "en majuscule est:", majuscule)

# Convertion en lower
minuscule = name.lower() #=> équivalent à "Christophe".lower()
print(name, "en minuscule est:", minuscule)




while True:
    reponse = input("Tapez 'Q ou q' pour quitter:")
    if reponse.upper() == 'Q':
        print("Fin !")
        break

while True:
    reponse = input("Tapez 'Q ou q' pour quitter:")
    if reponse.lower() == 'q':
        print("Fin !")
        break
