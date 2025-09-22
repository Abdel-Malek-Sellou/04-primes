
"""
Module de détection de nombres premiers.

Ce module fournit une fonction pour vérifier si un nombre est premier.
"""

def isprime(p):
    """
    Vérifie si un nombre est premier (version ultra-optimisée).
    """
    if p < 2:
        return False
    if p == 2:
        return True
    if p % 2 == 0:  # Éliminer les nombres pairs (sauf 2)
        return False
    # Tester seulement les diviseurs impairs jusqu'à √p
    d = 3
    while d * d <= p:
        if p % d == 0:
            return False
        d += 2  # Sauter les nombres pairs
    return True
 #### Fonction principale

def main():
    """
    Tout simplement la fonction main.
    """

    # vos appels à la fonction secondaire ici

    for n in range(100):
        if isprime(n):
            print(n, end=", ")

    print()


if __name__ == "__main__":
    main()
