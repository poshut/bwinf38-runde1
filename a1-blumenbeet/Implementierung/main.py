import sys
import itertools
import math

FARBEN = [
    'blau',
    'gelb',
    'gruen',
    'orange',
    'rosa',
    'rot',
    'tuerkis'
]

def farben_bestimmen(anzahl_farben, regeln):
    farben = set()
    for regel in regeln:
        farben.add(regel[0])
        farben.add(regel[1])
    
    for farbe in FARBEN:
        if len(farben) >= anzahl_farben:
            break;
        farben.add(farbe)

    return list(itertools.combinations(farben, anzahl_farben))

def aufstellung_bewerten(a, regeln):
    score = 0
    score += regeln.get((a[0],a[1]),0)
    score += regeln.get((a[0],a[2]),0)
    score += regeln.get((a[1],a[2]),0)
    score += regeln.get((a[1],a[3]),0)
    score += regeln.get((a[1],a[4]),0)
    score += regeln.get((a[2],a[4]),0)
    score += regeln.get((a[2],a[5]),0)
    score += regeln.get((a[3],a[4]),0)
    score += regeln.get((a[4],a[5]),0)
    score += regeln.get((a[3],a[6]),0)
    score += regeln.get((a[4],a[6]),0)
    score += regeln.get((a[4],a[7]),0)
    score += regeln.get((a[5],a[7]),0)
    score += regeln.get((a[6],a[7]),0)
    score += regeln.get((a[6],a[8]),0)
    score += regeln.get((a[7],a[8]),0)
    return score

def alle_kombinationen(farben, anzahl_farben, regeln):
    score = -math.inf
    comb = None
    i = 0
    for f in itertools.product(farben, repeat=9):
        i += 1
        if i % 1000000 == 0:
            print("tried", str(i / 1000000) + "M", "permutations")
        if len(set(f)) < anzahl_farben:
            continue
        s = aufstellung_bewerten(f, regeln)
        if s > score:
            comb = f
            score = s
    return comb, score

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("Benutzung: " + sys.argv[0] + " <Eingabedatei>", file=sys.stderr)
        exit(1)

    with open(sys.argv[1]) as f:
        zeilen = f.read().split("\n")
    
    anzahl_farben = int(zeilen[0])
    regeln = {}
    for zeile in zeilen[2:]:
        zeile = list(filter(None, zeile.split(" ")))
        if len(zeile) != 0:
            regeln[(zeile[0], zeile[1])] = int(zeile[2])
            regeln[(zeile[1], zeile[0])] = int(zeile[2])

    score = -math.inf
    comb = None
    for farben in farben_bestimmen(anzahl_farben, regeln):
        print("probing", farben)
        c, s = alle_kombinationen(farben, anzahl_farben, regeln)
        if s > score:
            score = s
            comb = c
    print(comb, score)