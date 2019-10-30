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