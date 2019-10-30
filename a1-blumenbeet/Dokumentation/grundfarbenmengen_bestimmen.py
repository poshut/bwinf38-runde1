def grundfarbenmengen_bestimmen(anzahl_farben, regeln):
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