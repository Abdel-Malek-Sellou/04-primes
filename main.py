from math import sqrt

#### Fonction secondaire


def isprime(p):
     d = 2 #on commence par diviser par 2 et on monte petit à petit
    ispremier = True #on part du principe que le nombre est premier jusqu'à preuve du contraire

    while d < p:
        if p % d == 0:
            q = p // d #on définit le quotient pour pouvoir l'appeler dans le print
            ispremier = False #le nombre n'est pas premier
        d += 1
    return(ispremier)

    pass

#### Fonction principale


def main():

    # vos appels à la fonction secondaire ici

    for n in range(100):
        if isprime(n):
            print(n, end=", ")

    print()


if __name__ == "__main__":
    main()
