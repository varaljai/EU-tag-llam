"""
Ausztria;1995.01.01
Belgium;1958.01.01
"""
# 2. feladat:

f = open("EUcsatlakozas.txt",encoding="latin2")
lista = []
for sor in f:
    lista.append(sor.strip().split(";"))
f.close()

# 3.feladat 2018 tagállamok

print(f"3. feladat: EU tagállamainak száma: {len(lista)} db")

# 4.feladat: 2007-ben {} ország csatlakozott.

szamlalo = 0
for sor in lista:
    if sor[1][:4] == "2007":
        szamlalo += 1
print(f"4. feladat: 2007-ben {szamlalo} csatlakozott. ")

#5.feladat: Magyarország csatlakozási dátuma : {}
for sor in lista:
    if sor [0] == "Magyarország" :
        print(f"5.feladat: Magyarország csatlakozási dátuma : {sor[1]}")

#6.feladat: Májusban {} csatlakozás

csatlakozasa = "nem volt"
for sor in lista:
    if sor[1][5:7] == "05":
        csatlakozasa = "volt"
print(f"6.feladat: májusban {csatlakozasa} csatlakozás!")
        
#7.feladat: legutoljára csatlakozás ország :{}
utoljara = ""
for sor in lista:
    if utoljara < sor[1]:
        utoljara = sor[1]
        orszag = sor[0]
print(f"7.feladat: legutoljára csatlakozás ország :{orszag}")

#8.feladat: statisztika
statisztika = dict()
for sor in lista:
    ev = sor[1][0:4]
    statisztika[ev] = statisztika.get(ev,0) + 1
for sor in statisztika.items():
    print(f"{sor[0]} - {sor[1]} ország")
        

        


