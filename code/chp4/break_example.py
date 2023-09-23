"""
 Programme essayant d'afficher les nombres 0, 1, 3, 4, 5, ...10
"""

# Utilisation de break dans une boucle for
print("Exemple break avec for:")
for n in range(0, 11):
    if n == 2:
        break
    print(n)

print("\n\n")

# Utilisation de break dans une boucle while
print("Exemple break avec while:")
nb = -1 # On commence ici à partir de -1 pour avoir le 0
while nb < 10:
    nb += 1
    if nb == 2:
        break
    print(nb)





while 1: #=> On peut remplacer 1 par True qui est toujours vrai donc boucle infinie
    reponse = input("Tapez 'Q' pour quitter:")
    if reponse == 'Q':
        print("Fin !")
        break





