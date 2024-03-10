import string

caracteres = list(string.ascii_letters)
taille = len(caracteres)

def chiffrer(message, secret):
    messageChiffre = ""
    for c in message:
        if c != " ":
            pos = caracteres.index(c)
            posCaractere = abs(pos + secret) % taille
            messageChiffre += caracteres[posCaractere]
        else:
            messageChiffre += " "
    return messageChiffre

def dechiffrer(message, secret):
    messageChiffre = ""
    for c in message:
        if c != " ":
            pos = caracteres.index(c)
            posCaractere = abs(pos - secret) % taille
            messageChiffre += caracteres[posCaractere]
        else:
            messageChiffre += " "
    return messageChiffre

print("Voulez vous chiffrer ou déchiffrer ?\n1. Chiffrer\n2. Déchiffrer")
choix = input("Entrer le numéro de votre choix:")
choix = int(choix)
if choix == 1:
    message = input("Entrer le message à chiffrer:")
    secret = input(f"Entrer le secret entre 1 et {len(caracteres)}:")
    secret = int(secret)
    messageCh = chiffrer(message, secret)
    print(messageCh)
else:
    message = input("Entrer le message à déchiffrer:")
    secret = input(f"Entrer le secret entre 1 et {len(caracteres)}:")
    secret = int(secret)
    messageCh = dechiffrer(message, secret)
    print(messageCh)