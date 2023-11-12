# Mini Projet 2

En Python, pour générer un nombre aléatoire on utilise le module random comme ci-dessous:
```python
  # Génération de nombre aléatoire
  import random
  random.randint(0, 100)
```
Le code précédent génère un nombre aléatoire entre 0 et 100 inclus.
Utilisez le code précédent, pour réaliser le mini-projet du nombre magique:
Coder un jeu de nombre magique où l’utilisateur doit deviner un nombre aléatoire généré en 10 tentatives
maximum. Le jeu doit être constitué de trois modes, le mode facile (nombre magique entre 0 et 100), le
mode moyen (nombre magique entre 0 et 1000) et le mode difficile (nombre magique entre 0 et 10000).
Après choix du mode faire deviner le nombre magique à l’utilisateur quand l’utilisateur entre un nombre
inférieur au nombre magique afficher « Le nombre magique est plus grand que nombreSaisi ». Quand
l’utilisateur entre un nombre supérieur au nombre magique afficher « Le nombre magique est plus petit que
nombreSaisi ». Sinon afficher « Bingo vous avez trouvé le nombre magique en x essais ». En cas d’échec
afficher un message d’échec et demander si l’utilisateur veut recommencer si oui réafficher le menu.
L’organisation des fonctions et modules est libre.