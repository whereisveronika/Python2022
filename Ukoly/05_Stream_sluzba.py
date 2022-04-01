"""
Uvažuj, že vyvíjíš software pro službu, která nabízí streamování videa.
Služba nabízí dva typy pořadů - filmy a seriály. Firma chce evidovat,
které filmy a seriály nabízí a jejich žánry. Dále chce u filmů evidovat délku a
u seriálů počet episod a délku jedné episody.

Vytvoř program, který bude obsahovat tři třídy - Polozka, Film a Serial.

Třída Polozka bude sloužit jako základ pro další třídy. Bude mít atributy určující název a žánr.
Oba atributy nastav ve funkci __init__ a získej je jako parametry.

Třída Film bude potomkem třídy Polozka. Film má kromě názvu a žánru atribut délka.

Třída Serial bude potomkem třídy Polozka. Má kromě názvu a žánru atributy počet epizod a délka epizody.

Všem třídám přidej funkci get_info, která vypíše informace o položce, resp. o filmu a seriálu.
Funkce u třídy Polozka vypíše název a žánr. Následně tuto funkci využij ve funkcích u tříd Film a Serial a přidej k ní informaci o délce, resp. počtu episod.

Po naprogramování si vytvoř alespoň jeden objekt reprezentující film a seriál a ověř, že vše funguje.
"""

class Polozka:
  def __init__(self, nazev, zanr):
    self.nazev = nazev
    self.zanr = zanr

  def get_info(self):
    return f'Vybrali jste polozku s nazvem {self.nazev} z zanru {self.zanr}.'

class Film(Polozka):
  def __init__(self, nazev, zanr, delka):
    super().__init__(nazev, zanr)
    self.delka = delka

  def get_info(self):
    return f'Vybrali jste film {self.nazev} z zanru {self.zanr} o delce {self.delka} minut.'

class Serial(Polozka):
  def __init__(self, nazev, zanr, epizody, delka_epizody):
    super().__init__(nazev, zanr)
    self.epizody = epizody
    self.delka_epizody = delka_epizody

  def get_info(self):
    return f'Vybrali jste serial {self.nazev} z zanru {self.zanr}, ktery ma {self.epizody} epizod o delce {self.delka_epizody} minut jedne epizody.'

to = Polozka("To", "Horor")
print(to.get_info())
movie = Film("Deník Bridget Jones", "Komedie", 132)
print(movie.get_info())
serial = Serial("Červený trpaslík", "Sitcom", 6, 28)
print(serial.get_info())