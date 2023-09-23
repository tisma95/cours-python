Python 3.11.4 (tags/v3.11.4:d2340ef, Jun  7 2023, 05:45:37) [MSC v.1934 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.


def hello():
    print("Bonjour tout le monde")

...     
>>> hello()
Bonjour tout le monde
>>> hello()
Bonjour tout le monde
>>> hello()def hello():
...     print("Bonjour tout le monde")
...     
SyntaxError: invalid syntax
>>> 
>>> 
>>> 
>>> 
>>> 
>>> def hello():
...     print("Bonjour tout le monde")
... 
...     
>>> # Exécution
>>> hello()
Bonjour tout le monde
>>> hello()
Bonjour tout le monde
>>> 
>>> 
>>> 
>>> def hello(nom):
...     print(f"Bonjour {nom} !")
... 
...     
>>> # Exécution
>>> hello("Christophe")
Bonjour Christophe !
>>> hello("Oscar")
Bonjour Oscar !
>>> 
>>> 
>>> 
>>> def nomComplet(nom, prenom):
...     print(f"Le nom est {nom} et le prénom {prenom}.")
... 
...     
>>> # Appel en respectant l'ordre
>>> nomComplet("Doé", "John")
Le nom est Doé et le prénom John.
>>> # Appel en ne respectant pas l'ordre
>>> nomComplet("John", "Doé")
Le nom est John et le prénom Doé.
>>> 
>>> 
>>> 
>>> def nomComplet(nom, prenom):
...     print(f"Le nom est {nom} et le prénom {prenom}.")
... 
...     
>>> # Appel en désordre
>>> nomComplet(prenom="John", nom="Doé")
Le nom est Doé et le prénom John.
>>> nomComplet(nom="Doé", prenom="John")
Le nom est Doé et le prénom John.
