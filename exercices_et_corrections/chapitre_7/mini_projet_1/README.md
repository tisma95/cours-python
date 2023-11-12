# Mini Projet 1

Créer un module multiplication qui contiendra les fonctions suivantes:
    • addition(nbre1, nbre2): qui retourne le résultat de nbre1 + nbre2
    • soustraction(nbre1, nbre2): qui retourne le résultat de nbre1 - nbre2
    • multiplication(nbre1, nbre2): qui retourne le résultat de nbre1 * nbre2
    • division(nbre1, nbre2): qui retourne le résultat de nbre1 / nbre2
Créer un deuxième module helper qui contiendra les fonctions suivantes:
    • afficheMenu(): qui affiche le menu des actions (addition, soustraction, multiplication, division)
    • saisirAction(minAction, maxAction): qui demande le numéro de l’action à réaliser numéro compris
entre minAction et maxAction par exemple dans notre cas çà sera entre 1 et 4
    • saisirNombre(typeNbre): qui va demander à l’utilisateur de saisir un nombre typeNbre permet de dire si
    c’est le nombre 1 ou le nombre 2 qui doit être renseigné.
Créer un fichier main.py qui va utiliser l’ensemble des fonctions des modules précédents pour faire réaliser
une calculatrice simple.
Cette fois-ci il faut gérer les cas d’erreurs possibles avec les blocs try/catch et si besoin finally/else/assert.