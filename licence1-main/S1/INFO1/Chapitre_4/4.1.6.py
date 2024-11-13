L1 = [10]*5
L2 = [10]*5


def sommeListe(L1: list, L2: list):
    L3 = [0]*len(L1)
    for i in range(len(L1)):
        L3[i] = L1[i] + L2[i]
    return L3

print(sommeListe(L1,L2))
        
    
