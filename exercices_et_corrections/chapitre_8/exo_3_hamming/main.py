#################################################################
#               Author: Ismael Maurice                          #
#               Language: Python                                #
#               Chapter 8                                       #
#               File: exo_3_hamming.py                          #
#################################################################

"""
    La distance de Hamming entre deux mots de même longueur est le nombre d’endroits où les lettres sont différentes.

    Par exemple: 𝑆𝐴𝑉𝑂𝑁 et J𝐴𝑃𝑂𝑁 ont 𝑝𝑜𝑢𝑟 𝑑𝑖𝑠𝑡𝑎𝑛𝑐𝑒 𝑑𝑒 𝐻𝑎𝑚𝑚𝑖𝑛𝑔 2
    Car la première lettre de Japon est différente de la première lettre de Savon, les troisièmes lettres aussi sont différentes.

    Ecrire un programme qui demande à l’utilisateur deux mots de mêmes longueurs et ensuite affiche la distance de Hamming entre les deux mots.
    Attention on ne doit pas tenir compte des majuscules et des minuscules Japon, SAVON doit donner comme distance de Hamming 2.
    Afficher un message d’erreur si l’utilisateur fournir une chaine vide ou des mots de longueurs différentes.

    Le calcul de la valeur de Hamming doit être effectué dans une fonction qui prend en paramètre deux mots et renvoie un entier qui correspond à la distance de Hamming.
"""

# TODO: Ecrire le code en python ci dessous