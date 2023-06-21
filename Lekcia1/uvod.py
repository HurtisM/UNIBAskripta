## Základné typy údajov
## Videli sme, že hodnoty (konštanty alebo výrazy) môžu byť rôznych typov. V Pythone má každý typ svoje meno:

## int pre celé čísla, napr. 0, 1, 15, -123456789, …
## float pre desatinné čísla, napr. 0.0, 3.14159, 2.0000000001, 33e50, …
## str pre znakové reťazce, napr. 'a', "abc", '', "I'm happy"

cislo = 1247
desatinne = 14.24
retazec = 'toto su znaky ..24.. aj tie cisla'

# na zistenie typu  premennej sluzi funcia type()

print(cislo, type(cislo))
print(desatinne, type(desatinne))
print(retazec, type(retazec))

# operacie s integermi:  + - *  je jasne.. ale // celociselne delenie  % -zvysok po deleni a ** -uocnovanie
print('7+5=',7+5,'  8-6=',8-6,'  5*12=',5*12)
print('24 // 7=',24//7, ' zvysok sa nvypise')
print('24 % 7=',24%7, ' tu sa vypise iba zvysok')
print('4**3=',4**3 , '  4 na tretiu')

# operacie s float (desatinnymi cislami)  + - * su rovnake ako predchadzajuce  / je obycajne deleni
# // delenie zaokruhlene nadol (celociselne)  % zvysok po deleni a ** umocnovanie je tiez rovnake 
print('*****************************************')
print('7+5=',7.4+5,'  8-6=',8-6.4,'  5*12=',5.2*12)
print('24 // 7=',24.0//7, ' zvysok sa nvypise')
print('24 % 7=',24.0%7, ' tu sa vypise iba zvysok')
print('4**3.2=',4**3.2 , '  4 na tretiu')

# takisto aj retazce mozeme scitat pomocou + alebo nasobit (len s integerom ) pomocou *
print('*****************************************')
str1 ='Monty'
str2 ='Python'
print(str1 + str2) # toto je ale bez medzery
print(str1 + ' ' + str2) # uz s medzerov
print('Ahoj ' + 'Python')
print('python ' * 4)

# print a input..
meno = input('Ako sa volas? ')
print('Ahoj ', meno)

# mena typov sluzia aj na pretypovanie (konvertovanie) premennych
# napr. int(3.14) da 3..  float(24) -> 24.0  a str(145) -> '145'

retazec = input('zadaj eura: ')
suma = float(retazec)               # pretypovanie
koruny = suma * 26
print(suma, 'euro je', koruny, 'korun')

print('zadana suma v euro je', float(input('zadaj eura: ')) * 26, 'korun') # to iste , len na jeden riadok.. pythonisticky pristup


# zabudovane funkcie abs()  a round()
a = -547.2475
print(abs(a))
print(round(a))
print(round(a,2))

# paralelne priradenie. viac premennych v jednom riadku:
x,y,z = 12,'ahoj',15.24

#preto funguje aj "prehodenie" hodnot dvoch premennych bez pomocnej premennej
a=10
b=25.8
print(a,b)
a,b = b,a
print(a,b)
p1, p2, p3 = 11, 22, 33
print(p1,p2,p3)
p1, p2, p3 = p2, p3, p1
print(p1,p2,p3)
a, b, c, d, e, f = 'Python'
print(a, b, c, d, e, f)

string = (input('zadaj cislo'))
print('posledne tri cifry cisla:', string, 'su', string[-3:-2], string[-2:-1], 'a' ,string[-1:])
