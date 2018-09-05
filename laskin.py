#Simppeli suomenkielinen laskin, joka on luotu osana Metropolian avoimen amk:n Python-ohjelmointi 3 op -kurssia 2018
#Tekijä: Mari Kekkonen
# -*- coding: UTF8 -*-

import math

valikko = """(1) +
(2) -
(3) *
(4) /
(5)sin(luku1/luku2)
(6)cos(luku1/luku2)
(7) Vaihda luvut
(8) Lopeta"""
inp_1 = int(input("Anna ensimmäinen luku: "))
inp_2 = int(input("Anna toinen luku: "))

while True:
    print(valikko)
    print("Valitut luvut:",inp_1, inp_2)
    inp_3 = int(input("Tee valinta (1-8): "))
    if inp_3 == 1:
        tulos = inp_1 + inp_2
        print("Tulos on:",tulos)
    elif inp_3 == 2:
        tulos = inp_1 - inp_2
        print("Tulos on:",tulos)
    elif inp_3 == 3:
        tulos = inp_1 * inp_2
        print("Tulos on:",tulos)
    elif inp_3 == 4:
        tulos = inp_1 / inp_2
        print("Tulos on:",tulos)
    elif inp_3 == 5:
        tulos = math.sin(inp_1/inp_2)
        print("Tulos on:",tulos)
    elif inp_3 == 6:
        tulos = math.cos(inp_1/inp_2)
        print("Tulos on:",tulos)
    elif inp_3 == 7:
        inp_1 = int(input("Anna uusi ensimmäinen luku: "))
        inp_2 = int(input("Anna uusi toinen luku: "))
        continue
    elif inp_3 == 8:
        break
    else:
        print("Valintaa ei tunnistettu.")
