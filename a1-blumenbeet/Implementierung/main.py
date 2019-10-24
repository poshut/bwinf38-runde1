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

def grundfarben_bestimmen(anzahl_farben, regeln):
    """
    Bestimmt alle möglichen Mengen an Grundfarben, ausgehend von den gegebenen Regeln und der Anzahl der Farben in einer Grundfarbenmenge
    @param anzahl_farben: Anzahl an Grundfarben pro Menge
    """

    # Welche Farben werden in den Regeln erwähnt?
    farben = set()
    for regel in regeln:
        farben.add(regel[0])
        farben.add(regel[1])
    
    # Hinzufügen zusätzlicher Farben, um auf die geforderte Anzahl zu kommen
    for farbe in FARBEN:
        if len(farben) >= anzahl_farben:
            break
        farben.add(farbe)

    # Wenn mehr Farben in den Regeln erscheinen als gefordert sind, sind alle Kombinationen an Farben aus den Regeln Grundfarbenmengen
    return itertools.combinations(farben, anzahl_farben)

def aufstellung_bewerten(a, regeln):
    """
    Bewertet eine Aufstellung mit den gegebenen Regeln
    @param a: Aufstellung als Liste an Farben
    @param regeln: dict mit Tupeln zweier Farben als Schlüssel und der Punktzahl als Wert
    """
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

def alle_kombinationen(grundfarben, anzahl_farben, regeln):
    """
    Bestimmt die beste Anordnung der gegebenen Grundfarben mit der gegebenen Anzahl an Farben und den gegebenen Regeln
    @param grundfarben: Die Grundfarben, deren Anordnung bestimmt werden soll (als Liste)
    @param anzahl_farben: Anzahl an verschiedenen Farben in der zu bestimmenden Anordnung
    @param regeln: dict mit Tupeln zweier Farben als Schlüssel und der Punktzahl als Wert
    """
    score = -math.inf
    comb = None
    for f in itertools.product(grundfarben, repeat=9):

        # Sind genürgend Farben in der Anordnung?
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
    
    # Anzahl der Farben und Regeln aus der Eingabedatei lesen
    anzahl_farben = int(zeilen[0])
    regeln = {}
    for zeile in zeilen[2:]:
        zeile = list(filter(None, zeile.split(" ")))
        if len(zeile) != 0:
            regeln[(zeile[0], zeile[1])] = int(zeile[2])
            regeln[(zeile[1], zeile[0])] = int(zeile[2])

    score = -math.inf
    comb = None

    # Für jede Grundfarbenmenge die ideale Anordnung bestimmen und die beste verwenden
    for farben in grundfarben_bestimmen(anzahl_farben, regeln):
        print("probing", farben)
        c, s = alle_kombinationen(farben, anzahl_farben, regeln)
        if s > score:
            score = s
            comb = c

    print(comb, score)