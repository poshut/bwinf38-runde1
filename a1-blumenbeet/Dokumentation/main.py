if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("Benutzung: " + sys.argv[0] + " <Eingabedatei>", file=sys.stderr)
        exit(1)

    try:
        with open(sys.argv[1]) as f:
            zeilen = f.read().split("\n")
    except FileNotFoundError:
        print("Eingabedatei nicht gefunden!", file=sys.stderr)
        exit(1)

    
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
    for farben in grundfarbenmengen_bestimmen(anzahl_farben, regeln):
        c, s = ideale_anordnung(farben, anzahl_farben, regeln)
        if s > score:
            score = s
            comb = c

    print("1. Reihe:", comb[0])
    print("2. Reihe:", ', '.join(comb[1:3]))
    print("3. Reihe:", ', '.join(comb[3:6]))
    print("4. Reihe:", ', '.join(comb[6:8]))
    print("5. Reihe:", comb[8])
    print("Diese Aufstellung erhält", score, "Punkte.")