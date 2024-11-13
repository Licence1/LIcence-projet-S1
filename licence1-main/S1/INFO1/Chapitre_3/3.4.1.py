x = 5
y = -9
z = 3

def max3(x: int, y: int, z: int): 
    if x > y and x > z:
        return x
    if y > x and y > z:
        return y
    else:
        return z
    
print(max3(x,y,z))


def max31(x: int, y: int, z: int):
    n = 0
    L = [x,y,z]
    for elt in L:
        if elt > n:
            n = elt
    return n

print(max31(x,y,z))

