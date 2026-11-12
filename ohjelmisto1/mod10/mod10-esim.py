class Koira:
    def __init__(self, nimi, syntymävuosi, haukahdus='Hau hau!'):
        self.nimi = nimi
        self.syntymävuosi = syntymävuosi
        self.haukahdus = haukahdus

    def hauku(self, kerrat):
        for i in range(kerrat):
            print(self.nimi + " haukkuu: " + self.haukahdus)

class hoitola:
    def __init__(self):
        self.koirat = []

    def koira_sisaan(self, koira):
        self.koirat.append(koira)
        print(koira.nimi + " kirjattu sisään.")
        print(koira.hauku(2))

koira1 = Koira("Muro", 2018)
koira2 = Koira("Rekku", 2022, "Woof woof!")

hoitola = hoitola()
hoitola.koira_sisaan(koira1)
hoitola.koira_sisaan(koira2)

koira1.hauku(3)

koira2.hauku(2)

koira2 = koira1

koira2.hauku(1)

def muokkaa_listaa(muokattava_lista):
    muokattava_lista.append(6)

lista = [1, 5, 8]
print(lista)
muokkaa_listaa(lista)
print(lista)