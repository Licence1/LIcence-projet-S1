# def nombrePrimes(n):
#     """renvoie la liste des nombres premiers <= n """
#     L = []
#     for k in range (2,n+1):
#         is_prime = True
#         for i in range(2,k):
#             if k%i == 0:
#                 is_prime = False
#         if is_prime:
#             L.append(k)
#     return L
            
# print(nombrePrimes(100))


def nombrePrimes2(n):
    """renvoie la liste des nombres premiers <= n """
    L = []
    for k in range (2,n+1):
        is_prime = True
        for i in range(2,int(k**0.5+1)):
            if k%i == 0:
                is_prime = False
        if is_prime:
            L.append(k)
    return L
            
print(nombrePrimes2(100000))
