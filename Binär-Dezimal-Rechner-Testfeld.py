"""
1101
Start bei 1
Das bisherige Ergebnis wird verdoppelt und anschließend das nächste Binärbit addiert.

Zu Beginn sind zwei Variablen zu erwarten:
ergebnis = ...
und
für jedes Zeichen im Binärstring: ...
"""

binaer = "1101"
ergebnis = 0

for ziffer in binaer:
    ergebnis = ergebnis * 2 + int(ziffer)