L = [1,3,5,6,9]

def comparaison(s):
    for elt in L:
        if elt == s: 
            return True
    return False

print(comparaison(9))