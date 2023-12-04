#iteracyjnie
def potega(liczba, n):
    wynik = liczba
    for i in range(1, n):
        wynik *= n
    return wynik

print(potega(2, 2))

#rekurencyjnie
def potegaRek(liczba, n):
    if n == 1:
        return liczba*n
    else:
        return liczba * potega(liczba, n-1)

print(potegaRek(2, 2))

