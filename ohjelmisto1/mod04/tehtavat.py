#Tehtävä 1

'''
kuhan_pituus = float(input("Anna kuhan pituus (cm): "))
if kuhan_pituus < 37:
    print("laske kuha takaisin järveen. Sallitusta pyyntimitasta puuttuu", 37 - kuhan_pituus, "cm.")
'''

#tehtävä 2

'''
print("Hyttiluokat:\n" \
      "LUX on parvekkeellinen hytti yläkannella.\n" \
      "A on ikkunallinen hytti autokannen yläpuolella.\n" \
      "B on ikkunaton hytti autokannen yläpuolella.\n" \
      "C on ikkunaton hytti autokannen alapuolella.")
hyttiluokka = input("Anna hyttiluokka: ")
if hyttiluokka in ["LUX", "A", "B", "C"]:
    print("Kiitos.")
else:
    print("Virheellinen hyttiluokka.")
'''

#tehtävä 3

'''
sukupuoli = input("Anna sukupuoli (nainen/mies): ")

if sukupuoli == "nainen":
    hemoglobiini = float(input("Anna hemoglobiiniarvo (g/l): "))
    if hemoglobiini < 117:
        print("Hemoglobiini on alhainen.")
    elif hemoglobiini > 175:
        print("Hemoglobiini on korkea.")
    else:
        print("Hemoglobiini on normaali.")

elif sukupuoli == "mies":
    hemoglobiini = float(input("Anna hemoglobiiniarvo (g/l): "))
    if hemoglobiini < 134:
        print("Hemoglobiini on alhainen.")
    elif hemoglobiini > 195:
        print("Hemoglobiini on korkea.")
    else:
        print("Hemoglobiini on normaali.")

'''

#tehtävä 4

'''
vuosiluku = float(input("Anna vuosiluku: "))
if (vuosiluku % 100 == 0 or vuosiluku % 400 == 0):
    print(f"Vuosi {vuosiluku:.0f} on karkausvuosi.")
else:
    print(f"Vuosi {vuosiluku:.0f} ei ole karkausvuosi.")
'''