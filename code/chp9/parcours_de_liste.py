Python 3.11.4 (tags/v3.11.4:d2340ef, Jun  7 2023, 05:45:37) [MSC v.1934 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.


# Création d'une liste
liste = [1, 3, "a", "b"]
# Affichage des valeurs de la liste avec while
while indice < len(liste):
    print(liste[indice])

    
Traceback (most recent call last):
  File "<pyshell#7>", line 1, in <module>
    while indice < len(liste):
NameError: name 'indice' is not defined
# Création d'une liste
# Création d'une liste




# Création d'une liste
liste = [1, 3, "a", "b"]
# Affichage des valeurs de la liste avec while
indice = 0
while indice < len(liste):
    print(liste[indice])
    indice += 1

    
1
3
a
b



# Création d'une liste
>>> liste = [1, 3, "a", "b"]
>>> # Affichage des valeurs de la liste avec for
>>> for indice in range(len(liste)):
...     print(liste)
... 
...     
[1, 3, 'a', 'b']
[1, 3, 'a', 'b']
[1, 3, 'a', 'b']
[1, 3, 'a', 'b']
>>>     # Création d'une liste
...     
>>> 
>>> 
>>> 
>>> # Création d'une liste
>>> liste = [1, 3, "a", "b"]
>>> # Affichage des valeurs de la liste avec for
>>> for indice in range(len(liste)):
...     print(liste[indice])
... 
...     
1
3
a
b
>>> 
>>> 
>>> 

>>> 
>>> 
>>> 
>>> # Création d'une liste
>>> liste = [1, 3, "a", "b"]
>>> # Parcours avec for
>>> for elt in liste:
...     print(elt)
... 
...     
1
3
a
b
>>> 
>>> 
>>> # Création d'une chaine de caractère
>>> msg = "Hello"
>>> for carac in msg:
...     print(carac)
... 
...     
H
e
l
l
o
>>> 
>>> 
>>> 
