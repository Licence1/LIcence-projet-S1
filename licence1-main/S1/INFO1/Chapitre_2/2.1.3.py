L = list(range(1,101))
#L = [1,6,189,1,4,6,8,0]

#Moyenne de la liste 
def moyenneListe(L: list):
    s = 0 
    for elt in L:
        s = s + elt
    return s / len(L)

print(f"La moyenne de cette liste est: {moyenneListe(L)}")
print(f"cette liste contient {len(L)} éléments")

#Nombre Pairs
def nbPairsListe(L: list):
    s = 0
    for elt in L:
        if elt % 2 == 0:
                s = s + 1
    return s
    
print(f"Cette liste contient {nbPairsListe(L)} nombres pairs")

#Maximum 

def maximumListe(L: list):
    s = 0
    for elt in L: 
        if elt > s:
            s = elt
    return s

print(f"La valeur maximum de la liste est {maximumListe(L)}.")