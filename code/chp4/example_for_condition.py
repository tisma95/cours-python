"""
    Ce programme affiche la liste des caractères d'un nom.
    Il dira les caractères qui sont des voyelles ou non.
"""

name = "Christophe"

# Boucle sur la liste des caractères du nom
print("Le nom " + name + " contient les lettres suivantes:\n")
for letter in name:
    # Verification si la lettre est une voyelle ou non
    if letter in "AEIOUYaeiouy":
        print("La voyelle:", letter)
    else:
        print("La consonne:", letter)






