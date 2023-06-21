def print_stars(num):
    print("* "*num)


def pyramida(pocet):
    for i in range(1,pocet*2):
        print_stars(pocet-abs(pocet-i))    

def trojuholnik(pocet):
    for i in range(1,pocet+1):
        print_stars(i)

def stvorec(pocet):
    for i in range(1,pocet+1):
        print_stars(pocet)

print("Pyramida")
pyramida(5)
print("Trojuholnik")
trojuholnik(5)
print("Stvorec")   
stvorec(3)     