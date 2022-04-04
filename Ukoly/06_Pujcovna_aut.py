"""
Půjčovna aut má v každém kraji ČR jedno auto s danou SPZ. Ke konci roku chce zjistit,
kolik všechna auta najezdila dohromady kilometrů. V souboru seznam_aut.txt je pro každou SPZ zaznamenáno
kolik dané auto ujelo kilometrů za daný rok. Hodnoty jsou v tisících kilometrů.
Bohužel se v jednotlivých krajích blbě zkoordinovali a někdo používal desetinnou čárku, někdo zase tečku.

Napište program, který na výstup vypíše součet všech ujetých kilometrů.

Napoveda:
s = "Nejradši mám koláče."
print(s.replace("koláče", "svíčkovou"))

Krom metod str (převod na řetězec) a int (převod na celé číslo) existuje
i metoda float (převod na desetinné číslo).

BONUS: Upravte váš program tak, aby jméno souboru k otevření zadal uživatel,
abychom mohli takto zpracovávat výkazy z různých souborů, aniž bychom museli upravovat samotný kód programu.
Program ověřte tak, že si soubor auta.txt přejmenujete, nebo si vytvořte nový.
"""

soubor = input("Zadejte jmeno souboru (nezapomente na priponu .txt): ")

with open(soubor, encoding='utf-8') as vstup:
  auta = vstup.readlines()

#print(auta)

auta = [auto.strip() for auto in auta]
auta = [auto.replace(",", ".") for auto in auta]
auta = [auto.split() for auto in auta]
auta = [[auto[0], round(float(auto[1])*1000, 0)] for auto in auta]
auta = [sum([auto[1]]) for auto in auta]
print(f'Dohromady auta najela {sum(auta)} kilometru.')