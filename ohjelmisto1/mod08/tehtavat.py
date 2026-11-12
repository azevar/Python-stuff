#tehtava 1
'''
vuodenajat = ("talvi", "talvi", "kevät", "kevät", "kevät", "kesä", "kesä", "kesä", "syksy", "syksy", "syksy", "talvi")

kuukausi = int(input("Anna kuukauden numero (1-12): "))

if 1 <= kuukausi <= 12:
    vuodenaika = vuodenajat[kuukausi - 1]
    print(f"Kuukausi {kuukausi} kuuluu vuodenaikaan: {vuodenaika}")
else:
    print("Virheellinen kuukauden numero.")
'''

#tehtava 2
'''
nimet = set()

nimi = input("Anna nimi (tyhjä lopettaa): ")

while nimi != "":
    if nimi in nimet:
        print("Aiemmin syötetty nimi")
    else:
        print("Uusi nimi")
        nimet.add(nimi)
    
    nimi = input("Anna nimi (tyhjä lopettaa): ")

print("\nSyötetyt nimet:")
for n in nimet:
    print(n)
'''
