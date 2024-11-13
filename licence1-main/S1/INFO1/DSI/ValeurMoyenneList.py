
L = [2.5 ,5.7 ,6.8 ,7.3 ,8.5 ,9.5 ,13.6 ,15.7]

def MoyenneList(L):
    total = 0
    for elt in L:
        total = total + elt
    return total / len(L)

print(MoyenneList(L))

def ValeurMoyenneList(L):
    L2 = []
    for elt in L: 
        if elt >= MoyenneList(L):
            L2.append(elt)
    return L2

print(ValeurMoyenneList(L))