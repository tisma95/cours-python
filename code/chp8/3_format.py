Python 3.11.4 (tags/v3.11.4:d2340ef, Jun  7 2023, 05:45:37) [MSC v.1934 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.


nom = "John"
prenom = "Doe"
age = 14
print("Je suis {0} {1} j'ai {age} ans.".format(nom, prenom, age))
Traceback (most recent call last):
  File "<pyshell#5>", line 1, in <module>
    print("Je suis {0} {1} j'ai {age} ans.".format(nom, prenom, age))
KeyError: 'age'


nom = "John"
prenom = "Doe"
age = 14
print("Je suis {0} {1} j'ai {2} ans.".format(nom, prenom, age))
Je suis John Doe j'ai 14 ans.
nomComplet = "{0} {1}".format(nom, prenom)

nomComplet
'John Doe'


nom = "John"
prenom = "Doe"
age = 14
personne = "{0} {1} {2}".format(nom, prenom, age)

nom = "John"
prenom = "Doe"
age = 14
personne = "{0} {1} {2}".format(nom, prenom, age)
personne
'John Doe 14'
type(personne)
<class 'str'>
print(personne)
John Doe 14
John Doe 14
SyntaxError: invalid syntax
personne = "{1} {0} {2}".format(nom, prenom, age)
personne
'Doe John 14'
personne = "{1} {0} {2}".format(nom, prenom, age)'Doe John 14'
SyntaxError: invalid syntax

personne = "{} {} {}".format(nom, prenom, age)
print(personne)
John Doe 14
John Doe 14
SyntaxError: invalid syntax

nom = "John"
prenom = "Doe"
age = 14
print("Je suis {nom} {prenom} j'ai {age} ans.".format(nom, prenom, age))
Traceback (most recent call last):
  File "<pyshell#41>", line 1, in <module>
    print("Je suis {nom} {prenom} j'ai {age} ans.".format(nom, prenom, age))
KeyError: 'nom'
print("Je suis {nom} {prenom} j'ai {age} ans.".format(nom, prenom, age))
Traceback (most recent call last):
  File "<pyshell#42>", line 1, in <module>
    print("Je suis {nom} {prenom} j'ai {age} ans.".format(nom, prenom, age))
KeyError: 'nom'


print("Je suis {nom} {prenom} j'ai {age} ans.".format(nom="John", prenom="Doe", age=14))
Je suis John Doe j'ai 14 ans.

print("Je suis {nom=} {prenom=} j'ai {age=} ans.".format(nom="John", prenom="Doe", age=14))
Traceback (most recent call last):
  File "<pyshell#46>", line 1, in <module>
    print("Je suis {nom=} {prenom=} j'ai {age=} ans.".format(nom="John", prenom="Doe", age=14))
KeyError: 'nom='
print("Je suis {nom} {prenom} j'ai {age} ans.".format(nom="John", prenom="Doe", age=14))
Je suis John Doe j'ai 14 ans.
nom = "John"

nom = "John"
prenom = "Doe"
age = 14
print("{nom=} {prenom=} {age=}".format(nom, prenom, age))
Traceback (most recent call last):
  File "<pyshell#53>", line 1, in <module>
    print("{nom=} {prenom=} {age=}".format(nom, prenom, age))
KeyError: 'nom='
print("Je suis {nom} {prenom} j'ai {age} ans.".format(nom="John", prenom="Doe", age=14))
Je suis John Doe j'ai 14 ans.
>>> 
>>> 
>>> f"{name=}"
Traceback (most recent call last):
  File "<pyshell#57>", line 1, in <module>
    f"{name=}"
NameError: name 'name' is not defined
>>> f"{nom=}"
"nom='John'"
>>> print("Je suis {nom=} {prenom=} j'ai {age=} ans.".format(nom="John", prenom="Doe", age=14))
Traceback (most recent call last):
  File "<pyshell#59>", line 1, in <module>
    print("Je suis {nom=} {prenom=} j'ai {age=} ans.".format(nom="John", prenom="Doe", age=14))
KeyError: 'nom='
>>> print("{nom=} {prenom=} {age=}".format(nom, prenom, age))
Traceback (most recent call last):
  File "<pyshell#60>", line 1, in <module>
    print("{nom=} {prenom=} {age=}".format(nom, prenom, age))
KeyError: 'nom='
>>> print("Je suis {nom=} {prenom=} j'ai {age=} ans.".format(nom="John", prenom="Doe", age=14))
Traceback (most recent call last):
  File "<pyshell#61>", line 1, in <module>
    print("Je suis {nom=} {prenom=} j'ai {age=} ans.".format(nom="John", prenom="Doe", age=14))
KeyError: 'nom='

>>> 
>>> 

>>> 
>>> # Formater avec f-string
>>> nom = "John"
>>> prenom = "Doe"
>>> age = 14
>>> print(f"{nom} {prenom} {age}")
John Doe 14
>>> # Formater en affichant le nom des variables
>>> print(f"{nom=} {prenom=} {age=}")
nom='John' prenom='Doe' age=14
>>> # Création de variable
>>> nomComplet = f"{nom} {prenom}"
>>> print(nomComplet)
John Doe
>>> nomComplet = f"{0} {1}"
>>> 
>>> nomComplet
'0 1'
