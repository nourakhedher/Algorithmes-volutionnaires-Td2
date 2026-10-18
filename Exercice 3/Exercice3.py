import random
import math

I = 10000
d = [[0, 14, 15, I, I, I, I, 17],
     [14, 0, 13, 14, 20, I, I, 21],
     [15, 13, 0, 11, 21, 17, 9, 9],
     [I, 14, 11, 0, 11, 10, 8, 20],
     [I, 20, 21, 11, 0, 15, 18, I],
     [I, I, 17, 10, 15, 0, 9, I],
     [I, I, 9, 8, 18, 9, 0, 13],
     [17, 21, 9, 20, I, I, 13, 0]]
n = 8


def cout(t):
    total = 0
    for i in range(n):
        total += d[t[i]][t[(i + 1) % n]]
    return total


def echanger(t, i, j):
    s = t[:]
    s[i], s[j] = s[j], s[i]
    return s


def afficher(nom, t, c):
    k = t.index(0)
    t = t[k:] + t[:k]
    print(nom, [v + 1 for v in t] + [1], "cout =", c)


def taboue():
    x = [0, 1, 2, 3, 4, 5, 6, 7]
    best, best_c = x, cout(x)
    tabou = {}
    for it in range(50):
        choix, choix_c, mv = None, 10 ** 9, None
        for i in range(1, n):
            for j in range(i + 1, n):
                y = echanger(x, i, j)
                c = cout(y)
                if tabou.get((i, j), -1) > it and c >= best_c:
                    continue
                if c < choix_c:
                    choix, choix_c, mv = y, c, (i, j)
        x = choix
        tabou[mv] = it + 5
        if choix_c < best_c:
            best, best_c = x, choix_c
    return best, best_c


def recuit():
    x = [0, 1, 2, 3, 4, 5, 6, 7]
    best, best_c = x, cout(x)
    T = 30
    for it in range(5):
        for k in range(20):
            i, j = random.sample(range(1, n), 2)
            y = echanger(x, i, j)
            delta = cout(y) - cout(x)
            if delta < 0 or random.random() < math.exp(-delta / T):
                x = y
            if cout(x) < best_c:
                best, best_c = x, cout(x)
        T = T * 0.5
    return best, best_c


def genetique():
    pop = []
    for k in range(30):
        t = [0, 1, 2, 3, 4, 5, 6, 7]
        random.shuffle(t)
        pop.append(t)
    for g in range(100):
        pop.sort(key=cout)
        nouvelle = pop[:2]
        while len(nouvelle) < 30:
            p1 = min(random.sample(pop, 3), key=cout)
            p2 = min(random.sample(pop, 3), key=cout)
            cut = random.randint(1, n - 1)
            enfant = p1[:cut]
            for v in p2:
                if v not in enfant:
                    enfant.append(v)
            if random.random() < 0.2:
                i, j = random.sample(range(n), 2)
                enfant = echanger(enfant, i, j)
            nouvelle.append(enfant)
        pop = nouvelle
    best = min(pop, key=cout)
    return best, cout(best)


t, c = taboue()
afficher("Taboue:", t, c)
t, c = recuit()
afficher("Recuit:", t, c)
t, c = genetique()
afficher("Genetique:", t, c)
