L = [-5,2,9,-5,999,-7]


def maximumListe(L: list):
    s = L[0]
    for elt in L: 
        if elt > s:
            s = elt
    return s

print(f"La valeur maximum de la liste est {maximumListe(L)}.")
