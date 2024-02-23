"""
pl = punteggi per lettera
lp = numero di lettere presenti
lu = lettere in mano all'utente
le = singola lettera
pi = parole italiane
"""

import random

pl = {
    'a': 1, 'b': 5, 'c': 2, 'd': 5, 'e': 1, 'f': 5, 'g': 8, 'h': 8, 'i': 1,
    'l': 3, 'm': 3, 'n': 3, 'o': 1, 'p': 5, 'q': 10, 'r': 2,
    's': 2, 't': 2, 'u': 3, 'v': 3, 'z': 8
}
lp = {
    'a': 14, 'b': 3, 'c': 6, 'd': 3, 'e': 11, 'f': 3, 'g': 2, 'h': 2, 'i': 12,
    'l': 5, 'm': 5, 'n': 5, 'o': 15, 'p': 3, 'q': 1, 'r': 6,
    's': 6, 't': 6, 'u': 5, 'v': 3, 'z': 2
}


def calc_punt(s):
    total = 0
    for c in s:
        total += pl[c]
    return total


def controllo_parola(s):
    for c in s:
        if c not in lp or lp[c] == 0:
            return False
        lp[c] -= 1
    return True


def lettura_file():
    f = open("280000_parole_italiane.txt", "r")
    pi = []
    for x in f:
        pi.append(x.strip())
    return pi

def sostituisci_lettere_utilizzate(s, lu, lettere):
    for c in s:
        lu = lu.replace(c, '')
    while len(lu) < 8 and len(lettere) > 0:
        le = random.choice(lettere)
        lettere.remove(le)
        lu+=le
    return lu

def main():
    pi = lettura_file()
    lettere = []
    for x in lp:
        for _ in range(lp[x]):
            lettere.append(x)
    lu = ""
    for _ in range(8):
        le = random.choice(lettere)
        lettere.remove(le)
        lu+=le
    while True:
        print("Lettere del giocatore --> " + lu)
        inp = str(
            input("Inserisci la parola che riesci a formare con le lettere che hai\n(scrivi 'end' per terminare): "))

        if inp == "end":
            print("Grazie per giocato! ;)")
            break

        if controllo_parola(inp) == True and inp in pi:
            print(f"Parola {inp} ha {calc_punt(inp)} punti")
            lu = sostituisci_lettere_utilizzate(inp, lu, lettere)
        else:
            print("Parola non valida")


main()
