#2.feladat:
f = open("EUcsatlakozas.txt","r",)
lista = []
for sor in f:
    lista.append(sor.strip().split(";"))
f.close()

#3.feladat: EU tagállamainak száma:
print(f"3. feladat: EU tagállamainak száma: {len(lista)} db")

#4.feladat: 2007-ben csatlakozott.
csatlakozot = 0
for sor in lista:
    if sor[1][0:4] == "2007":
        csatlakozot += 1
print(f"4. feladat: 2007-ben {csatlakozot} ország csatlakozott.")

#5.feladat: Magyarország csatlakozási dátuma :
magyarorszag = 0
for sor in lista:
    if sor[1][5:7] == "05":
        magyarorszag = sor[1]
print(f"5. feladat: Magyarország csatlakozási dátuma : {magyarorszag}")

#6.feladat:Májusban csatlakozás
csatlakozas = "nem volt"
for sor in lista:
    if sor[0] == "Magyarország":
        csatlakozas = "volt"
print(f"6. feladat: Májusban {csatlakozas} csatlakozás")

#7. feladat: Legutoljára csatlakozott ország:
last = ''
for sor in lista:
    if last < sor[1]:
        last = sor[1]
        orszag = sor[0]
print(f"7. feladat: Legutoljára csatlakozott ország: {orszag}")

#8.feladatL:
statisztika = dict()
for sor in lista:
    ev = sor[1][:4]
    statisztika[ev] = statisztika.get(ev,0) + 1
print(f"8. feladat: statisztika")
for sor in statisztika.items():
    print(f'      {sor[0]} - {sor[1]} ország')

        


