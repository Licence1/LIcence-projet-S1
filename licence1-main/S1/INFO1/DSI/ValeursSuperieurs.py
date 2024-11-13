def ValeurSuperieur(L,a):
    L2 = []
    for elt in range(len(L)):
        if a <= L[elt]:
            L2.append(L[elt])
    return L2

print(ValeurSuperieur([12.4, 34.7, 54.6, 65.7, 76.99],99))
