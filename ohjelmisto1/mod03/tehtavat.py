import math

'''
nimi= input('Gimme your name: ')
print(f'Wsg {nimi}!!')

#ympyrän pinta-ala: pi * r^2

r = float(input('Gimme the radius of the circle: '))
pinta_ala = math.pi * r ** 2
# pyoristys = round(pinta_ala, 2)
print(f'The area of the circle is: {pinta_ala:.2f} twin')
'''

'''
a = float(input('anna suorakulmion kanta: '))
b = float(input('anna suorakulmion korkeus: '))
piiri = 2 * (a + b)
# piiri2 = 2 * a + 2 * b
# print(f'suorakulmion piiri on: {piiri:.2f} twin')
print(f'suorakulmion piiri on: {piiri:.2f} ja pinta-ala: {a * b:.4f} twin')
'''

#tehtävä 5

'''

luoti_grammoina = 13.3
naula_luoteina = 32
leiviskä_nauloina = 20

leiviskat = float(input("Paljonko leivisköjä?\n"))
naulat = float(input("Paljonko nauloja?\n"))
luodit = float(input("Paljonko luoteja?\n"))

yhteensa_luodit = (leiviskat * leiviskä_nauloina * naula_luoteina + naulat * naula_luoteina + luodit)

yhteensa_grammat = yhteensa_luodit * luoti_grammoina

kilogrammat = int(yhteensa_grammat // 1000)
grammat = yhteensa_grammat % 1000

print("\nMassa nykymittojen mukaan:")
print(f"{kilogrammat} kilogrammaa ja {grammat:.2f} grammaa.")

'''

'''

#opettajan tapa

leiviskat_lkm = float(input("Anna leivisköiden määrä: "))
naulat_lkm = float(input("Anna naulojen määrä: "))
luodit_lkm = float(input("Anna luotien määrä: "))

naulat_lkm = leiviskat_lkm * 20 + naulat_lkm
luodit_lkm = naulat_lkm * 32 + luodit_lkm

massa_g = luodit_lkm * 13.3
massa_kg = massa_g / 1000

print(f"Massa nykymittojen mukaan: {int(massa_kg % 1000)} kilogrammaa ja {massa_g % 1000:.2f} grammaa.")

'''

#tehtävä 6

'''
import random

luku = random.randint(0, 9)
luku2 = random.randint(0, 9)
luku3 = random.randint(0, 9)
print(f'{luku}, {luku2}, {luku3}')
print(f'{random.randint(0, 9)}, {random.randint(0, 9)}, {random.randint(0, 9)}')
'''