"""
Vytvoř program pro evidenci aut malé autopůjčovny. Půjčovna má 2 automobily:

Registrační značka	Značka a typ vozidla	Počet najetých kilometrů
4A2 3020	Peugeot 403 Cabrio	47534
1P3 4747	Škoda Octavia	41253
Vytvoř třídu Auto, která bude obsahovat informace o autech, které půjčovna nabízí.
Třída bude mít tyto atributy:

registrační značka automobilu,
značka a typ vozidla,
počet najetých kilometrů,
informaci o tom, jestli je vozidlo aktuálně volné
(pravdivostní hodnota -- True pokud je volné a False pokud je vypůjčené).
Vytvoř metodu __init__() pro třídu Auto. Registrační značku, značku a typ vozidla
a počet kilometrů získej jako parametry funkce __init__ a ulož je jako atributy objektu.
Poslední atribut nastav jako True, tj. na začátku je vozidlo volné.

Vytvoř objekty, které reprezentují všechny automobily půjčovny.

Třídě Auto přidej metodu pujc_auto(), která nebude mít (kromě obligátního self) žádný parametr.
Funkce zkontroluje, jestli je vozidlo aktuálně volné. Pokud je volné, změní hodnotu atributu,
který určuje, zda je vozidlo půjčené, a vrátí text "Potvrzuji zapůjčení vozidla".
Pokud je vozidlo již půjčené, vrátí text "Vozidlo není k dispozici".

Dále tříde Auto přidej funkci get_info(), která vrátí informaci o vozidle (stačí registrační
značka a značka a typ vozidla) jako řetězec.

Nakonec do programu (mimo třídu) napiš dotaz na uživatele, jakou značku si uživatel přeje půjčit.
Uživatel může zadávat hodnoty Peugeot nebo Škoda. Jakmile si uživatel vybere značku,
vypiš informaci o vozidle pomocí funkce get_info() a následně použij funkci pujc_auto().

Otestuj, že program nedovolí půjčit stejné auto dvakrát.
"""

class Vehicle():
  def __init__(self, spz, brand_type, kilometers, availability = True):
    self.spz = spz
    self.brand_type = brand_type
    self.kilometres = kilometers
    self.availability = availability

  def __str__(self):
    return f"Vybrali jste vozidlo {self.brand_type} s poznavaci znackou {self.spz} a {self.kilometres} najetymi kilometry."

  def get_vehicle(self):
    if self.availability == True:
      self.availability = False
      print(f"Vozidlo je volne. Potvrzuji zapujceni vozidla")
    else:
      print(f"Vozidlo neni k dispozici.")


vehicle = input("Jake vozidlo si chcete vypujcit? ")
if vehicle == "Škoda":
  vehicle = Vehicle("1P3 4747", "Škoda Octavia", 41253)
elif vehicle == "Peugeot":
  vehicle = Vehicle("4A2 3020", "Peugeot 403 Cabrio", 47534)
else:
  vehicle = f"Toto auto nemame."

print(vehicle)
vehicle.get_vehicle()
vehicle.get_vehicle()
