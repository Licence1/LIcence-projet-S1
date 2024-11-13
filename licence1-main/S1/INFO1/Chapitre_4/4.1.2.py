L = list(range(-10,10))

def position2(L: list,x: int):
    for i in range(len(L)):
        if L[i] == x:
            return i
    return -1

print(position2(L,7))
print(L)



