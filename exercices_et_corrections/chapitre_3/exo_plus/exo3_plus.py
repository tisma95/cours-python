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
N_MIN = 1
N_MAX = 12
nb1 = random.randint(N_MIN, N_MAX)
nb2 = random.randint(N_MIN, N_MAX)
resultat = nb1 * nb2
print (nb1, "X", nb2, "= ?")
trouve = input()
trouve = int(trouve)
if trouve == resultat:
    print ("BRAVO !")
else:
    print ("Erreur, le produit de", nb1, "X", nb2, "est égal à", resultat)
