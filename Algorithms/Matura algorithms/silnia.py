#Iteracyjnie
def silnia(liczba):
    wynik = 1
    liczba = int(liczba)
    if liczba == 1:
        return 1
    else:
        for i in range(2, liczba+1):
            wynik*=i
    return wynik

print(silnia(5))

#Rekurencyjnie
def silniaRek(liczba):
    liczba = int(liczba)
    if liczba == 1:
        return 1
    else:
        return liczba * silniaRek(liczba-1)

print(silniaRek(5))

#Rekurencyjnie2
def silnia_rekurencyjnie(n): return n*silnia_iteracyjnie(n-1) if n > 1 else 1

print(silnia_rekurencyjnie(5))
