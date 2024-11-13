s = "Hello World my name is paul"

def premierMot(s):
    pm = ""
    for i in s:
        pm = pm + i
        if i == " ":
            return pm
        
print(premierMot(s))


#Compléxité = n