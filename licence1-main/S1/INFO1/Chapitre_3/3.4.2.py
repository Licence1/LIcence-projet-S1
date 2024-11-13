
def uneMinuteEnPlus(h: int,m: int):
    h >= 0 and h >= 23
    if m > 59 or m < 0 or h > 23 or h < 0:
        return False
    if m >= 0 and m < 59:
        m = m + 1
        h = h
    if m == 59:
            m = 00
            h = h + 1
    if h == 24:
        h = 00
    heure = (h,m)
    return heure

print(uneMinuteEnPlus(12,1))

      
def uneMinuteEnPlus1(h: int,m: int):
    if m > 59 or m < 0 or h > 23 or h < 0:
        return False
    if m >= 0 and m < 59:
        m = m + 1
        h = h
    elif m == 59:
            m = 0
            h = h + 1
    if h == 24:
        h = 00
    heure = (h,m)
   
    return (heure)

print(uneMinuteEnPlus1(23,59))


def uneMinuteEnPlus2(h: int,m: int):
    mh = (h,m)
    # h >= 0 and h >= 23
    if m > 59 or m < 0 or h > 23 or h < 0:
        return False
    if h == 23 and m == 59:
        mh = (0,0)
    if mh == (h,59):
        mh = (h+1,00)
    elif mh == (h,m):
        mh = (h,m+1)
    return mh
    
print(uneMinuteEnPlus2(22,59))

