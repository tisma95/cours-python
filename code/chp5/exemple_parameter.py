Python 3.11.4 (tags/v3.11.4:d2340ef, Jun  7 2023, 05:45:37) [MSC v.1934 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> def hello(nom="Christophe"):
...     print("Bonjour", nom, "!")
... 
...     
>>> # Appel sans spécifier le paramètre
>>> hello()
Bonjour Christophe !
>>> # Appel en spécifiant le paramètre
>>> hello("Toto")
Bonjour Toto !
>>> hello(nom="tout le monde")
Bonjour tout le monde !
>>> 
>>> 
>>> def nomComplet(prenom, nom="Doé"):
...     print(f"Votre nom est {nom} et prénom {prenom} !")
... 
...     
>>> # Appel sans le paramètre optionnel
>>> nomComplet("John")
Votre nom est Doé et prénom John !
>>> nomComplet(prenom="John")
Votre nom est Doé et prénom John !
>>> # Appel avec le paramètre optionnel
>>> nomComplet("John", "Toto")
Votre nom est Toto et prénom John !
>>> 
>>> 
