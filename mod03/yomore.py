# teksti = "hood calculator, gimme two numbers"

# luku = input("Gimme the first number: ")
# luku2 = input("Gimme the second number: ")

# luku = float(luku)
# luku2 = float(luku2)

#luku = 67
#luku2= 420

# summa = luku + luku2
#print("summa", summa)

#print("lukujen", luku, "ja", luku2, "summa on", summa)

#sama liitosoperaattorilla (+)
# summa = str(summa)
#print("summa: " + summa)

# print("the numbers " + str(luku) + " and " + str(luku2) + " equal to " + summa + ".")

import math


new_user = input("Gimme your name: ")

ikä = 21

print(f'wsg {new_user}!! i am ahmed and i am {ikä} years old')

points = 69
points = 420
print(f'you have {points} points')

merkkijono = 'abdi'
# merkkijono = '9'
pisteet = 0

print(f'merkkijono: {merkkijono:<20s} sijoitetaan tähän väliin')

kokonaisluku = -9
kokonaisluku_pitkä = 12_456_123_100
liukuluku = 3.141
kompleksiluku = 3 + 4j
totuusarvo = False

print(kompleksiluku)
print(kompleksiluku.real)
print(kompleksiluku.imag)

# tyyppi = type(totuusarvo)  tai suoraan

print(f'Muuttujan tyyppi voidaan tutkia {type(kompleksiluku)}')

print(f"{'vakio':6s}| {"arvo":6s}")
print("-----------------")
print(f"{'Pii':12s}: {math.pi:<10.2f}")


tuloste = '''
    yhteenlasku (+), vähennyslasku (-)
    kertolasku (*), jakolasku (/)
    jakojäännösoperaatio (%)
    pelkän kokonaisosan palauttava jakolasku (//) 
    potenssiinkorotus (**)
'''
print(tuloste)

#laskukone

print("Gimme two numbers and i will calculate them for you twin")

a = float(input("Gimme the first number:\n"))
b = float(input("Gimme the second number:\n"))

yhteenlasku = a + b
vahennyslasku = a - b
kertolasku = a * b
jakolasku = a / b
potenssiinkorotus = a ** b
kokonaisosa = a // b
jakojaannos = a % b

print(f'Yhteenlasku: {yhteenlasku}')
print(f'Vähennyslasku: {vahennyslasku}')
print(f'Kertolasku: {kertolasku}')
print(f'Jakolasku: {jakolasku}')
print(f'Potenssiinkorotus: {potenssiinkorotus}')
print(f'Kokonaisosa: {kokonaisosa}')
print(f'Jakojäännös: {jakojaannos}')
