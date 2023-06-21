teploty = [10, 13, 15, 18, 17, 12, 12]

for i in range(7):
    print(f'{i}. den {teploty[i]}')




#vypocita minimum , maximum a priemer hodnot zoznamu
sucet = 0
maximum = minimum = teploty[0]
for prvok in teploty:
    sucet += prvok
    if prvok < minimum:
        minimum = prvok
    if prvok > maximum:
        maximum = prvok
priemer = sucet / 7
print(f'priemerna teplota je {priemer:.1f}')  # fornatovanie desatinneho cisla na jedno miesto
print(f'minimalna teplota je {minimum}')
print(f'maximalna teplota je {maximum}')

#prechadzanie listom a zmena hodnot pomocou cyklu.. kazda teplota sa zvysi o 2
for i in range(len(teploty)):
    teploty[i] += 2
print(teploty)

# minimum maximum a priemer ale teraz pomocou funkcii listu (pola)
sucet = sum(teploty)
maximum = max(teploty)
minimum = min(teploty)
priemer = sucet / len(teploty)
print(f'priemerna teplota je {priemer:.1f}')
print(f'minimalna teplota je {minimum}')
print(f'maximalna teplota je {maximum}')

# funkcia list() parametrom musí byť iterovateľná hodnota, t.j. nejaká postupnosť, ktorá sa dá prechádzať (iterovať), napr. for-cyklom
#  -funkcia list() túto postupnosť rozoberie na prvky a z týchto prvkov poskladá nový zoznam
# - parameter môže chýbať, vtedy vygeneruje prázdny zoznam

print(list(teploty))    # tu len vytvori kopiu uz existujuceho listu
print(list(range(5, 16)))  # vytvori zoznam od 5 do 15
print(list('Python'))


# metody pola append , pop , sort, remove,

pole = [1,8,34,54,1,8,3,0,7,8,15]
print(pole)
pole.append(99)
print(pole)
pole.pop()              #odstrani posledny prvok
print(pole)
pole.insert(3,999)
print(pole)
pole.pop(3)         # odstrani prvok s INDEXOM 3
print(pole)
pole.remove(54)   # odoberie prvok 54 
print(pole)
pole.sort()
print(pole)
print(pole.count(8))
print(pole.index(8))
