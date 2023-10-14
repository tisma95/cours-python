Python 3.11.4 (tags/v3.11.4:d2340ef, Jun  7 2023, 05:45:37) [MSC v.1934 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> 
>>> 
>>> # Fonction qui demande un nombre à l'utilisateur
>>> 
==================================================================================== RESTART: Shell ====================================================================================
>>> # Fonction qui demande un nombre à l'utilisateur et retourne le carré
>>> def saisieEtCalculCarre():
...     nbre = input('Entrer un nombre:')
...     nbre = int(nbre)
...     return nbre * nbre
... 
>>> # Execution avec saisie d'un nombre
>>> saisieEtCalculCarre()
Entrer un nombre:2
4
>>> 
==================================================================================== RESTART: Shell ====================================================================================
>>> # Fonction qui demande un nombre à l'utilisateur et retourne le carré
>>> def saisieEtCalculCarre():
...     nbre = input('Entrer un nombre:')
...     nbre = int(nbre)
...     return nbre * nbre
... 
>>> # Exécution avec saisie d'un nombre
>>> saisieEtCalculCarre()
Entrer un nombre:2
4
>>> # Exécution avec saisie de tout sauf un nombre
>>> saisieEtCalculCarre()
Entrer un nombre:a
Traceback (most recent call last):
  File "<pyshell#19>", line 1, in <module>
    saisieEtCalculCarre()
  File "<pyshell#15>", line 3, in saisieEtCalculCarre
    nbre = int(nbre)
ValueError: invalid literal for int() with base 10: 'a'
