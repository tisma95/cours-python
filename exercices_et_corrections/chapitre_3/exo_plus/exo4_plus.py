'''
Exo 4:

Ecrire un programme en python qui demande à l'utilisateur son nom et ensuite ses prénoms.
Le programme doit ensuite afficher le nom complet de l'utilisateur en respectant les conventions française.
Supposons que l'utiliseur entre:
Nom: doé
Prénoms: john TOTO
le programme doit afficher votre nom complet est: DOE John Toto
Si il entre:
Nom: doé
Prénom: john il doit afficher DOE John
Vous aurez besoin des fonctions suivantes: *upper()* (voir exo 2 plus), *title*
'''

nom = input ("Veuillez entrer vore nom de famille: ")
prenoms = input ("Veuillez entrer vos prénoms: ")
print ("Bonjour", nom.upper(), prenoms.title())
