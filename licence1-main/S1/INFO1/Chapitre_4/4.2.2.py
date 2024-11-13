# Exercice 4.2.2 Écrire une fonction alterne(L1: list, L2: list) 
# -> list qui, étant données deux listes L1 et L2 supposées de même taille,
# construit une liste deux fois plus grande,contenant l’alternance des éléments de L1 et de L2.

# L1 = list(range(1,101,2))
# L2 = list(range(1,101,2))

L1 = [1,1,1,1]
L2 = [2,2,2,2]

print(len(L1))
print(len(L2))

def listAlterne(L1: list, L2: list):
    L3 = []*(len(L1)+len(L2))
    for i in range(len(L1)):
        L3.append(L1[i])
        L3.append(L2[i])
    return L3
    
    
print(listAlterne(L1, L2))

