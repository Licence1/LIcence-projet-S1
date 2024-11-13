from bibimages import *

monImage = nouvelleImage(1000, 1000 )
x1 = 50
x2 = 100
y1 = 150
y2 = 200
c = (255.255.255)

def ligneHorizontal(img, x1: int, y1: int, x2: int, y2: int):
    l = largeurImage(img)
    h = hauteurImage(img)
    for x in range(l):
        colorierPixel(img, x2-x1, y2-y1, c)
        
ligneHorizontal(monImage,x1,y1,x2,y2)
afficherImage(monImage)

# def rectangleCreux
