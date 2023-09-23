
"""
    Ce programme demandera le nom d'utilisateur
    tant que celui-ci n'est pas Christophe
    sinon affiche le message de Bienvenue. 
"""

# On demande une première fois le nom d'utilisateur
username = input("Entrer votre nom d'utilisateur:")

# On boucle tant que le nom d'utilisateur n'est pas égal à celui attendu
while username != "Christophe":
    # Affichage du message nom d'utilisateur incorrect
    print("Nom d'utilisateur incorrect !")
    # Demander encore le nom d'utilisateur
    username = input("Entrer votre nom d'utilisateur:")

# Instruction qui s'exécutera quand on sortira de la boucle
print("Bienvenue", username) # affichera Bienvenue nom_utilisateur




