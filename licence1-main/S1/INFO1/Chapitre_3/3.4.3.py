P = 285

def photocoPrix(n: int):
    p1 = 0
    p2 = 0
    p3 = 0
    if n <= 10: 
        p1 = p1 + n
    elif n <= 30:
        p1 = 10
        p2 = p2 + n - 10 
    else:
        p1 = 10
        p2 = 20
        p3 = p3 + n - 30
    return (p1*20)+(p2*15)+(p3*10)

def convertoPrix(n):
    prix = photocoPrix(n)
    euro = prix // 100
    cents = prix % 100
    return euro,cents

print(photocoPrix(P))
print(convertoPrix(P))
