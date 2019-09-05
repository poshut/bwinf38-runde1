import sys

def parse_tankstelle(s):
    words = s.split(' ')
    words = list(filter(None, words))
    words[0] = int(words[0])
    words[1] = float(words[1])
    return words

def minimize_stops(verbrauch, tankgroesse, fuellung, strecke, tankstellen):
    """
    Diese Funktion berechnet die Mindestanzahl an Tankstellenhalten, der Preis ist hierbei egal.
    """
    stops = 0
    position = 0
    for i,tankstelle in enumerate(tankstellen):
        # Die Tankstelle sollte auf der Strecke liegen
        assert strecke > tankstelle[0]
        # Die neue Fuellung berechnen
        fuellung -= (verbrauch / 100.0) * (tankstelle[0] - position)

        position = tankstelle[0]

        # Die Fuellung berechnen, wenn hier nicht getankt wird und es nicht die letzte Tankstelle ist
        if i != len(tankstellen) - 1:
            fuellung_alternativ = fuellung - (verbrauch / 100.0) * (tankstellen[i+1][0] - position)
            if fuellung_alternativ < 0:
                # Wir muessen tanken!
                stops += 1
                fuellung = tankgroesse
    return stops


if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("Benutzung:", sys.argv[0], "<Eingabedatei>", file=sys.stderr)
        exit(1)
    
    with open(sys.argv[1]) as f:
        zeilen = f.read().split("\n")

    verbrauch = int(zeilen[0])
    tankgroesse = int(zeilen[1])
    fuellung = int(zeilen[2])
    strecke = int(zeilen[3])
    tankstellen = list(map(parse_tankstelle, zeilen[5:-1]))
    print("Verbrauch:" + str(verbrauch), "Größe: " + str(tankgroesse), "Füllung: " + str(fuellung), "Strecke: " + str(strecke), "Tankstellen: " + str(tankstellen), sep='\n')

    print("Es muss mindestens", minimize_stops(verbrauch, tankgroesse, fuellung, strecke, tankstellen), "Mal gehalten werden.")

