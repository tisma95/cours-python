Python 3.11.4 (tags/v3.11.4:d2340ef, Jun  7 2023, 05:45:37) [MSC v.1934 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.

# Initialisation de la chaîne
nom = "Christophe"
>>> # Initialisation de la variable indice
>>> indice = 0
>>> print("Les caractères de la chaine '" + nom + "' sont:")
Les caractères de la chaine 'Christophe' sont:
>>> while indice < len(nom):
...     print(nom[indice])
...     indice += 1
... 
...     
C
h
r
i
s
t
o
p
h
e
>>> 
>>> # Initialisation de la chaîne
>>> # Initialisation de la chaîne
>>> # Initialisation de la chaîne
>>> 
>>> # Initialisation de la chaîne
>>> nom = "Christophe"
>>> # Initialisation de la variable total de caractères
>>> total = len(nom)
>>> for indice in range(total):
...     print(nom[indice])
... 
...     
C
h
r
i
s
t
o
p
h
e
>>> 
>>> # Initialisation de la chaine
>>> msg = "Hello"
>>> msg[0]
'H'
>>> msg[1]
'e'
>>> msg[-1]
'o'
>>> msg[-2]
'l'
>>> # Initialisation de la chaine
>>> msg = "Hello"
>>> msg[100]
Traceback (most recent call last):
  File "<pyshell#31>", line 1, in <module>
    msg[100]
IndexError: string index out of range
