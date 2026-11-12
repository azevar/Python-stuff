import random
'''
suorita = True
while suorita:
    print("tämä printtaantuu vain kerran")
    suorita = False

print("suoritus loppui")

luku = 1

while luku <= 5:
    print(luku)
    luku += 1

print("jatketaan ohjelmaa")

luku = int(input("Anna luku josta lasketaan alaspäin: "))

while luku >= 1:
    print(luku)
    luku -= 1
'''

'''
salasana = input("Anna salasana: ").strip().lower()
while salasana != "salasana":
    print("Väärä salasana!")
    salasana = input("Anna salasana uudelleen: ")
print("Oikea salasana!")
'''

'''
komento = input("Anna komento (lopeta, APUA): ").strip().lower(

while komento != "lopeta":
    if komento == "apua":
        print("Tämä ohjelma ei osaa auttaa sinua.")
    else:
        print("Tuntematon komento!")
    komento = input("Anna komento (lopeta, APUA): ").strip().lower(
)

'''

'''
noppa1 = noppa2 = heitot = 0

while (noppa1 != 6 or noppa2 != 6 ):

    noppa1 = random.randint(1,6)
    noppa2 = random.randint(1,6)
    print(noppa1, noppa2)
    heitot = heitot + 1

print(f"Tarvittiin {heitot:d} heittoa.")
'''

'''
eka = 1
while eka <= 5:
    toka = 1
    while toka <= 5:
        print(f"{eka} kertaa {toka} on {eka+toka:d}")
        toka = toka + 1
    eka = eka + 1
'''

'''
kierros = 0
heitto = 0

while pelikerta <= 1000:

    noppa1 = noppa2 = 0
    while (noppa1 != 6 or noppa2 != 6 ):

        noppa1 = random.randint(1,6)
        noppa2 = random.randint(1,6)
        print(noppa1, noppa2)
        heitot = heitot + 1
pelikerta += 1

print("pelikertoja meillä oli", pelikerta)
print(f"Tarvittiin {heitot:d} heittoa.")
print(f"jokaisella kierroksella oli keskimäärin {heitot/pelikerta} heittoa")
'''