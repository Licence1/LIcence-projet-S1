for j in range(10):
    print(j, j * j)
    
print("     ")

for k in range(3,8):
    print (k,2 * k + 1)
    
print("     ")

for k in range(3, 9, 2):
    print(k)
    
print("     ")
    
for i in range(10):
    print("bonjour")
    

print("     ")

    
for a in [10,11,12]:
    for b in [1,2,3]:
        print (a,b)
        
print("     ")

u = [2,6,1,10,6]
v = [2,5,6,4]

for x in u :
    for y in v:
        print(x, y, x + y, x == y)
        
def mystere(n):
    s = 0 
    for i in range (1, n+1):
        s = s + i
    return s 

print(mystere(2))
print(mystere(3))
print(mystere(4))

def sommeCarre(n):
    s = 0
    for i in range(1, n+1) :
        n = i * i
        s = s + n
    return s

print(sommeCarre(5))




