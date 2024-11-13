from bibimages import *

img = ouvrirImage("teapot.png")

def filtreRouge(img):
    L = largeurImage(img)
    H = hauteurImage(img)
    for x in range(L):
        for y in range(H):
            (r, g, b) = couleurPixel(img, x, y)
            colorierPixel(img, x, y, (r, 0, 0))

filtreRouge(img)
afficherImage(img)
