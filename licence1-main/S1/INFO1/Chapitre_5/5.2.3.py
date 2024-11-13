from bibimages import *

monImage = nouvelleImage(300, 300)
c = (255,100,0)
y = 100

def ligneHorizontaleAuMilieu(monImage, c, y):
    l = largeurImage(monImage)
    h = hauteurImage(monImage)
    for x in range(l):
        colorierPixel(monImage, x, y, c)

ligneHorizontaleAuMilieu(monImage, c, y)
afficherImage(monImage)
