Python 3.11.4 (tags/v3.11.4:d2340ef, Jun  7 2023, 05:45:37) [MSC v.1934 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.

# Déclaration d'une variable entière
a = 1
id(a)
140722933130024
# Déclaration d'une nouvelle variable a
a = 1
id(a)
140722933130024
# Déclaration d'une variable entière140722933130024

# Déclaration d'une variable entière
a = 1
id(a)
140722933130024
# Déclaration d'une variable entière b avec la même valeur
b = 1
id(b)
140722933130024

# Déclaration d'une variable chaine
nom1 = "Christophe"
id(nom1)
2328340450032
# Déclaration d'une autre variable chaine avec la même valeur
nom2 = "Christophe"
id(nom2)
2328340450032
nom1 is nom2
True
nom1 is not nom2
False
nom3 = "Christophe"
id(nom3)
2328340450032
nom4 = nom1
id(nom4)
2328340450032
nom1 = 'toto"
SyntaxError: incomplete input
nom1 = 'toto'
nom1
'toto'
nom4
'Christophe'
nom1 is nom4
False
nom1 is nom2
False
nom4 is nom2
True
username = "toto"
nom = input()
toto
id(username)
2328340455280
id(nom)
2328335078000






# Création d'une variable avec une valeur
a = 1
id(a)
140722933130024
# Demander une valeur à l'utilisateur qui va etre 1
b # Création d'une variable avec une valeur
1


# Création d'une variable avec une valeur
a = 1
id(a)
140722933130024
# Demander une valeur à l'utilisateur qui va être 1
b = input()
1
b
'1'
id(b)
140722933173376
# Même si on convertit en entier
b = int(b)
b
1
id(b)
140722933130024
# Création d'une variable avec une valeur

# Création d'une variable avec une valeur
a = 1
id(a)
140722933130024
# Demander une valeur à l'utilisateur qui va être 1
b = input()
b
id(b)
140722933176120
# Si on convertit en entier on aura le même id
b = int(b)
Traceback (most recent call last):
  File "<pyshell#72>", line 1, in <module>
    b = int(b)
ValueError: invalid literal for int() with base 10: 'b'
# Création d'une variable avec une valeur
a = 1
id(a)
140722933130024
# Demander une valeur à l'utilisateur qui va être 1
b = input()
1
id(b)
140722933173376
# Si on convertit en entier on aura le même id
b = int(b)
b
1
id(b)
140722933130024


# Chaine
a = "toto"
id(a)
2328340455280
b = input()
toto
id(b)
2328334397360
b = str(b)
id(b)
2328334397360



# Définition d'une variable chaine
nom1 = "John"
id(nom1)
2328340470704
# Démander à l'utilisateur de saisir une chaine qui sera la même valeur John
nom2 = input()
John
nom2
'John'
id(nom2)
2328335077232



# Cas des types simple entiers
a = 1
id(a)
140722933130024
b = 1
id(b)
140722933130024
# Demandons un entiers à l'utilisateur c
c = input()
1
c
'1'
# Après saisie la valeur est stockée dans une case différente
id(c)
140722933173376
# L'id devient identique à celui de a et b si on convertit en entier
c = int(c)
c
1
id(c)
140722933130024


# Cas des types simple entiers
a = 1
id(a)
140722933130024
id(b)
140722933130024
a is b
True
# Demandons un entiers à l'utilisateur c
c = input()
1
c
'1'
>>> # Après saisie la valeur est stockée dans une case différente
>>> id(c)
140722933173376
>>> c is a
False
>>> # L'id devient identique à celui de a et b si on convertit en entier
>>> c = int(c)
>>> c
1
>>> id(c)
140722933130024
>>> c is a
True
>>> 
>>> 

>>> a = '1'
>>> b = 1
>>> a == b
False
>>> 
>>> # Cas des types complexes comme les strings
>>> nom1 = "John"
>>> id(nom1)
2328340470704
>>> nom2 = "John"
>>> id(nom2)
2328340470704
>>> nom1 is nom2
True
>>> # Demander un nom à l'utilisateur qui sera la même valeur
>>> nom3 = input()
John
>>> nom3
'John'
>>> id(nom3)
2328340447920
>>> nom3 is nom1
False
>>> nom3 is nom2
False
>>> nom3 == nom1
True
>>> nom3 == nom2
True
