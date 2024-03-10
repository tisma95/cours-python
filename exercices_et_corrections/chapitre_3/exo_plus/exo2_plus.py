
"""
Exo 2:
Le gérant d'une coopérative agricole attribue un emploi du temps à ses travailleurs
suivant les conditions de la météo de la journée. il établit les règles suivantes:

- si la météo est jugée" bonne" l’employé effectue l'emploi du temps 1.
- si la météo est jugée "mauvaise" l’employé effectue l'emploi du temps 2.
- si la météo est jugée intermédiaire" l’employé effectue l'emploi du temps 3.

1.Ecrire un algorithme en langage naturel qui donne l’emploi du temps de l’employé suivant la météo journalière.
2.Ecrire cet algorithme en Python.
"""

print("Quelle est la météo du jour ? ('b ou B' pour bonne, 'i ou I' pour intermédaire et 'm ou M' pour mauvaise)")
meteo = input("Entrer une valeur:")

# Méthode 1
if meteo == "B" or meteo == "b":
    print("Vous devez utiliser l'emploi du temps 1")
elif meteo == "I" or meteo == "i":
    print("Vous devez utiliser l'emploi du temps 3")
elif meteo == "M" or meteo == "m":
    print("Vous devez utiliser l'emploi du temps 2")
else:
    print("Météo inconnue")

# Méthode 2
if meteo.upper() == "B":
    print("Vous devez utiliser l'emploi du temps 1")
elif meteo.upper() == "I":
    print("Vous devez utiliser l'emploi du temps 3")
elif meteo.upper() == "M":
    print("Vous devez utiliser l'emploi du temps 2")
else:
    print("Météo inconnue")
