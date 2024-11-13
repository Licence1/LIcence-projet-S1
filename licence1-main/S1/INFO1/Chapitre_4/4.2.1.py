# Exercice 4.2.1 Écrire une fonction inverseListe(L: list) qui "inverse" l’ordre de la liste :
# elle crée une nouvelle liste dont le premier élément est le dernier de L, le deuxième est 
# l’avantdernier de L, etc. jusqu’au dernier élément qui est le premier de L.

L1 = list(range(0,101,2))


def inverseList(L1: list):
    L1.reverse()
    L2 = [0]*len(L1)
    for i in range(len(L1)):
        L2[i] = L1[i]
    return L2 
        
print(L1)
print(inverseList(L1))