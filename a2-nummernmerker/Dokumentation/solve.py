def loesen(nummer):
    if nummer in cache:
        return cache[nummer]

    if len(nummer) == 0:
        return [], 0
    elif len(nummer) == 1:
        return [], math.inf

    bloecke, nullen = loesen(nummer[2:])
    laenge = 2

    if len(nummer) >= 3:
        bloecke3, nullen3 = loesen(nummer[3:])
        if nullen3 <= nullen:
            bloecke = bloecke3
            nullen = nullen3
            laenge = 3

    if len(nummer) >= 4:
        bloecke4, nullen4 = loesen(nummer[4:])
        if nullen4 <= nullen:
            bloecke = bloecke4
            nullen = nullen4
            laenge = 4
    
    if nummer[0] == '0':
        nullen += 1
    
    bloecke = [nummer[:laenge]] + bloecke
    cache[nummer] = (bloecke, nullen)
    return bloecke, nullen