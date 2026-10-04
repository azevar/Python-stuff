#tehtava 1

class Auto:
    def __init__(self, rekistekitunnus, huippunopeus):
        self.rekisteritunnus = rekistekitunnus
        self.huippunopeus = huippunopeus
        self.nopeus = 0
        self.kuljettu_matka = 0

def kiihdyta(self, muutos):
    print("Kiihdytetään")
    self.nopeus += muutos
if self.nopeus > self.huippunopeus:
    self.nopeus = self.huippunopeus
elif self.nopeus < 0:
    self.nopeus = 0

def kulje(self, tuntimäärä):
    self.kuljettu_matka += self.nopeus * tuntimäärä

auto= Auto ("ABC-123", 142)

print("Auton rekisteritunnus:", auto.rekisteritunnus)
print("huippunopeus:", auto.huippunopeus)
print("nopeus:", auto.nopeus)
print("kuljettu matka:", auto.kuljettu_matka)

auto.kiihdyta(30)
auto.kiihdyta(70)
auto.kiihdyta(50)
print("nopeus:", auto.nopeus)
auto.kulje(1.5)
print("nopeus:", auto.nopeus)
print("kuljettu matka 1.5h jälkeen:", auto.kuljettu_matka)

auto.kiihdyta(-200)
print("nopeus jarrutuksen jälkeen:", auto.nopeus)