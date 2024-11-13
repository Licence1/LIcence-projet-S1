fond= ouvrirImage("road.jpg")
avantPlan= ouvrirImage("personnage.png")

def copieCoinImage(avantPlan, fond):
    L= largeurImage(avantPlan)
    H= hauteurImage(avantPlan)
    for x in range(L):
        for y in range(H):
            (r,g,b)=couleurPixel(avantPlan ,x, y)
            if (r,g,b)!=(0,255,0):
                colorierPixel(fond,x,y,(r,g,b))
            
copieCoinImage(avantPlan, fond)  
afficherImage(fond)
