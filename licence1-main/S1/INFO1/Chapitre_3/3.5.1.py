def factorielle(n: int):
    m = 1
    for i in range(1,n+1):
        m = (i * m)
    return m
        

# print(factorielle(10))


def factorielle2(r):
    for i in range(r+1):
        m = factorielle(i)
        print(i,m)
        
      
print(factorielle2(25))
