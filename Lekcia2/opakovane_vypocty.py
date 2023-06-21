# For cyklus
# cyklus s danym poctom opakovani

for i in range(4):          #range(pocet opakovani)  0-n-1, teda pre n=4 sa vypise 4krat ale nedosiahne hodnotu 4!
    print(i, 'riadok')

n = int(input('zadaj n: '))
pocet = 0
for i in range(n):
    pocet = pocet + 1
print('pocet prechodov cyklu =', pocet)    


# cyklus s vymenovanymi hodnotami
#Namiesto funkcie range(n), ktorá pre nás vygenerovala postupnosť čísel od 0 do n-1,
# sme vymenovali presné poradie hodnôt, pre ktoré sa postupne v cykle vykoná blok prikazov. 
# Vymenované hodnoty musia byť oddelené čiarkou a mali by byť aspoň dve.

for x in 5, 7, 11, 13, 23:
    x2 = x ** 2
    print('druhá mocnina', x, 'je', x2)

# Vymenované hodnoty sa môžu aj ľubovoľne opakovať, napr.
i = 1
for prem in 2, 1, 7, 2, 3:
    print(i, 'prechod cyklu s hodnotou', prem)
    i = i + 1

## Okrem toho, že sa hodnoty môžu opakovať, nemáme obmedzenia ani na typy vymenovaných hodnôt.
# 
for hodnota in 3.14, abs(7 - 123), 'text', 100 / 4, abs, '42':
    print(hodnota, type(hodnota))


# cyklus moze prechadzat aj cez retazec po jednotlivych znakoch
for znak in 'python':
    print(znak)

vstup = input('zadaj: ')
pocet = 0
retazec1 = retazec2 = ''
for znak in vstup:
    retazec1 = retazec1 + znak
    retazec2 = znak + retazec2
    pocet = pocet + 1
print('pocet znakov retazca =', pocet)
print('retazec1 =', retazec1)
print('retazec2 =', retazec2)    
