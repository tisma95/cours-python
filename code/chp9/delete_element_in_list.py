Python 3.11.4 (tags/v3.11.4:d2340ef, Jun  7 2023, 05:45:37) [MSC v.1934 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.


# Création d'une variable
msg = "Bonjour !"
>>> msg
'Bonjour !'
>>> # Suppression de la variable
>>> del msg
>>> msg
Traceback (most recent call last):
  File "<pyshell#7>", line 1, in <module>
    msg
NameError: name 'msg' is not defined
>>> 
>>> 
>>> 
>>> # Création d'une liste
>>> liste = [1, 'a', 2]
>>> liste
[1, 'a', 2]
>>> len(liste)
3
>>> # Suppression de l'élément à l'indice 1
>>> del liste[1]
>>> liste
[1, 2]
>>> len(liste)
2
>>> 
>>> 
>>> 
>>> del liste[3]
Traceback (most recent call last):
  File "<pyshell#22>", line 1, in <module>
    del liste[3]
IndexError: list assignment index out of range
>>> 
>>> 
>>> # Création d'une liste
>>> liste = [1, 'a', 2, 'a', 3]
>>> liste
[1, 'a', 2, 'a', 3]
>>> len(liste)
5
>>> liste.remove('a')
>>> # Seul le premier 'a' a été supprimé
>>> liste
[1, 2, 'a', 3]
>>> len(liste)
4
>>> # Suppression du prochain 'a'
>>> liste.remove('a')
>>> liste
[1, 2, 3]
>>> # Suppression d'un élement qui n'existe pas dans la liste génère une erreur
>>> liste.remove('a')
Traceback (most recent call last):
  File "<pyshell#37>", line 1, in <module>
    liste.remove('a')
ValueError: list.remove(x): x not in list
>>> 
>>> 
>>> 
>>> 
