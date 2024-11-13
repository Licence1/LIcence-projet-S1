#Exercice 1.4.2 Écrire une fonction abs2(x) qui retourne la valeur absolue de x. Attention :
#bien nommer cette fonction abs2, et non abs, car la fonction abs est prédéfinie en python
import math

a = -184

def abs2(a):
    x = math.sqrt(a*a)
    return int(x)

print(f"La valeur absolue de {a} est {abs2(a)}")
