#tehtava 1
'''
import random

lkm = int(input("Anna arpakuutioiden lukumäärä: "))
summa = 0
for i in range(lkm):
    noppa = random.randint(1,6)
    print(f"Arvottiin {noppa}")
    summa += noppa

print(f"Silmälukujen summa on {summa}")
'''


#tehtava 2
'''
luvut = []

luku = (input("Anna luku, tyhjä lopettaa: "))
while luku != "":
    try:
        luku = (luku)
        luvut.append(luku)
    except ValueError:
        print("Virheellinen luku, yritä uudelleen.")

    luku = input("Anna luku, tyhjä lopettaa: ")

if luvut:
    luvut.sort(reverse=True)
    viisi_suurinta = luvut[:5]
    print(f"Syötit seuraavat luvut: {luvut}")
    print(f"Viisi suurinta lukua järjestyksessä suurimmasta alkaen: {viisi_suurinta}")
    for luku in viisi_suurinta:
        print(luku)
else:
    print("Et syöttänyt yhtään lukua.")
'''

#tehtava 3
'''
luku = int(input("Anna kokonaisluku: "))

alkuluku = True

if luku <= 1:
    alkuluku = False
else:
    for i in range(2, luku):
        if luku % i == 0:
            alkuluku = False
            break

if alkuluku:
    print(f"Luku {luku} on alkuluku.")
else:
    print(f"Luku {luku} ei ole alkuluku.")
'''

#tehtava 4
'''
kaupungit = []

for i in range(5):
    kaupunki = input(f"Anna {i + 1}. kaupungin nimi: ")
    kaupungit.append(kaupunki)

print("\nSyöttämäsi kaupungit:")
for kaupunki in kaupungit:
    print(kaupunki)
'''