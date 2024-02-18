#################################################################
#               Author: Ismael Maurice                          #
#               Language: Python                                #
#               Chapter 3                                       #
#               File: exo4.py                                   #
#################################################################

"""
    Objectifs: Ecrire un programme qui demande l’âge d’une personne à l’utilisateur.
    Ensuite, il l’informe de sa catégorie:
    Poussin de 0 à 7 ans,
    Pupille de 8 à 9 ans,
    Minime de 10 à 11 ans,
    Cadet de 12 à 17 ans,
    Junior de 18 à 49 ans
    et Senior après 50 ans.
"""

# Demander l'âge à l'utilisateur
age = input("Veuillez entrer un âge svp:")
# Convertion en entier et affichage de la saisie de l'utilisateur
age = int(age)
if age < 2:
    print(f"Vous avez saisi {age} an")
else:
    print(f"Vous avez saisi {age} ans")
# Affichage de la catégorie de l'utilisateur
categorie = "Inconnue"
if age >= 0 and age <= 7:
    categorie = "Poussin"
elif age >= 8 and age <= 9:
    categorie = "Pupille"
elif age >= 10 and age <= 11:
    categorie = "Minime"
elif age >= 12 and age <= 17:
    categorie = "Cadet"
elif age >= 18 and age <= 49:
    categorie = "Junior"
elif age >= 50:
    categorie = "Senior"
print(f"L'âge {age} appartient à la catégorie {categorie}")