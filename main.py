"""
Module de détection de nombres premiers.

Ce module fournit une fonction pour vérifier si un nombre est premier.
"""


def isprime(p):
    """
    Vérifie si un nombre est premier.
    
    Un nombre premier est un nombre naturel supérieur à 1 qui n'a pas de 
    diviseurs positifs autres que 1 et lui-même.
    
    Args:
        p (int): Le nombre à vérifier pour la primalité
        
    Returns:
        bool: True si le nombre est premier, False sinon
        
    Exemples:
        >>> isprime(7)
        True
        >>> isprime(10)
        False
        >>> isprime(1)
        False
    """
    d = 2
    ispremier = True
    while d < p:
        if p % d == 0:
            ispremier = False
        d += 1
    return ispremier
