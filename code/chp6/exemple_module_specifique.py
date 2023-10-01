Python 3.11.4 (tags/v3.11.4:d2340ef, Jun  7 2023, 05:45:37) [MSC v.1934 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> 
>>> # Import avec espace de nom par défaut
>>> import math
>>> help(math.pow)
Help on built-in function pow in module math:

pow(x, y, /)
    Return x**y (x to the power of y).

>>> # Import avec espace de nom spécifique
>>> import math as mathematique
>>> help(mathematique.pow)
Help on built-in function pow in module math:

pow(x, y, /)
    Return x**y (x to the power of y).

>>> # Import avec espace de nom par défaut
>>> import math
>>> help(math.pow)
Help on built-in function pow in module math:

pow(x, y, /)
    Return x**y (x to the power of y).

>>> math.pow(2,2)
4.0
>>> 
>>> 
>>> 
>>> # Import avec espace de nom spécifique
>>> import math as mathematique
>>> help(mathematique.pow)
Help on built-in function pow in module math:

pow(x, y, /)
    Return x**y (x to the power of y).

>>> mathematique.pow(2,2)
4.0
