# funkcia type() vráti typ zadanej hodnoty
# funkcie int(), float() a str() pretypujú zadanú hodnotu na iný typ
# funkcie print() a input() sú určené na výpis textov a prečítanie textu zo vstupu
# funkcie abs() a round() počítajú absolútne hodnoty čísel a zaokrúhľujú desatinné čísla
# funkcie round() a reversed() generujú postupnosť čísel, resp. ju otáčajú

import math

for uhol in range(0, 91, 5):
    uhol_v_radianoch = math.radians(uhol)
    sin_uhla = math.sin(uhol_v_radianoch)
    cos_uhla = math.cos(uhol_v_radianoch)
    print(uhol, sin_uhla, cos_uhla)

#krajsi zapis   
for uhol in range(0, 91, 5):
    uhol_v_radianoch = math.radians(uhol)
    sin_uhla = math.sin(uhol_v_radianoch)
    cos_uhla = math.cos(uhol_v_radianoch)
    print(f'{uhol:3} {sin_uhla:6.3f} {cos_uhla:6.3f}')    

""" MModul random
Aj tento modul obsahuje knižnicu funkcií, ale tieto umožňujú generovanie náhodných čísel. 
My z tejto knižnice využijeme najmä tieto dve funkcie:

randrange() vyberie náhodné číslo z postupnosti celých čísel
choice() vyberie náhodný prvok z nejakej postupnosti, napr. zo znakového reťazca (postupnosti znakov)     """

import random

for i in range(100):
    nahodne = random.randrange(1, 7)
    print(nahodne, end=' ')

print()

for i in range(100):
    nahodne =  random.choice('aeiouy')
    print(nahodne, end = ' ')