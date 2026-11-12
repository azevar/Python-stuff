from ohjelmisto1.peliprojekti.peliluokat import Esine, Huone, Pelaaja

def main():
    #Luodaan pelaaja ja muutama esinettä ja huonetta
    miekka = Esine("Miekka", 3.5)
    avain = Esine("Kultainen avain", 0.2)

    aula = Huone("Aula", miekka)
    kirjasto = Huone("Kirjasto", avain)
    kellari = Huone("Kellari") #Huone ilman esinettä

    pelaaja_nimi = input("Anna pelaajan nimi: ")
    pelaaja = Pelaaja(pelaaja_nimi, aula)

    while True:
        print("\n--- PELIVALIKKO ---")
        print(f"Olet täällä: {pelaaja.sijainti}")
        print(f"Inventaario: {[str(e) for e in pelaaja.esineet]}")
        print("1. Mene toiseen huoneeseen")
        print("2. Kerää huoneessa oleva esine")
        print("3. Lopeta peli")

        valinta = input("Valitse toiminto (1-3): ")

        if valinta == "1":
            print("\nValitse huone:")
            print("1. Aula")
            print("2. Kirjasto")
            print("3. Kellari")
            kohde_valinta = input("Valinta: ")

            if kohde_valinta == "1":
                pelaaja.liiku(aula)
            elif kohde_valinta == "2":
                pelaaja.liiku(kirjasto)
            elif kohde_valinta == "3":
                pelaaja.liiku(kellari)
            else:
                print("Virheellinen valinta.")

        elif valinta == "2":
            pelaaja.keraa_esine()

        elif valinta == "3":
            print("Kiitos pelaamisesta!")
            break
        else:
            print("Tuntematon komento, yritä uudelleen.")

if __name__ == "__main__":
    main()