#Muistikirja, joka on luotu Metropolian avoimen amk:n Python-ohjelmointi 3 op -kurssin päättötyönä 2018
#Tekijä: Mari Kekkonen
# -*- coding: UTF8 -*-
import time
import pickle

#alifunktio muistion alkioiden laskemiseksi
def lukumaara(parametri):
    maara = 0
    for i in parametri:
        maara = maara + 1
    return maara

#alifunktio muutosten tekemiseksi
def muutos(parametri):
    while True:
        try:
            parametri = int(parametri)
            sijainti = parametri - 1
            return sijainti
        except:
            print("Virheellinen syöte!")
            parametri = input("Anna luku: ")

try:
    tiedosto = open("muistio.dat","rb")
    tiedosto.close()
except IOError:
    print("Virhe tiedostossa, luodaan uusi muistio.dat.")
    tiedosto = open("muistio.dat","wb")
    sisalto = []
    pickle.dump(sisalto,tiedosto)
    tiedosto.close()

#tiedoston muisto.dat sisältö muuttujaan sisalto
tiedosto = open("muistio.dat","rb")
sisalto = pickle.load(tiedosto)
tiedosto.close()

valikko = """
(1) Lue muistikirjaa
(2) Lisää merkintä
(3) Muokkaa merkintää
(4) Poista merkintä
(5) Tallenna ja lopeta
"""
while True:
    print(valikko)
    inp = input("Mitä haluat tehdä?: ")
    try:
        inp = int(inp)
        if inp == 1: #lue muistikirjaa
            for i in sisalto:
                print(i)
        elif inp == 2: #lisää merkintä
            uusi_teksti = str(input("Kirjoita uusi merkintä: "))
            aika = time.strftime("%X %x")
            lisays_listalle = uusi_teksti+":::"+aika
            sisalto.append(lisays_listalle)
        elif inp == 3: #muokkaa merkintää
            lkm = lukumaara(sisalto)
            print("Listalla on",lkm,"merkintää.")
            muutos_alkio = input("Mitä niistä muutetaan?: ") #muutossyöte
            muutos_alkio = muutos(muutos_alkio)
            print(sisalto[muutos_alkio])
            sisalto.pop(muutos_alkio)
            uusi_teksti = str(input("Anna uusi teksti: ")) #lisäys muistioon
            aika = time.strftime("%X %x")
            lisays_listalle = uusi_teksti+":::"+aika
            sisalto.insert(muutos_alkio,lisays_listalle)
        elif inp == 4: #poista merkintä
            lkm = lukumaara(sisalto)
            print("Listalla on",lkm,"merkintää.")
            muutos_alkio = input("Mikä niistä poistetaan?: ") #muutossyöte
            muutos_alkio = muutos(muutos_alkio)
            print("Poistettiin merkintä", sisalto[muutos_alkio])
            sisalto.pop(muutos_alkio)
        elif inp == 5: #lopetus ja sisalto-listan tallennus tiedostoon muistio.dat
            tiedosto = open("muistio.dat","wb")
            pickle.dump(sisalto,tiedosto)
            tiedosto.close()
            print("Lopetetaan.")
            break
    except:
        print("Tuntematon valinta.")
