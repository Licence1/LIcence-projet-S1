from bibimages import *


monImage = nouvelleImage (300,300)


def ligneHorizontaleBlancheAuMilieu(monImage):
    l = largeurImage(monImage)
    h = hauteurImage(monImage)
    for x in range(l):
        colorierPixel(monImage, x, h//2, (255,255,2555))


ligneHorizontaleBlancheAuMilieu(monImage)
afficherImage(monImage)
