"""
Vytvoř program na prodej vstupenek do letního kina. Ceny vstupenek jsou v tabulce níže.

Datum	Cena
1. 7. 2021 - 10. 8. 2021	250 Kč
11. 8. 2021 - 31. 8. 2021	180 Kč
Mimo tato data je středisko zavřené.

Tvůj program se nejprve zeptá uživatele na datum a počet osob, pro které uživatel chce vstupenky koupit.
Uživatel zadá datum ve středoevropském formátu. Převeď řetězec zadaný uživatelem na datum pomocí funkce
datetime.strptime().

Pokud by uživatel zadal příjezd mimo otevírací dobu, vypiš, že letní kino je v té době uzavřené.
Pokud je letní kino otevřené, spočítej a vypiš cenu za vstupenky.

Data lze porovnávat pomocí známých operátorů <, >, <=, >=, ==, !=. Tyto operátory můžeš použít v podmínce if.
Níže vidíš příklad porovnání dvou dat. Program vypíše text "První datum je dřívější než druhé datum.".
"""
from datetime import *

datum = input("Kdy prijdete do kina? ")
osoby = int(input("Kolik kupujete vstupenek? "))

datum = datetime.strptime(datum, "%d.%m.%Y")
otevreno = datetime(2022, 7, 1)
zmena_ceny = datetime(2022, 8, 11)
zavreno = datetime(2022, 8, 31)

if datum < otevreno or datum > zavreno:
  print(f'Mame otevreno pouze v lete od 1.7.2022 do 31.8.2022. Vyberte jine datum.')
elif datum > otevreno and datum < zmena_ceny:
  cena_vstupenek = osoby * 250
  print(f'Kupujete vstupenky pro {osoby} lidi a zaplatite {cena_vstupenek} korun.')
else:
  cena_vstupenek = osoby * 180
  print(f'Kupujete vstupenky pro {osoby} lidi a zaplatite {cena_vstupenek} korun.')


