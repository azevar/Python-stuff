#tehtava 1
'''
luku = 1
while luku <= 1000:

    if luku % 3 == 0:
        print(luku)
luku += 1 
'''


#tehtava 2
'''
tuumat = float(input("Anna tuumien määrä: "))

while tuumat >= 0:
    senttimetrit = tuumat * 2.54
    print(f"{tuumat} tuumaa on {senttimetrit} senttimetriä")
    tuumat=float(input("Anna tuumien määrä: "))

print("Syötit negatiivisen luvun, ohjelma päättyy.")
'''

#tehtava 3
'''
luvut = []

luku = (input("Anna luku: "))
while luku != "":
    try:
        luku = (luku)
        luvut.append(luku)
    except ValueError:
        print("Virheellinen luku, yritä uudelleen.")

    luku = input("Anna luku, tyhjä syöte lopettaa: ")

if luvut:
    pienin = min(luvut)
    suurin = max(luvut)
    print(f"Syötit seuraavat luvut: {luvut}")
    print(f"Pienin luku: {pienin}")
    print(f"Suurin luku: {suurin}")
else:
    print("Et syöttänyt yhtään lukua.")
'''  



#tehtava 4
'''
oikea_numero = 7
arvaus = int(input("arvaa numero 1 ja 10 välillä: "))

while arvaus != oikea_numero:
    print("Väärin")
    arvaus = int(input("Arvaa uudestaan:"))

print(f"Jes, Sait kaiken oikein! Numero tosiaan oli {oikea_numero}")

peli_käynnissä = True
print("tervetuloa")

while peli_käynnissä:
    print("Valitse minne mennään (j tai l eli jatka tai lopeta)")
    valinta = input("Anna komento")
    if valinta == "j":
        print("Jatketaan")
    if valinta == "l":
        print("Peli päättyi")
        peli_käynnissä = False
        break
    else:
        print("Anna vaa käsky senkin typerys")

'''

#tehtava 5
'''
oikea_tunnus = "python"
oikea_salasana = "rules"
yritykset = 5

yritys_laskuri = 0
kirjautuminen_onnistui = False

while yritys_laskuri < yritykset and not kirjautuminen_onnistui:
    tunnus = input("Anna käyttäjätunnus: ")
    salasana = input("Anna salasana: ")

    if tunnus == oikea_tunnus and salasana == oikea_salasana:
        kirjautuminen_onnistui = True
        print("Kirjautuminen onnistui!")
    else:
        yritys_laskuri += 1
        print(f"Väärä tunnus tai salasana. Yrityksiä jäljellä: {yritykset - yritys_laskuri}")

if kirjautuminen_onnistui:
    print("Tervetuloa!")
else:
    print("Pääsy evätty.")
'''