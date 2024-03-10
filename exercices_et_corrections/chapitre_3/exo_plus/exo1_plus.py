"""
Exo 1:

L’entrée dans un musée privé dépend de l’âge des visiteurs:
le prix sans réduction est de 8 euros et 50 centimes.
Un enfant de moins de 12 ans ne paie pas.
Pour un jeune de moins de 18 ans, il y a une réduction de 12%.
Les autres paient le plein tarif.
"""
tarifSansReduction = 8.5  #définir "Tarif" le Tarif Normal (8€50 pour l'exercice)
ageGratuit = 12 # définir "Gratuit" pour moins de quel âge ? (12 ans pour l'exrcice)
ageReduc = 18 # définir "ageReduc" l'age de réduction tarifaire (18 ans pour l'exercice)
pourcentageReduc = 12 # définir "pourcentageReduc" (12% pour l'exercice) le % de réduction pour les gens compris entre "Gratuit" et "ageReduc"

tarifReduit = tarifSansReduction - ((tarifSansReduction * pourcentageReduc) / 100)
print ("Bienvenue au musée de l'informatique!\nLes tarifs sont les suivants:\n-", ageReduc, "ans et + :", tarifSansReduction, "€\n- Moins de", ageReduc, "ans :", tarifReduit, "€ (soit", pourcentageReduc,"% de réduction)\n- Moins de", ageGratuit,"ans : GRATUIT !\n")
print ("Combien d'adultes êtes vous ? (+ de", ageReduc, "ans)")
nbAdultes = input()
nbAdultes = int(nbAdultes)
print ("Combien y'a t'il de personnes de plus de", ageGratuit,"et moins de", ageReduc, "ans ?")
nbAdos = input()
nbAdos = int(nbAdos)
print ("Et combien de moins de", ageGratuit, "ans ?")
nbEnfants = input()
nbEnfants = int(nbEnfants)
totalAdults = tarifSansReduction * nbAdultes
totalAdos = tarifReduit * nbAdos
nbreEntrees = nbAdultes + nbAdos + nbEnfants
totalPayer = totalAdults + totalAdos
print ("Le montant à payer pour:\n-", nbAdultes, "adulte(s) =", totalAdults, "€\n-", nbAdos, "entre", ageGratuit, "et", ageReduc, "ans =", totalAdos, "€\n-", nbEnfants, "de moins de", ageGratuit, "ans = GRATUIT")
print ("Soit un montant total à règler de", totalPayer, "€ pour", nbreEntrees, "personne(s)")
