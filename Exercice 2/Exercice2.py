import random

# couts D1 -> M1, M2, M3
# couts D2 -> M1, M2, M3
cout = [[5, 3, 4],
        [6, 7, 2]]
offre = [8, 9]
demande = [4, 5, 8]

def cout_total(x):
    total = 0
    for i in range(2):
        for j in range(3):
            total += cout[i][j] * x[i][j]
    return total

def solution_initiale_aleatoire():
    d = demande.copy()
    x = [[0, 0, 0], [0, 0, 0]]
    for i in range(2):
        reste = offre[i]
        while reste > 0:
            j = random.randint(0, 2)
            if d[j] > 0:
                q = min(reste, d[j])
                x[i][j] += q
                reste -= q
                d[j] -= q
    return x

def voisins(x):
    for i1 in range(2):
        for i2 in range(2):
            if i1 == i2:
                continue
            for j1 in range(3):
                for j2 in range(3):
                    if j1 != j2 and x[i1][j1] >= 1 and x[i2][j2] >= 1:
                        y = [r[:] for r in x]
                        y[i1][j1] -= 1
                        y[i1][j2] += 1
                        y[i2][j2] -= 1
                        y[i2][j1] += 1
                        yield (j1, j2), y

def recherche_taboue(max_iter=30, tenure=3):
    x = solution_initiale_aleatoire()
    meilleur, meilleur_cout = x, cout_total(x)
    tabou = {}

    for it in range(max_iter):
        choix, choix_cout, choix_mv = None, float("inf"), None
        for mv, y in voisins(x):
            c = cout_total(y)
            if tabou.get(mv, -1) > it and c >= meilleur_cout:
                continue
            if c < choix_cout:
                choix, choix_cout, choix_mv = y, c, mv
        if choix is None:
            break
        x = choix
        j1, j2 = choix_mv
        tabou[(j2, j1)] = it + tenure
        if choix_cout < meilleur_cout:
            meilleur, meilleur_cout = x, choix_cout

    return meilleur, meilleur_cout


x, c = recherche_taboue()
print("D1 ->", x[0])
print("D2 ->", x[1])
print("Cout minimal =", c)
