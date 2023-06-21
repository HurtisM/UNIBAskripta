# Na jedniný riadok výstupu vypíš štyri rôzne prvočísla a,b,c,d pričom musí platiť 40< a,b,c,d < 1000
# a zaroven |a-b| = |c-d| = 2
def primes(n):
    out = list()
    sieve = [True] * (n+1)
    for p in range(2, n+1):
        if (sieve[p]):
            out.append(p)
            for i in range(p, n+1, p):
                sieve[i] = False
    return out
 
zoznam = primes(1000)

dvojicky = []
for i in range(len(zoznam)-1):
    if zoznam[i] >40:
        if zoznam[i+1] - zoznam[i] == 2:
            dvojicky.append(zoznam[i])
            dvojicky.append(zoznam[i+1])
        if len(dvojicky) == 4:
            break    


for i in range(4):
    print(dvojicky[i], end=' ')