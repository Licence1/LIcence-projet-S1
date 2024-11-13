from bibimages import *

img = ouvrirImage("teapot.png")

def modifierLuminosité(img,facteur: float):
    L = largeurImage(img)
    H = hauteurImage(img)
    for x in range(L):
        for y in range(H):
            (r, g, b) = couleurPixel(img, x, y)
            r = int(facteur * r)
            b = int(facteur * b)
            g = int(facteur * g)
            colorierPixel(img, x, y, (r, g, b))
modifierLuminosité(img, 0.5)
afficherImage(img)
            
