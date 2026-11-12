'''

k1_rotu = 'Mastiffi'
k1_nimi = 'Wuffe'
k1_syntymävuosi = 2022

k1_rotu = 'Bokseri'
k1_nimi = 'Lissu'
k1_syntymävuosi = 2025

k1_rotu = 'Labradori'
k1_nimi = 'Sisu'
k1_syntymävuosi = 2020

class Koira:
    pass

koira = Koira()
koira2 = Koira()

koira.nimi = "Wuffe"
koira.rotu = "Mastiffi"

koira2.nimi = "Lissu"
koira2.rotu = "Bokseri"

print('Ensimmäisen koiran nimi:', koira.nimi)
print('Ensimmäisen koiran rotu:', koira.rotu)

print('Toisen koiran nimi:', koira2.nimi)
print('Toisen koiran rotu:', koira2.rotu) 

class Koira:

    tehty = 0

    koiran_lelut = ['vinkulelu', 'purulelu', 'pallo', 'narulelu']

    def __init__(self, nimi, rotu, syntymävuosi, haukahdus='Hau hau!'):
        self.nimi = nimi
        self.rotu = rotu
        self.syntymävuosi = syntymävuosi
        self.haukahdus = haukahdus
        self.luokitus = 'nisäkäs'
        Koira.tehty += 1

    def hauku(self, kerrat):
        print(f'{self.nimi} tervehtii sinua')
        for i in range(kerrat):
            print(self.haukahdus)

koira = Koira("Lissu", "Bokseri", 2022, "Hau hau!")
koira2 = Koira("Wuffe", "Mastiffi", 2025, "Hau hau!")
koira3 = Koira("Fifi", "Puudeli", 2015)

koira.hauku(2)
print()
koira2.hauku(3)
print()
koira3.hauku(1)

print(f'1. koiran nimi on {koira.nimi} ja rotu on {koira.rotu}'),
vuosi {koira.syntymävuosi}
print(f'2. koiran nimi on {koira2.nimi} ja rotu on {koira2.rotu}')

'''
'''
info = 'pelaajan tiedot'

class Player:
    def __init__(self, name, skill_level, inventory):
        self.name = name
        self.skill_level = skill_level
        self.inventory = inventory

    def show_info(self):
        print(f'Pelaajan nimi: {self.name}')
        print(f'Taso: {self.skill_level}')
        print(f'Inventaario:')
        for item in self.inventory:
            print('>',{item})
        print('--------')

    def add_item(self, item):
        self.inventory.add(item)
        print(f'Lisätty {item} inventaarioon.')

player1 = Player(
    "Player 1", 10, {"map", "knife"})
player2 = Player("Player 2", 20, {"axe"})

player1.show_info()
player2.show_info()

player1.add_item("key")

'''