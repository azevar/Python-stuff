import random

#tehtava 1
'''
import random

def heita_noppaa():
    return random.randint(1, 6)

def paaohjelma():
    silmaluku = 0
    while silmaluku != 6:
        silmaluku = heita_noppaa()
        print(f"Heiton tulos: {silmaluku}")

paaohjelma()
'''

#tehtava 2
'''
import random

def heita_noppaa(tahkot):
    return random.randint(1, tahkot)

def paaohjelma():
    tahkot = int(input("Anna nopan tahkojen määrä: "))
    maksimi = tahkot
    silmaluku = 0
    
    while silmaluku != maksimi:
        silmaluku = heita_noppaa(tahkot)
        print(f"Heiton tulos: {silmaluku}")

paaohjelma()
'''

#tehtava 3
'''
def gallonat_litroiksi(gallonat):
    return gallonat * 3.785

def paaohjelma():
    gallonat = float(input("Anna bensiinin määrä gallonoina (negatiivinen lopettaa): "))
    while gallonat >= 0:
        litrat = gallonat_litroiksi(gallonat)
        print(f"{gallonat} gallonaa on {litrat:.3f} litraa.")
        gallonat = float(input("Anna bensiinin määrä gallonoina (negatiivinen lopettaa): "))
    print("Ohjelma lopetettu.")

paaohjelma()
'''

#tehtava 4
'''
def laske_summa(luvut):
    return sum(luvut)

def paaohjelma():
    testilista = [5, 10, 15, 20, 25]
    tulos = laske_summa(testilista)
    print(f"Listan lukujen summa on: {tulos}")

paaohjelma()
'''

#tehtava 5
'''
def karsi_parittomat(luvut):
    parilliset = []
    for luku in luvut:
        if luku % 2 == 0:
            parilliset.append(luku)
    return parilliset

def paaohjelma():
    alkuperainen = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    karsittu = karsi_parittomat(alkuperainen)
    print(f"Alkuperäinen lista: {alkuperainen}")
    print(f"Karsittu lista (vain parilliset): {karsittu}")

paaohjelma()
'''

#tehtava 6
'''
import math

def laske_yksikkohinta(halkaisija_cm, hinta_eur):
    sade_m = (halkaisija_cm / 2) / 100
    pinta_ala_m2 = math.pi * (sade_m ** 2)
    return hinta_eur / pinta_ala_m2

def paaohjelma():
    print("Pizza 1:")
    halkaisija1 = float(input("Anna pizzan halkaisija (cm): "))
    hinta1 = float(input("Anna pizzan hinta (€): "))
    
    print("\nPizza 2:")
    halkaisija2 = float(input("Anna pizzan halkaisija (cm): "))
    hinta2 = float(input("Anna pizzan hinta (€): "))
    
    yksikkohinta1 = laske_yksikkohinta(halkaisija1, hinta1)
    yksikkohinta2 = laske_yksikkohinta(halkaisija2, hinta2)
    
    print(f"\nPizza 1 yksikköhinta: {yksikkohinta1:.2f} €/m²")
    print(f"Pizza 2 yksikköhinta: {yksikkohinta2:.2f} €/m²")
    
    if yksikkohinta1 < yksikkohinta2:
        print("Pizza 1 antaa paremman vastineen rahalle.")
    elif yksikkohinta2 < yksikkohinta1:
        print("Pizza 2 antaa paremman vastineen rahalle.")
    else:
        print("Pizzoilla on sama yksikköhinta.")

paaohjelma()
'''