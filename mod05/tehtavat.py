#tehtava 1

luku = 1
while luku <= 1000:

    if luku % 3 == 0:
        print(luku)
luku += 1 

#tehtava 4
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