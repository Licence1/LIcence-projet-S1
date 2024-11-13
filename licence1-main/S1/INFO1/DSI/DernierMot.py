t = "Hello World of Destruction Machine"
s = reversed(t)


def DernierMot(s):
    pm = ""
    for i in s:
        pm = pm + i
        if i == " ":
            return pm[::-1]

print(DernierMot(s))


#Compléxité = n