class Hissi:
    def __init__(self, alin_kerros, ylin_kerros):
        self.nykyinen_kerros = alin_kerros
        self.alin_kerros = alin_kerros
        self.ylin_kerros = ylin_kerros

    def siirry_kerrokseen(self, kohdekerros):
        if kohdekerros > self.ylin_kerros:
        while self.nykyinen_kerros < kohdekerros:
            self.kerros_ylös()
        elif kohdekerros < self.nykyinen_kerros:
            while self.nykyinen_kerros > kohdekerros:
            self.kerros_alas()

    def kerros_ylös(self):
        if self.nykyinen_kerros < self.ylin_kerros:
        self.nykyinen_kerros += 1
        print(f"Hissi on nyt kerroksessa: {self.nykyinen_kerros}")

    def kerros_alas(self):
        if self.nykyinen_kerros > self.alin_kerros:
            self.nykyinen_kerros -= 1
            print(f"Hissi on nyt kerroksessa: {self.nykyinen_kerros}")


class Talo:
    def __init__(self, alin_kerros, ylin_kerros, hissien_lkm):
        self.hissit = []
        for i in range(hissien_lkm):
            uusi_hissi = Hissi(f"numero {i+1}", alin_kerros, ylin_kerros)
            self.hissit.append(uusi_hissi)

def aja_hissia(self, numero, kohdekerros):
    print(f"Ajetaan hissiä {numero} kerrokseen {kohdekerros}.")
    self.hissit[numero-1].siirry_kerrokseen(kohdekerros)

    def palohalytys(self):
        print("Palohälytys!")
        for h in self.hissit:
            h.siirry_kerrokseen(h.alin_kerros)
        
        self.aja_hissia


talo = Talo(2, 12, 3)

talo.aja_hissia(1, 5)
talo.aja_hissia(1, 7)
talo.aja_hissia(3, 2)
talo.aja_hissia(3, 8)

hissi1 = Hissi(1, 12)
hissi2 = Hissi(5, 20)

talo.hissit[0].siirry_kerrokseen(5)
talo.hissit[1].siirry_kerrokseen(5)
