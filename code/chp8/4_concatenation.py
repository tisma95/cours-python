Python 3.11.4 (tags/v3.11.4:d2340ef, Jun  7 2023, 05:45:37) [MSC v.1934 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> 
>>> 
>>> nom = "John"
>>> 
>>> 
>>> # Concaténation simple
>>> nom = "John"
>>> prenom = "Doe"
>>> nom + prenom
'JohnDoe'
>>> # Concaténation en mettant un espace
>>> nom + " " + prenom
'John Doe'
>>> # Concaténation de plusieurs chaînes
>>> "Persone " + nom + " " + prenom
'Persone John Doe'
>>> 
>>> # Essaie concaténation entre chaine et nombre
>>> nom = "John"
>>> age = 14
>>> nom + age
Traceback (most recent call last):
  File "<pyshell#17>", line 1, in <module>
    nom + age
TypeError: can only concatenate str (not "int") to str
>>> # Concaténation avec convertion
>>> nom = "John"
>>> age = 14
>>> nom + str(age)
'John14'
