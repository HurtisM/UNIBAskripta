""" vstup = input('zadaj: ')
pocet = 0
retazec1 = retazec2 = ''
for znak in vstup:
    retazec1 = retazec1 + znak
    retazec2 = znak + retazec2
    pocet = pocet + 1
print('pocet znakov retazca =', pocet)
print('retazec1 =', retazec1)
print('retazec2 =', retazec2)   
if retazec1 == retazec2:
    print("Retazec:",vstup," je palindrom")   """    

""" vstup = input('zadaj slovo: ') 
pocet = int(input("zadaj n:"))

for i in range(pocet):
    pocet -= 1
    print("." * pocet, vstup)

vstup = input('zadaj slovo: ') 
pocet = int(input("zadaj n:"))

for i in range(pocet):
    i+= 1
    print( i* (vstup+" "))


od = int(input("zadaj od:"))
do = int(input("zadaj do:")) 
retazec = ""

for i in range(od,do+1):
    retazec = retazec + str(i)+ " " +str(i*i) + " " + str(i*i*i) + "\n"

print(retazec) """

cislo = int(input("zadaj cislo:"))
medzera =0
while cislo > 0:
    print(" "* medzera , end= "")
    for i in range(1,cislo+1):
        print(i, end = " ")
    print()
    cislo -=1 
    medzera +=1   

cislo = int(input("zadaj cislo:"))
for riadok in range(cislo):
    print(" " * riadok, end="")
    for i in range(1,cislo+1):
        print( i, end =" ")
    print()
    cislo -=1    

cislo = int(input("zadaj cislo:"))
for j in range(cislo):
    print("  " * j, end="")
    for i in range(1,cislo*2):
        print(cislo-abs(cislo-i), end =" ")   
    print()    
    cislo -=1     