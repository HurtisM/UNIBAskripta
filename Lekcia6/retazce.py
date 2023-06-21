# zisti ci sa dany znak nachadza v retazci
def zisti(znak, retazec):
    for z in retazec:
        if z == znak:
            return True
    return False

x = zisti('q','Martin')
print(x)

# to iste sa da aj binarnou operaciou in
print( 'ar' in 'Martin')
#negacia sa robi dvoma sposobmi  if no a not in...  druhy sposob je pouzivanejsi
retazec = "Martin"
print(retazec)
if not 'a' in retazec:
    print("Nie je tam")
if 'az' not in retazec:
    print("Nie je tam 2")

# znaky v retazci su indexovane od nuly
a = 'Python'
for i in range(len(a)):
    print(i, a[i])    
# zaporne indexovanie, Znaky reťazca sú indexované od -1 do -len()
a = 'Python'
for i in range(1, len(a)+1):
    print(-i, a[-i])    


#Python na porovnávanie používa vnútornú reprezentáciu Unicode (UTF-8). S touto reprezentáciou môžeme pracovať pomocou funkcií ord() a chr():
# funkcia ord(znak) vráti vnútornú reprezentáciu znaku (kódovanie v pamäti počítača)
# opačná funkcia chr(číslo) vráti jednoznakový reťazec, pre ktorý má tento znak danú číselnú reprezentáciu
print(ord('A'))
print(chr(65))



