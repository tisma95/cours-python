#################################################################
#               Author: Ismael Maurice                          #
#               Language: Python                                #
#               Chapter 3                                       #
#               File: exo4.py                                   #
#################################################################

"""
    Objectifs: Ecrire un programme qui demande l’âge d’une personne à l’utilisateur. Ensuite, il l’informe de sa catégorie:
    Poussin de 0 à 7 ans, Pupille de 8 à 9 ans, Minime de 10 à 11 ans, Cadet de 12 à 17 ans, Junior de 18 à 49 ans
    et Senior après 50 ans.
"""

# TODO: Ecrire le code en python ci dessous

saisie=input ("Veuillez entrer votre âge: ")
age=int(saisie)
print ("Vous avez",age,"ans et entrez donc dans la cathégorie:")
if age >=50:
    print ("SENIOR")
elif (age >=18 and age <=49):
    print ("JUNIOR")
elif (age >=12 and age <=17):
    print ("CADET")
elif (age >=10 and age <=11):
    print ("MINIME")
elif (age >=8 and age <=9):
    print ("PUPILLE")
elif age <= 7:
    print ("POUSSIN")




