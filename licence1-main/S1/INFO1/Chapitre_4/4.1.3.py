L = [1,2,3,4,5,-1,-5,-9,-7]*3
L2 = list(range(len(L)-1))
x = 4

def positionDernier(L: list,x: int):
    s=-1
    for i in range(len(L)):
        if L[i] == x: 
            s = i
    return s 
print(positionDernier(L,x))


# print(L)
# print(list(range(len(L)-1)))
            
