a = "chemise"
b = "e"



def IndicePremiereOccurrence(a: str, b: str):
    for elt in range(len(a)):
        if a[elt] == b:
            return elt
    return -1
    
print(IndicePremiereOccurrence(a, b))

def IndiceDerniereOccurence(a :str, b :str):
    indice = -1
    for elt in range(len(a)):
        if a[elt] == b:
            indice = elt
    return indice

print(IndiceDerniereOccurence(a, b))

            
def SousChaine(a :str, b :str):
    d = IndicePremiereOccurrence(a, b)
    f = IndiceDerniereOccurence(a, b)
    result = ""
    for elt in range(d,f+1):
        result = result + a[elt]
    return result

print(SousChaine(a, b))
