L = [1,2,3,4,7,9,5,9,0]

def listeVersEntiers(L: list):
    result = 0
    L.reverse()
    for i in range(len(L)):
        l = L[i]*(10**i)
        result = result + l
    return result

print(listeVersEntiers(L))