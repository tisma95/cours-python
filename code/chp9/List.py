Python 3.11.4 (tags/v3.11.4:d2340ef, Jun  7 2023, 05:45:37) [MSC v.1934 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.


# Méthode avec le mot clé list
maListe = list()
type(maListe)
<class 'list'>



# Méthode avec une


# Méthode avec le mot clé list
maListe = list()
type(maListe)
<class 'list'>
maListe
[]





# Méthode avec une liste vide
maListe = []
type(maListe)
<class 'list'>
maListe
[]


# Liste avec des éléménts de départ
maListe = [1, 'a', True, 2.0]
type(maListe)
<class 'list'>
maListe
[1, 'a', True, 2.0]



# Création d'une liste
maListe = [1, 'a', True, [2, 3], 2.0]
# Affichage du premier élement de la liste
maListe[0]
1


# Création d'une liste
maListe = [1, 'a', True, [2, 3], 2.0]
# Affichage du premier élement de la liste et son type
maListe[0]
1
type(maListe[0])
<class 'int'>
# Affichage du deuxième élement de la liste et son type
maListe[1]
'a'
type(maListe[1])
<class 'str'>
# Affichage du troisième élement de la liste et son type
maListe[2]
True
type(maListe[2])
<class 'bool'>
# Affichage du quatrième élement de la liste et son type
maListe[3]
[2, 3]
type(maListe[3])
<class 'list'>
# Affichage du dernier élement de la liste et son type
maListe[4]
2.0
type(maListe[4])
<class 'float'>


liste = []
liste.append(1)
liste
[1]
liste
[1]




# Création d'une liste vide


# Création d'une liste avec des élementsmaListe = [1, 'a', True, [2, 3], 2.0]
# Création d'une liste avec des élements


# Création d'une liste avec des élements
maListe = [1, 'a', True, [2, 3], 2.0]
# Affichage de l'élement à l'indice 2
maListe[2]
True
# Insertion d'un élement à l'indice 2
maListe.insert(2, 'John')
maListe
[1, 'a', 'John', True, [2, 3], 2.0]
# Affichage de l'élement à l'indice 2
maListe[2]
'John'



# Création d'une liste avec des élements
maListe = [1, 'a', True, [2, 3], 2.0]
# Affichage de la liste
maListe
[1, 'a', True, [2, 3], 2.0]
# Ajout d'un élement à la fin de la liste avec append
maListe.append("John")
# Affichage de la liste
maListe
[1, 'a', True, [2, 3], 2.0, 'John']



# Création d'une liste
maListe = [1, 'a', True, [2, 3], 2.0]
maListe
[1, 'a', True, [2, 3], 2.0]
# Pour changer la valeur de l'élément 'a' à l'indice 1
maListe[1] = 2

# Création d'une liste
maListe = [1, 'a', True, [2, 3], 2.0]
maListe
[1, 'a', True, [2, 3], 2.0]
# Pour changer la valeur de l'élément 'a' à l'indice 1
maListe[1] = 2
maListe
[1, 2, True, [2, 3], 2.0]




>>> 
>>> # Création d'une liste 1
>>> liste1 =[1, 2]
>>> liste1
[1, 2]
>>> # Création d'une liste 2
>>> liste2 = [2, 3]
>>> liste2
[2, 3]
>>> # Ajout des élements de la liste 2 à la fin de la liste 1
>>> liste1.extend(liste2)
>>> liste1
[1, 2, 2, 3]
>>> 
>>> 
>>> 
>>> 
>>> 
>>> liste3 = liste1.extends(liste2)
Traceback (most recent call last):
  File "<pyshell#124>", line 1, in <module>
    liste3 = liste1.extends(liste2)
AttributeError: 'list' object has no attribute 'extends'. Did you mean: 'extend'?
>>> liste3 = liste1 + liste2
>>> liste3
[1, 2, 2, 3, 2, 3]
>>> 
>>> 
>>> 
>>> 
>>> # Création d'une liste 1
>>> liste1 =[1, 2]
>>> liste1
[1, 2]
>>> # Création d'une liste 2
>>> liste2 = [2, 3]
>>> liste2
[2, 3]
>>> # Ajout des élements de la liste 2 à la fin de la liste 1
>>> liste1 += liste2 #=> équivaut à liste1 = liste1 + liste2
>>> liste1
[1, 2, 2, 3]
>>> 
>>> 
>>> 
>>> # Création d'une liste 1
>>> liste1 =[1, 2]
>>> liste1
[1, 2]
>>> # Création d'une liste 2
>>> liste2 = [2, 3]
>>> liste2
[2, 3]
>>> # Création d'une liste 3 qui est la liste 1 suivant des élements de la liste 2
>>> liste3 = liste1 + liste2
>>> liste3
[1, 2, 2, 3]
>>> 
>>> 
>>> 
