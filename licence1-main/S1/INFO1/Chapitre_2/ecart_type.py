import math

M = [8,8,8,12,12,12]

def sommeList(M):
    s = 0
    for elt in M : 
        s = s + elt
    return s
    
print(f"La somme des éléments de la liste est {sommeList(M)}")


def sommeCarreListe(M):
    x = 0 
    for E in M:
        y = E * E
        x = x + y
    return x

print(f"la somme des carrés de cette liste est {sommeCarreListe(M)}")
 

def ecartType(M):
    n = len(M)
    x = sommeList(M)
    y = sommeCarreListe(M)
    return math.sqrt((y/n)-(x/n)**2)
    
print(f"L'ecart type entre les éléments de la liste est {ecartType(M)}")