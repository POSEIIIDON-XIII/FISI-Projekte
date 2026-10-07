def dezimal_zu_binaer(zahl):
    if zahl == 0:
        return "0"

    reste = []

    while zahl > 0:
        reste.append(zahl % 2)
        zahl = zahl // 2

    binaer = []
    reste.reverse()
    for jede_ziffer in reste:
        binaer.append(str(jede_ziffer))

    binaer_string = "".join(binaer)
    return binaer_string



def binaer_formatieren(binaer_string):
    if binaer_string == "0":
        return binaer_string

    laenge_binaer_string = len(binaer_string)
    rest_binaer_string = laenge_binaer_string % 4

    if rest_binaer_string == 0:
        fehlende_nullen = 0
    else:
        fehlende_nullen = 4 - rest_binaer_string

    binaer_ergebnis = "0" * fehlende_nullen + binaer_string
    nibbles = []

    for i in range(0, len(binaer_ergebnis), 4):
        nibble = binaer_ergebnis[i: i + 4]
        nibbles.append(nibble)

    formatierter_binaer_string = " ".join(nibbles)
    return formatierter_binaer_string



def binaer_zu_dezimal(binaer):
    ergebnis = 0
    for ziffer in binaer:
        ergebnis = ergebnis * 2 + int(ziffer)
    return ergebnis




while True:
    try:
        modus = int(input("Was möchtest du umrechnen?\n1 - Dezimal zu Binär\n2 - Binär zu Dezimal\n\nDeine Auswahl: "))
        if modus == 1:
            print(f"Du hast '{modus} - Dezimal in Binär' gewählt.")
        elif modus == 2:
            print(f"Du hast '{modus} - Binär in Dezimal' gewählt.")
        else:
            print("Ungültige Eingabe! Bitte tippe 1 für Dezimal zu Binär oder 2 für Binär zu Dezimal.")
            continue
        break
    except ValueError:
        print("Ungültige Eingabe! Bitte tippe 1 für Dezimal zu Binär oder 2 für Binär zu Dezimal.")



if modus == 1:
    while True:
        try:
            modus_1 = int(input("Welche Dezimalzahl möchtest du umrechnen? "))
            break
        except ValueError:
            print("Ungültige Eingabe! Bitte verwende nur Zahlen.")


    ergebnis = binaer_formatieren(dezimal_zu_binaer(modus_1))
    print(ergebnis)



elif modus == 2:
    while True:
        modus_2 = input("Welche Binärzahl möchtest du umrechnen? ")
        modus_2 = modus_2.replace(" ", "")
        if modus_2 == "":
            print("Ungültige Eingabe! Bitte gebe eine Binärzahl ein.")
        else:
            gueltig = True
            for zeichen in modus_2:
                if zeichen != "0" and zeichen != "1":
                    gueltig = False
                    print("Ungültige Eingabe! Eine Binärzahl darf nur aus 0 und 1 bestehen.")
                    break
            if gueltig:
                ergebnis = binaer_zu_dezimal(modus_2)
                print(ergebnis)
                break        