# -*- coding: cp1252 -*-

import random

#alifunktio
def koneenpeli():
    koneen_vastaus = random.randint(1,3)
    if koneen_vastaus == 1:
        return "Jalka"
    elif koneen_vastaus == 3:
        return "Torakka"
    elif koneen_vastaus == 2:
        return "Ydinase"

#toinen alifunktio
def JTY_peli(kone,pelaaja):
    if kone == "Jalka":
        if pelaaja == "Ydinase":
            return "Voitit!"
        elif pelaaja == "Torakka":
            return "Hävisit!"
        else:
            return "Tasapeli!"

    elif kone == "Ydinase":
        if pelaaja == "Jalka":
            return "Hävisit!"
        elif pelaaja == "Torakka":
            return "Voitit!"
        else:
            return "Tasapeli!"

    elif kone == "Torakka":
        if pelaaja == "Jalka":
            return "Voitit!"
        elif pelaaja == "Ydinase":
            return "Hävisit!"
        else:
            return "Tasapeli!"

#pääfunktio
def main():
    kierrokset = 0
    voitot = 0
    tasapelit = 0
    while True:
        inp = input("Jalka, Ydinase vai Torakka? (Lopeta lopettaa): ")
        if inp == "Lopeta":
            print("Pelasit",kierrokset,"kierrosta, joista voitit",voitot, "ja pelasit tasan",tasapelit,"peliä.")
            break
        else:
            kierrokset = kierrokset + 1
            tietokone = koneenpeli()
            JTY_tulos = JTY_peli(tietokone,inp)
            if JTY_tulos == "Voitit!":
                voitot = voitot + 1
            elif JTY_tulos == "Tasapeli!":
                tasapelit = tasapelit + 1
            print("Sinä valitsit: ", inp)
            print("tietokone valitsi: ", tietokone)
            print(JTY_tulos)

#pääfunktion kutsu
if __name__ == "__main__":
    main()
