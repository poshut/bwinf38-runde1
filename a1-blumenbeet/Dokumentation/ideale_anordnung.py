def ideale_anordnung(grundfarben, anzahl_farben, regeln):
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