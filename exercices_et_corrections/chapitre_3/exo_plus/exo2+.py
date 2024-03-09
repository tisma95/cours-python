
"""
Exo 2:
Le gérant d'une coopérative agricole attribue un emploi du temps à ses travailleurs
suivant les conditions de la météo de la journée. il établit les rèles suivantes:

- si la météo est jugée" bonne" l’employé effectue l'emploi du temps 1.
- si la météo est jugée "mauvaise" l’employé effectue l'emploi du temps 2.
- si la météo est jugée intermédiaire" l’employé effectue l'emploi du temps 3.

1.Ecrire un algorithme en langage naturel qui donne l’emploi du temps de l’employé suivant la météo journalière.

Debut:
    Ecrire "Quelle est la météo du jour ?"
    Ecrire " (B = Bonne, I = Intermédiaire, M = Mauvaise)
    Lire MeteoJour
    Si MeteoJour == B Alors
        Ecrire EmploisDuTemps1
    SinonSi MeteoJour == M Alors
        Ecrire EmploisDuTemps2
    SinonSi MeteoJour == I Alors
        Ecrire EmploisDuTemps3
    FinSi
Fin

2.Ecrire cet algorithme en Python.
"""
MeteoBonne = "B"
Meteobonne = "b" 
MeteoMauva = "M"
Meteomauva = "m"
MeteoInter = "I"
Meteointer = "i"
Meteo = input ("Quelle est la météo du jour ? (B)onne (M)auvaise (I)ntermédiaire ?")
if Meteo == MeteoBonne or Meteo == Meteobonne:
    print ("La Méteo est bonne:\n-07h00-10h00 TACHES AGRICOLES\n-10H00-12H00 TACHES AGRICOLES\n- Pause Déjeuner -\n-13H00-15H00 TACHES AGRICOLES\n-15H00-18H00 TACHES AGRICOLES")
elif Meteo == MeteoMauva or Meteo == Meteomauva:
    print ("La Méteo est mauvaise:\n-09h00-10h00 TACHES SOUS HABRIT\n-10H00-12H00 TACHES ADMINISTRATIVES\n- Pause Déjeuner -\n-14H00-15H00 TACHES SOUS HABRIT\n-15H00-16H00 TACHES SOUS HABRIT")
elif Meteo == MeteoInter or Meteo == Meteointer:
    print ("La Méteo est intemédiaire:\n-08h00-10h00 TACHES SOUS HABRIT\n-10H00-12H00 TACHES AGRICOLES\n- Pause Déjeuner -\n-13H00-15H00 TACHES AGRICOLES\n-15H00-17H00 TACHES SOUS HABRIT")
else:
    print ("Veuillez Saisir B, M ou I...")

