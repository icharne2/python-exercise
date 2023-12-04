def czynniki(liczba):
    czynniki = []
    liczba = int(liczba)
    dzielnik = 2

    while liczba != 1:
        while liczba%dzielnik == 0:
            czynniki.append(dzielnik)
            liczba = int(liczba/dzielnik)
        dzielnik+=1
    print(czynniki)

czynniki(6)
