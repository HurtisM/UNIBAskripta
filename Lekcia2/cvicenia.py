""" 1.Program prečíta nejaké slovo a jedno celé číslo n, potom vypíše n-riadkov, 
pričom v každom bude niekoľko znakov bodka a toto zadané slovo: 
v prvom riadku výpisu bude pred slovom n-1 znakov '.', v každom ďalšom bude o bodku menej """

n = int(input('zadaj cislo: '))
slovo = input('zadaj slovo: ')

for i in range(n):
    print('.'*(n-i-1),slovo)

"""2.  Program prečíta nejaké slovo a jedno celé číslo n, potom vypíše n-riadkov: 
v prvom je zadané slovo raz, v druhom je 2-krát (slová sú oddelené medzerou), 
v treťom 3-krát (tiež s medzerou medzi slovami), atď. Použite len jeden cyklus. """   

n = int(input('zadaj cislo: '))
slovo = input('zadaj slovo: ')

for i in range(1,n+1):
    print(i*(slovo + " "))

"""3.Program prečíta dve celé čísla od a do 
a vypíše tabuľku druhých a tretích mocnín všetkých čísel z intervalu <od, do>."""    

od = int(input('zadaj od: '))
do = int(input('zadaj do: '))

for i in range(od,do+1):
    print(i, i**2, i**3)

"""4. Program prečíta celé číslo a vypíše počet cifier a tiež ciferný súčet tohto čísla. Číslo preveďte na znakový reťazec (resp. ho po prečítaní neprevádzajte na číslo) 
a potom postupne pomocou for-cyklu prechádzajte jeho cifry (jednoznakové reťazce), každú preveďte na číslo a pripočítajte k výslednému súčtu."""    

cislo = input('zadaj cislo: ')
pocet_cifier = len(cislo)
ciferny_sucet = 0

for i in cislo:
    ciferny_sucet += int(i)

print("cislo", cislo, " ma ",pocet_cifier,"cifier a ciferny sucet je ",ciferny_sucet)

"""5.Program prečíta celé číslo (maximálne 8-ciferné) a potom v cykle (8-krát) postupne toto číslo skracuje o poslednú cifru, 
zároveň vypisuje skrátené číslo aj poslednú cifru, o ktorú bolo skrátené."""

cislo = input('zadaj cislo:')

for i in range(1,9):
    print(cislo[0:-i], cislo[-i])

    