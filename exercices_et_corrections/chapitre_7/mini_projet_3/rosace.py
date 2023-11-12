#################################################################
#               Author: Ismael Maurice                          #
#               Language: Python                                #
#               Projet: Turtle                                  #
#               Version: V1                                     #
#               File: rosace.py                                 #
#################################################################

from turtle import *

def drawRosace(table: int, modulo:int=360, radius:int=200, couleurCercle:str="red", couleurSegment:str="blue"):
    """
        Nom
        -------
        drawRosace

        Description
        ------------
        Dessine la table de multiplication dun nombre modulo un autre dans un cercle trigonométrique.

        Paramètres
        -----------
        :param table (int obligatoire): la table du nombre à dessiner
        :param modulo (int optionnel): la fin de la table de multiplication par défaut la valeur sera 360
        :param radius (int optionnel): le rayon du cercle à dessiner par défaut le rayon sera de 200
        :param couleurCercle (str optionnel): la couleur du cercle la valeur par défaut est red pour rouge et les valeurs possibles sont ["yellow", "gold", "orange", "red", "maroon", "violet", "magenta", "purple", "navy", "blue", "skyblue", "cyan", "turquoise", "lightgreen", "green", "darkgreen", "chocolate", "brown", "black", "gray"]
        :param couleurSegment (str optionnel): la couleur des segments du cercle la valeur par défaut est blue pour bleu et les valeurs possibles sont ["yellow", "gold", "orange", "red", "maroon", "violet", "magenta", "purple", "navy", "blue", "skyblue", "cyan", "turquoise", "lightgreen", "green", "darkgreen", "chocolate", "brown", "black", "gray"]

        Réponse
        ---------
        Affichage du résulat dans une fénêtre graphique.

        Exemples
        --------
        drawRosace(table=2) => Affiche la table de 2 modulo 360 dans un cercle de rayon 200 avec pour couleur rouge pour le cercle et bleu pour les segments du cercle
        drawRosace(table=2, modulo=100) => Affiche la table de 2 modulo 100 dans un cercle de rayon 200 avec pour couleur rouge pour le cercle et bleu pour les segments du cercle
        drawRosace(table=2, modulo=100, radius=100) => Affiche la table de 2 modulo 100 dans un cercle de rayon 100 avec pour couleur rouge pour le cercle et bleu pour les segments du cercle
        drawRosace(table=2, modulo=100, radius=100, couleurCercle="blue") => Affiche la table de 2 modulo 100 dans un cercle de rayon 100 avec pour couleur bleu pour le cercle et bleu pour les segments du cercle
        drawRosace(table=2, modulo=100, radius=100, couleurCercle="blue", couleurSegment="red") => Affiche la table de 2 modulo 100 dans un cercle de rayon 100 avec pour couleur bleu pour le cercle et rouge pour les segments du cercle
    """
    colors = ["yellow", "gold", "orange", "red", "maroon", "violet", "magenta", "purple", "navy", "blue", "skyblue", "cyan", "turquoise", "lightgreen", "green", "darkgreen", "chocolate", "brown", "black", "gray"]
    assert type(table) == int, "Vous devez fournir un nombre pour la table"
    assert table > 0, "Vous devez fournir un nombre supérieur à 0 pour la table"
    assert type(modulo) == int, "Vous devez fournir un nombre pour le modulo"
    assert modulo > 0, "Vous devez fournir un nombre supérieur à 0 pour le modulo"
    assert type(radius) == int, "Vous devez fournir un nombre pour le rayon"
    assert radius > 0, "Vous devez fournir un nombre supérieur à 0 pour le rayon"
    assert type(couleurCercle) == str, "Vous devez fournir une chaîne de caractères pour la couleur du cercle"
    assert couleurCercle in colors, f"Vous devez choisir une couleur de cercle parmi les suivantes: {', '.join(colors)}"
    assert type(couleurSegment) == str, "Vous devez fournir une chaîne de caractères pour la couleur des segments"
    assert couleurSegment in colors, f"Vous devez choisir une couleur des segments parmi les suivantes: {', '.join(colors)}"
    # Definition des variables de travail
    print(radius)
    pts = []
    initialPosition = 0, -radius


    def drawSegments():
        """
            Desine la multiplication de m = n * table pour les n de 1 à modulo - 1 en liant les points n et m.
        """
        color(couleurSegment)
        for n in range(1, modulo):
            m = (table * n) % modulo
            moveTo(pts[n])
            moveTo(pts[m], True)

    def moveTo(pos, trace=False):
        if not trace:
            up()
        goto(pos)
        down()

    def drawCircle():
        """
            Dessine le cercle initial.
        """
        color(couleurCercle)
        moveTo(initialPosition)
        deltaAngle = 360 // modulo
        for _ in range(modulo):
            pts.append(pos())
            circle(radius, deltaAngle)
    # Display the rosace
    window = Screen()
    window.setup(width = 1.0, height = 1.0)
    window.title(f'Rosace of {table} modulo {modulo}')
    S_WIDTH, S_HEIGHT = screensize();
    # window.setup(width=1.0, height=1.0, startx=None, starty=None)
    up()
    goto((int(S_WIDTH/2), -int(S_HEIGHT/2)))
    down()
    speed("fastest")
    drawCircle()
    drawSegments()
    exitonclick()