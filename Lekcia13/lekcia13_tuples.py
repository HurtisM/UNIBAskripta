# definovanie matice 3x3
m = [[1,2,3],[4,5,6],[7,8,9]]


#vypis po riadkoch
for riadok in m:
    print(riadok)

# vypis po prvkoch
for riadok in m:
    for prvok in riadok:
        print(prvok, end=' ')
    print()    
 # vypis pomocou indexovania

for i in range(len(m)):
    for j in range(len(m[i])):
        print(m[i][j], end =' ') 
    print()

# maticu mozeme aj definovat pomocou cyklov
matica = []
for i in range(3):
    matica.append([0, 0, 0])

print(matica)

#funkcia na "vyrobenie" matice - prvky su nuly
def vyrob(pocet_riadkov, pocet_stlpcov, hodnota=0):
    vysl = []
    for i in range(pocet_riadkov):
        vysl.append([hodnota] * pocet_stlpcov)
    return vysl

def vypis(tab):
    for i in range(len(tab)):
        for j in range(len(tab[i])):
            print(tab[i][j], end=' ')
        print()

def ocisluj(tab):
    poc = 0
    for i in range(len(tab)):
        for j in range(len(tab[i])):
            tab[i][j] = poc
            poc += 1

matica2 = vyrob(5,4)
vypis(matica2)
ocisluj(matica2)
vypis(matica2)