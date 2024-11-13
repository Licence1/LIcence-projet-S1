import math

L = [1,2,3,4,5]
def sommeList(L):
    s = 0
    for elt in L: 
        s = s + elt
    return s
    
print(sommeList(L))

# #2.3.1
# def produit(a,x):
#     s = 0 
#     for i in range(a):
#         s = s + x
#     return s

# a = 7
# x = 6
# print(produit(a,x))

# #2.3.2.1
# n = 89215
# L = list(range(1,n+1))

def sommeCarreListe(L):
    x = 0 
    for E in L:
        y = E * E
        x = x + y
    return x

print(sommeCarreListe(L))
 
# # 2.3.2.2

M = [8,8,8,12,12,12]


def ecartType(M):
    n = len(M)
    x = sommeList(M)
    y = sommeCarreListe(M)
    return math.sqrt((y/n)-(x/n)**2)
    
print(ecartType(M))


# def ecartType(L):
    