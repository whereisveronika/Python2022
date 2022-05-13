"""
Stáhni si soubor temperature.csv, který obsahuje informace o průměrné teplotě v různých městech v listopadu 2017.

Vypiš si prvních několik řádků, ať si prohlédneš strukturu tabulky.

Dále napiš následující dotazy:

Dotaz na měření, která byla provedena v Praze. Je na datech něco zvláštního? Napadá tě, čím to může být? Nápověda:
Dotaz na měření, ve kterých je teplota (sloupec AvgTemperature) vyšší než 80 stupňů.
Dotaz na měření, ve kterých je teplota vyšší než 60 stupňů a současně bylo měření provedeno
v regionu (sloupec Region) Evropa (Europe).
Dotaz na extrémní hodnoty, tj. měření, ve kterých je teplota vyšší než 80 stupňů nebo menší než - 20 stupňů.
---------------------------------------------------------------------------------------------------------------------
BONUS
Nainstaluj si modul pytemperature a zkus si vytvořit nový sloupec, který bude obsahovat
průměrnou templotu ve stupních Celsia.

Ve svém programu nejprve proveď import modulu pytemperature. Nový sloupec pak přidáš do tabulky tak,
že nalevo od = vložíš tabulku a název nového sloupce do hranatých závorek.
Napravo pak můžeš provádět výpočty pomocí již existujících sloupců. Můžeš např. použít funkci f2c
z modulu pytemperature, která převede teplotu ze stupňů Fahrenheita na stupně Celsia.

import pytemperature
df["AvgTemperatureCelsia"] = pytemperature.f2c(df["AvgTemperature"])
Nyní můžeš zpracovat následující příklady:

Dotaz na měření, ve kterých je teplota (sloupec AvgTemperatureCelsia) vyšší než 30 stupňů Celsia.
Dotaz na měření, ve kterých je teplota vyšší než 15 stupňů Celsia a současně bylo měření
provedeno v regionu (sloupec Region) Evropa (Europe).
Dotaz na extrémní hodnoty, tj. měření, ve kterých je teplota vyšší než 30 stupňů Celsia nebo
menší než -10 stupňů. Jsou některé hodnoty podezřelé?
--------------------------------------------------------------------------------------------------------------------
BONUS 2
Pokračuj ve své práci s informacemi o průměrných teplotách. Pokud jsi zpracoval/a první bonus,
můžeš pracovat s teplotami ve stupních Celsia.

Napiš následující dotazy:

Dotaz na řádky z 13. listopadu 2017 (sloupec Day musí mít hodnotu 13).
Dotaz na řádky z 13. listopadu 2017 ze Spojených států amerických (sloupec Day musí mít hodnotu 13 a sloupec
Country hodnotu US). Výsledek dotazu si ulož do nové tabulky a použij ji jako vstup pro následující dotaz.
Pro data z předchozího dotazu napiš dotaz na řádky ve městech (sloupec City) Washington a Philadelphia.
"""

import pandas
teplota = pandas.read_csv("temperature.txt")

#print(teplota.head())

#mesto = input("Zadejte mesto: ")
#mesto = teplota.loc[teplota["City"] == mesto]
#print(mesto)

""" Puvodne jsem mela nastavene mesto jako index, ale nedavalo to smysl kvuli unikatnosti. """

vysoke = teplota[teplota["AvgTemperature"] > 80]
#print(vysoke)

teplota_regionu = teplota[(teplota["AvgTemperature"] > 60) & (teplota["Region"] == "Europe")]
#print(teplota_regionu)

extremni_teploty = teplota[(teplota["AvgTemperature"] > 80) | (teplota["AvgTemperature"] < (-20))]
#print(extremni_teploty)

# BONUS

import pytemperature
teplota["AvgTemperatureCelsius"] = pytemperature.f2c(teplota["AvgTemperature"])
#print(teplota.head())
nad_tricet = teplota[teplota["AvgTemperatureCelsius"] > 30]
#print(nad_tricet)
teplota_regionu = teplota[(teplota["AvgTemperatureCelsius"] > 15) & (teplota["Region"] == "Europe")]
#print(teplota_regionu)
extremni_teploty = teplota[(teplota["AvgTemperatureCelsius"] > 30) | (teplota["AvgTemperatureCelsius"] < (-10))]
#print(extremni_teploty)

# BONUS 2

den = teplota[teplota["Day"] == 13]
#print(den)
stat = teplota[(teplota["Day"] == 13) & (teplota["Country"] == "US")]
#print(stat)
us_mesta = teplota[(teplota["Day"] == 13) & (teplota["Country"] == "US") & ((teplota["City"] == "Philadelphia") | (teplota["City"] == "Washington"))]
print(us_mesta)