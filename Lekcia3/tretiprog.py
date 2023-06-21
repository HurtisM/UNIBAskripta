

#vypise vsetky delitele cisla
def delitele(cislo):
    zoznam_delitelov = ""
    for i in range(1,cislo+1):
        if cislo % i == 0:
            zoznam_delitelov += str(i) + " "
    return zoznam_delitelov

# vypise sucet vsetkych delitelov zadaneho cisla
def sucet_delitelov(cislo):
    sucet = 0
    for i in range(1,cislo+1):
        if cislo % i == 0:
            sucet += i
    return sucet

# Zisti ci cilo je dokonale => sucet delitelov = cislu
def je_dokonale(cislo):
    sucet = 0
    for i in range(1,cislo):
        if cislo % i == 0:
            sucet += i
    if sucet == cislo:
        return True
    return False            

# vypise vsetky dokonale cisla z untervalu
def vsetky_dokonale(od,do):
    if od <= 0: od = 1
    for cislo in range(od , do+1):
        sucet = 0
        for i in range(1,cislo):
            if cislo % i == 0:
                sucet +=i
        if sucet == cislo:
            print(cislo , " je dokonale")
    return                


#najvacsi spolocny delitel - Euklidov algoritmus
def nsd(a,b):
    if b == 0: return a
    return nsd(b, a%b)

# funcia vrati POCET delitelov zadaneho cisla
def pocet_delitelov(cislo):
    pocet = 0
    for i in range(1,cislo+1):
        if cislo % i == 0:
            pocet += 1
    return pocet

#funkcia pomocou predchadzajucej funkcie zisti ci cislo je prvocislo..
def je_prvocislo(cislo):
    pocet = 0
    for i in range(1,cislo+1):
        if cislo % i == 0:
            pocet += 1
    if pocet == 2: return True
    return False
 

# funkcia zisti prvocisla z intervalu (a,b)   a>=0
def vsetky_prvocisla(a,b):
    for i in range(a,b+1):
        if je_prvocislo(i): print(i, end=" ") 

#funkcia vrati sucet mocnin dvojky  s exponentmi menšími ako n  

def sucet_mocnin2(n):
    sucet = 0
    for i in range(n):
        sucet += (2**i) 
    return sucet    

def sucet_mocnin2a(n):
    sucet = 0
    for i in range(n):
        sucet += 1/(2**i) 
    return sucet  

for i in range(15):
        print(i, sucet_mocnin2(i), sucet_mocnin2a(i))

vsetky_dokonale(0,100)