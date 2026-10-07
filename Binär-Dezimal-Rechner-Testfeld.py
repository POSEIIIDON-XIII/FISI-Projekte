binaer = "1101"

def binaer_zu_dezimal(binaer):
    ergebnis = 0
    for ziffer in binaer:
        ergebnis = ergebnis * 2 + int(ziffer)
    return ergebnis

ergebnis = binaer_zu_dezimal("1101")
print(ergebnis)
