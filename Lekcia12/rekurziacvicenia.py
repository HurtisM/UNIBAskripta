def retazec(n):
    if n == 0:
        return ''
    if n == 1:
        return 'a'
    return retazec(n-2) + '+' + retazec(n-1)


def w(n):
    s = 0
    while n:
        s += n + w(n-1)
        n -= 1
    return s    



# Funkcia urob(a, b)  počíta bez cyklov súčin dvoch nezáporných celých čísel a to len pomocou sčitovania.
def urob(a, b):
    if a == 0:
        return 0
    return b + urob(a - 1, b)

# funkcia umocni vypočíta mocninu a**b ale bez cyklu a bez násobenia - na násobenie použite funkciu urob()
def umocni(a,b):
    if b==0:
        return 1
    return urob(a,umocni(a,b-1))


def nsd(a,b):
    if b == 0: return a
    return nsd(b, a%b)



def vypis(n):
    if n<1:
        pass
    else:
        #print(n, end=',')  
        vypis(n-1)
        print(n,end='.')




print(umocni(3,7))
print(nsd(40,24))
vypis(10)