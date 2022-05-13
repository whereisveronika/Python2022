"""
Stáhni si dataset, který obsahuje seznam zvířat k adopci v ZOO Praha. Zdroj dat je Národní katalog otevřených dat.
Data si načti pomocí metody pandas.read_csv(). Pozor, nastav oddělovač na znak středníku. Využij parametr sep.
Seznam se s daty. Kolik má tabulka řádek a sloupců? Jak se sloupce jmenují?
Které zvíře se nachází na záznamu s indexem 34? Vypiš pomocí iloc název tohoto zvířete v češtině i angličtině.

#Bonus
V lekci jsme zmínili, že existují i jiné typy indexů, než jen číselný, který sám vyrobí pandas. Například v kontextu
souboru se zvířaty se nabízí hned několik sloupců, které bychom mohli využít jako index, které nejsou číselné.

Načti znovu data, ale tentokrát nastav parametr index_col na název sloupce, který obsahuje název zvířete v češtině.
Všimni si, že sloupec teď povýší na index a už se nenachází mezi "běžnými" sloupci.

Pomocí <tvoje-promenna>.index.is_unique ověř, zda je nový index unikátní.

Seřazený index je efektivnější a přehlednější. Seřaď index pomocí metody .sort_index().
Bacha, metoda vrátí novou tabulku se seřazeným indexem. Budeš tedy chtít přepsat původní tabulku.

Vyhledej řádek indexovaný názvem "Outloň váhavý". Namísto metody .iloc využij .loc.

Rozsahy fungují podobně jako u číselných indexů. Vyhledej záznamy mezi "Želva Smithova" a "Želva žlutočelá".
"""

import pandas

zvirata = pandas.read_csv("zvirata.txt", sep=";")

#print(zvirata.info())
#print(zvirata.columns)
#print(zvirata.head())
#print(zvirata.iloc[34])
names = zvirata.iloc[34, [1, 2]]
cz_name = zvirata.iloc[34, 1]
en_name = zvirata.iloc[34, 2]

print(names)
print(cz_name)
print(en_name)

# BONUS

zvirata = pandas.read_csv("zvirata.txt", sep=";", index_col="nazev_cz")
#print(zvirata.head())
#print(zvirata.index.is_unique)

seradit = zvirata.sort_index()
#print(seradit.head())
hledat = seradit.loc["Outloň váhavý"]
#print(hledat)
hledat = seradit.loc[["Želva Smithova", "Želva žlutočelá"]]
print(hledat)