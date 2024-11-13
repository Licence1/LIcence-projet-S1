from bibimages import *

monImage = nouvelleImage(300, 300)
c = (255,100,0)
d = 20

def ligneHorizontale(img, c, y):
    l = largeurImage(img)
    h = hauteurImage(img)
    for x in range(l):
        colorierPixel(img, x, y, c)
        
def grilleHorizontale(img, c, d):
    l = largeurImage(img)
    h = hauteurImage(img)
    y = 0 
    for yo in range(0,h,d):
        ligneHorizontale(img, c, yo)

grilleHorizontale(monImage,c ,d)
afficherImage(monImage)
