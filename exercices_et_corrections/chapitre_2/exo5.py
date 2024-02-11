#################################################################
#               Author: Ismael Maurice                          #
#               Language: Python                                #
#               Chapter 2                                       #
#               File: exo5.py                                   #
#################################################################

"""
    Objectifs: Quelles seront les valeurs des variables A et B après exécution des instructions suivantes ?

    DEBUT
     Variables A, B en Entiers
     A <- 5
     B <- 2
     A <- B
     B <- A
    FIN

    Les deux dernières instructions permettent-elles d’échanger les deux valeurs de B et A ? Si l’on inverse
    les deux dernières instructions, cela change-t-il quelque chose ?
"""

A = 5
B = 2
A = B
B = A
# Non çà ne change pas les valeurs des deux variables
print ("1.Non çà ne change pas les valeurs des deux variables\nValeur A =", A, "\nValeur B =", B)
A = 5
B = 2
B = A
A = B
# Oui celà change la valeur des variables
print ("2.Oui celà change la valeur des variables\nValeur A =", A, "\nValeur B =", B)