def somme_diviseurs(nombre):
    somme = 0
    for diviseur in range(1, nombre // 2 + 1):
        if nombre % diviseur == 0:
            somme += diviseur
    return somme

def sont_amis(M, N):
    return somme_diviseurs(M) == N and somme_diviseurs(N) == M

# Programme principal
if __name__ == "__main__":
    try:
        M = int(input("Entrez un entier M : "))
        N = int(input("Entrez un entier N : "))

        if sont_amis(M, N):
            print(f"{M} et {N} sont des nombres amis.")
        else:
            print(f"{M} et {N} ne sont pas des nombres amis.")
    except ValueError:
        print("Veuillez entrer des entiers valides.")