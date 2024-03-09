"""
Exo 3:
Objectifs : programmer un petit test sur les tables de multiplication.
• Définis une variable a, à laquelle tu affectes une valeur au hasard entre 1 et 12.
• Même chose pour une variable b.
• Affiche à l’écran la question : « Combien vaut le produit a × b ? » (Remplace a et b par leur valeur !) • Récupère la réponse de l’utilisateur et transforme-la en un entier.
• Si la réponse est correcte affiche « Bravo ! », sinon affiche « Perdu ! La bonne réponse était. . . ».
"""
# Doc Chapitre 6 les modules
import random
Nb1=random.randint(1,12)
Nb1=int(Nb1)
Nb2=random.randint(1,12)
Nb2=int(Nb2)
Resultat=Nb1*Nb2
print (Nb1,"X",Nb2,"=")
Trouve=input()
Trouve=int(Trouve)
if Trouve == Resultat:
    print ("BRAVO !")
else:
    print ("Erreur, le produit de",Nb1,"X",Nb2,"est = à",Resultat)
