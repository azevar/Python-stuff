class Esine:
    #esine, jolla on nimi ja paino
    def __init__(self, nimi: str, paino: float):
        self.nimi = nimi
        self.paino = paino

    def __str__(self):
        return f"{self.nimi} ({self.paino} kg)"


class Huone:
    #huone, jossa voi olla esine
    def __init__(self, nimi: str, esine: Esine = None):
        self.nimi = nimi
        self.esine = esine

    def __str__(self):
        esine_info = f", täällä on esine: {self.esine}" if self.esine else ""
        return f"Huone: {self.nimi}{esine_info}"


class Pelaaja:
    def __init__(self, nimi: str, sijainti: Huone):
        self.nimi = nimi
        self.esineet: list[Esine] = [] #Esineet, mitä pelaajalla on
        self.sijainti = sijainti  #Pelaajan sijainti

    def liiku(self, kohde: Huone):
        #Pelaaja liikkuu toiseen huoneeseen
        self.sijainti = kohde
        print(f"{self.nimi} siirtyi huoneeseen: {kohde.nimi}")

    def keraa_esine(self):
        #Kerää huoneessa olevat esineet
        if self.sijainti.esine:
            löytynyt_esine = self.sijainti.esine
            self.esineet.append(löytynyt_esine)
            print(f"Keräsit esineen: {löytynyt_esine.nimi}")
            #Poistaa esineen huoneesta, koska se otettiin
            self.sijainti.esine = None
        else:
            print("Tässä huoneessa ei ole kerättävää esinettä.")