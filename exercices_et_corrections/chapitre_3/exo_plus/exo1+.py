"""
Exo 1:

L’entrée dans un musée privé dépend de l’âge des visiteurs:
le prix sans réduction est de 8 euros et 50 centimes.
Un enfant de moins de 12 ans ne paie pas.
Pour un jeune de moins de 18 ans, il y a une réduction de 12%.
Les autres paient le plein tarif.
"""
Tarif = 8.5  #définir "Tarif" le Tarif Normal (8€50 pour l'exercice)
Gratuit = 12 # définir "Gratuit" pour moins de quel âge ? (12 ans pour l'exrcice) 
AgeReduc = 21 # définir "AgeReduc" l'age de réduction tarifaire (18 ans pour l'exercice)
PcentReduc = 12 # définir "PcentReduc" (12% pour l'exercice) le % de réduction pour les gens compris entre "Gratuit" et "AgeReduc"

TarifReduit = Tarif - (Tarif*PcentReduc/100)
print ("Bienvenue au musée de l'informatique!\nLes tarifs sont les suivants:\n-",AgeReduc,"ans et + :",Tarif,"€\n- Moins de",AgeReduc,"ans :",TarifReduit,"€ (soit",PcentReduc,"% de réduction)\n- Moins de",Gratuit,"ans : GRATUIT !\n")
print ("Combien d'adultes êtes vous ? (+ de",AgeReduc,"ans)")
Adultes = input()
Adultes = int (Adultes)
print ("Combien y'a t'il de personnes de plus de",Gratuit,"et moins de",AgeReduc,"ans ?")
Ados = input()
Ados = int (Ados)
print ("Et combien de moins de",Gratuit,"ans ?")
Enfants = input()
Enfants = int (Enfants)
TotalAdults=Tarif*Adultes
TotalAdos=TarifReduit*Ados
NbreEntrees=Adultes+Ados+Enfants
TotalPayer=TotalAdults+TotalAdos
print ("Le montant à payer pour:\n-",Adultes,"adulte(s) =",TotalAdults,"€\n-",Ados,"entre",Gratuit,"et",AgeReduc,"ans =",TotalAdos,"€\n-",Enfants,"de moins de",Gratuit,"ans = GRATUIT")
print ("Soit un montant total à règler de",TotalPayer,"€ pour",NbreEntrees,"personne(s)")

