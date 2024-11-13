L = list(range(-50,50+1))
print(L)
print(" ")
print(" ")

# def absListe(L: list):
#     for i in L:
#         s = (i**2)**0.5
#         L[i] = int(s)
#     return L

# print(absListe(L))


def absListe2(L: list):
    for i in range(len(L)):
        L[i] = int((L[i]*L[i])**0.5)
    return L

print(absListe2(L))
