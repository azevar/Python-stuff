teksti = "hood calculator, gimme two numbers"

luku = input("Gimme the first number: ")
luku2 = input("Gimme the second number: ")

luku = float(luku)
luku2 = float(luku2)

#luku = 67
#luku2= 420

summa = luku + luku2
#print("summa", summa)

#print("lukujen", luku, "ja", luku2, "summa on", summa)

#sama liitosoperaattorilla (+)
summa = str(summa)
#print("summa: " + summa)

print("the numbers " + str(luku) + " and " + str(luku2) + " equal to " + summa + ".")
