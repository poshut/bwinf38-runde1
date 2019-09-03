import math
import sys

cache = {}

def solve(nummer):
    if nummer in cache:
        return cache[nummer]

    if len(nummer) == 0:
        return [], 0
    elif len(nummer) == 1:
        return [], math.inf

    bloecke, nullen = solve(nummer[2:])
    laenge = 2

    if len(nummer) >= 3:
        bloecke3, nullen3 = solve(nummer[3:])
        if nullen3 <= nullen:
            bloecke = bloecke3
            nullen = nullen3
            laenge = 3

    if len(nummer) >= 4:
        bloecke4, nullen4 = solve(nummer[4:])
        if nullen4 <= nullen:
            bloecke = bloecke4
            nullen = nullen4
            laenge = 4
    
    if nummer[0] == '0':
        nullen += 1
    
    bloecke = [nummer[:laenge]] + bloecke
    cache[nummer] = (bloecke, nullen)
    return bloecke, nullen

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("Benutzung: " + sys.argv[0] + " <zahl>", file=sys.stderr)
        exit(1)

    bloecke, nullen = solve(sys.argv[1])
    print("Die Blöcke, die sich Sarahs Mutter merken muss, sind:", ' '.join(bloecke))
    print(nullen, "von", len(bloecke), "Blöcken fangen mit 0 an.")






