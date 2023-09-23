"""
 Programme affichant les nombres 0, 1, 3, 4, 5, ...10
"""

# Utilisation de continue dans une boucle for
print("Exemple avec for:")
for n in range(0, 11):
    if n == 2:
        continue
    print(n)

print("\n\n")

# Utilisation de continue dans une boucle while
print("Exemple avec while:")
nb = -1 # On commence ici à partir de -1 pour avoir le 0
while nb < 10:
    nb += 1
    if nb == 2:
        continue
    print(nb)


