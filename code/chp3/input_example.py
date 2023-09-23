
saisie = input("Entrer votre age:")

# La saisie de l'utilisateur est une chaine de caractère de type string
print(type(saisie))

# Conversion en entier car un age est en entier
age = int(saisie)

# Condition en fonction de l'âge
if age >= 18:
    print("Vous êtes majeur")
else:
    print("Vous êtes mineur")



