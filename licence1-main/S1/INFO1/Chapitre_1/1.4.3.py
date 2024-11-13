#Exercice 1.4.3 Écrire une fonction nbJours(mois) qui reçoit en paramètre le numéro d’un
#mois et qui renvoie le nombre de jours de ce mois (sans tenir compte des années bisextiles).
#Note : éviter de traiter un par un chacun des 12 cas ! :

mois = 2
   
def nbjours(mois):
    if mois == 2:
        nj = 28
        return nj
    if mois % 2 != 0:
        nj = 31
        return nj
    if mois > 12 or mois < 0:
        nj = 0
        return nj
    else:
        nj = 30
        return nj
    
    
print(f"ce mois à {nbjours(mois)} jours")
