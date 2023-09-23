"""
    Ce programme affichera "Bienvenue" si le nom d'utilisateur est soit Christophe ou John.
    Sinon il affichera "Utilisateur inconnu".
"""

username = "Christophe"


if username == "Christophe":
    print("Bienvenue")
elif username == "John":
    print("Bienvenue")
else:
    print("Utilisateur inconnu")


if username == "Christophe":
    print("Bienvenue")
else:
    if username == "John":
        print("Bienvenue")
    else:
        print("Utilisateur inconnu")





