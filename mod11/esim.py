elainten_lkm = 0

class Elain:

    def __init__(self, nimi, paino, synt_aika):
        self.nimi = nimi
        self.paino = paino
        self.synt_aika = synt_aika
        Elain.elainten_lkm += 1

    def liiku(self):
        return f"{self.nimi} liikkuu!"

    def kaikki_tiedot(self):
        print(f"Nimi: {self.nimi}, Paino: {self.paino/1000} kg, Syntymäaika: {self.synt_aika}")

class Peto:
    def __init__(self, on_metsastaja):
        self.on_metsastaja = on_metsastaja

class Ilves(Elain):
    def kilju(self):
            return f"{self.nimi} kiljuu!"
    
    def kaikki_tiedot(self):
        print("\nIlves")
        super().kaikki_tiedot()

class Karhu(Elain, Peto):
    def __init__(self, nimi, paino, synt_aika, on_horroksessa, on_metsastaja=True):
        super().__init__(nimi, paino, synt_aika)
        Peto.__init__(self, on_metsastaja)
        self.on_horroksessa = on_horroksessa

    def karju(self):
            return f"Karhu nimeltä {self.nimi} karjuu!"
    def kaikki_tiedot(self):
        return f"Nimi: {self.nimi}, Paino: {self.paino/1000} kg, Syntymäaika: {self.synt_aika}, On horroksessa: {self.on_horroksessa}"

uusi_elain = Elain("Joku elukka", 1500, 20250921)
uusi_elain.liiku()

ilves1 = Ilves("Ilveskissa", 6500, 20250921)
ilves1.liiku()
ilves1.kilju()

karhu1 = Karhu("Nalle", 155000, 20200814, False)
karhu1.karju()


kaikki_elaimet = [uusi_elain, ilves1, karhu1]
for elain in kaikki_elaimet:
    elain.kaikki_tiedot()