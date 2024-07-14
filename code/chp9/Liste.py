######### Parcours de liste avec enumerate #############

# Création d'une liste avec des éléments de départ
maListe = ['a', 1, 'toto', 4]
for indice,valeur in enumerate(maListe):
    print(f"Element à l'indice {indice}: {valeur}")

# Création d'une liste avec des éléments de départ
maListe = ['a', 1, 'toto', 4]
# Enumerate avec une seule valeur
for element in enumerate(maListe):
    # Elément contient deux valeurs en indice 0 on a l'indice de l'élement et à l'indice 1 la valeur
    print("Elément actuelle de enumerate:", element)
    # Création de l'indice et valeur
    indice = element[0]
    valeur = element[1]
    print(f"Elément à l'indice {indice}: {valeur}")


# Création d'une chaine
message = "Hello World"
# Création de la liste de mots du message
mots = message.split(" ") #=> équivaut à message.split()
# La variable 'mots' est une liste de mots
print(mots)

######### De chaine vers liste #############

# Création d'une chaine
chaine = "a,b,c,d,e"
# Création d'une liste de caractères
caracteres = chaine.split(",")
# La variable 'caracteres' est une liste de caractères
print(caracteres)


# Création d'une chaine avec des espaces, tabulations et saut de lignes
chaine = "Hello World\nToto\tRoro"
print(chaine)
# Création d'une liste de mots
mots = chaine.split()
print(mots)

######### De liste vers chaines #############

# Création d'une liste de mots
maListe = ["Toto", "Roro"]
print(maListe)
# Création d'une chaine avec un espace entre chaque mot
chaine1 = " ".join(maListe)
print(chaine1)
# Création d'une chaine avec | entre chaque mot
chaine2 = "|".join(maListe)
print(chaine2)

######### Join vs Split #############

# Création de liste de nombres
nombres = [1, 2, 3, 4]
print(nombres)
# Création d'une liste qui va contenir le double de chaque nombre
double = [2 * n for n in nombres]
# La variable 'double' est bien une liste
print(type(double))
print(double)
# Création d'une liste qui va contenir le carré de chaque nombre
carre = [elt * elt for elt in nombres]
# La variable 'carre' est bien une liste
print(type(carre))
print(carre)


######### Parcours avec filtrage #############

# Création de liste des nombres de 0 à 10
nombres = [n for n in range(11)]
print("Les nombres de 0 à 10 sont:")
print(nombres)
# Création d'une liste des nombres pairs de 0 à 10 basée sur la liste précédente
pairs = [n for n in nombres if n % 2 == 0]
print("La liste des nombres pairs entre 0 et 10 sont:")
print(pairs)

######### Méthodes usuelles de liste #############
liste = ['a', 1, 2, 'a']
'a' in liste
'b' in liste
1 in liste

liste = ['a', 1, 2, 'a']
print(liste)
'b' in liste
liste.append('b')
print(liste)
'b' in liste


liste = [1, 2, 3]
print(liste)
liste.reverse()
print(liste)

liste = ['a', 1, 2, 'a']
print(liste)
liste.count('a')
liste.count('b')

