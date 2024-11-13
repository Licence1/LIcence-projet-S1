from bibimages import *

monImage = nouvelleImage(300, 300)
c = (255,100,0)

def ligneHorizontaleAuMilieu(monImage, c):
    l = largeurImage(monImage)
    h = hauteurImage(monImage)
    for x in range(l):
        colorierPixel(monImage, x, h//2, c)

ligneHorizontaleAuMilieu(monImage, c)
afficherImage(monImage)
