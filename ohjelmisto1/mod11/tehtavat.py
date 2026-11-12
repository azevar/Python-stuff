#tehtava 1
'''
class Julkaisu:
    def __init__(self, nimi):
        self.nimi = nimi

class Kirja(Julkaisu):
    def __init__(self, nimi, kirjoittaja, sivumaara):
        super().__init__(nimi)
        self.kirjoittaja = kirjoittaja
        self.sivumaara = sivumaara

    def tulosta_tiedot(self):
        print(f"Kirja: {self.nimi}, Kirjoittaja: {self.kirjoittaja}, Sivumäärä: {self.sivumaara} sivua")

class Lehti(Julkaisu):
    def __init__(self, nimi, paatoimittaja):
        super().__init__(nimi)
        self.paatoimittaja = paatoimittaja

    def tulosta_tiedot(self):
        print(f"Lehti: {self.nimi}, Päätoimittaja: {self.paatoimittaja}")

julkaisut = [
    Lehti("Aku Ankka", "Aki Hyppä"),
    Kirja("Hytti n:o 6", "Rosa Liksom", 200)
]

for j in julkaisut:
    j.tulosta_tiedot()
'''

#tehtava 2
'''
class Auto:
    def __init__(self, rekisteritunnus, huippunopeus):
        self.rekisteritunnus = rekisteritunnus
        self.huippunopeus = huippunopeus
        self.nopeus = 0
        self.kuljettu_matka = 0

    def kiihdyta(self, muutos):
        self.nopeus += muutos
        if self.nopeus > self.huippunopeus:
            self.nopeus = self.huippunopeus
        elif self.nopeus < 0:
            self.nopeus = 0

    def kulje(self, tuntimaara):
        self.kuljettu_matka += self.nopeus * tuntimaara


class Sahkoauto(Auto):
    def __init__(self, rekisteritunnus, huippunopeus, akkukapasiteetti):
        super().__init__(rekisteritunnus, huippunopeus)
        self.akkukapasiteetti = akkukapasiteetti


class Polttomoottoriauto(Auto):
    def __init__(self, rekisteritunnus, huippunopeus, bensatankin_koko):
        super().__init__(rekisteritunnus, huippunopeus)
        self.bensatankin_koko = bensatankin_koko


sahkoauto = Sahkoauto("ABC-15", 180, 52.5)
polttomoottori = Polttomoottoriauto("ACD-123", 165, 32.3)

sahkoauto.kiihdyta(120)
polttomoottori.kiihdyta(100)

sahkoauto.kulje(3)
polttomoottori.kulje(3)

print(f"Sähköauto ({sahkoauto.rekisteritunnus}) matkamittarilukema: {sahkoauto.kuljettu_matka} km")
print(f"Polttomoottoriauto ({polttomoottori.rekisteritunnus}) matkamittarilukema: {polttomoottori.kuljettu_matka} km")
'''