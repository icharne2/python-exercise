#iteracyjnie - Euklides
def nwd(liczba1, liczba2):
    liczba1 = int(liczba1)
    liczba2 = int(liczba2)
    while liczba2 != 0:
        liczba1, liczba2 = liczba2, liczba1%liczba2
    return liczba1

print(nwd(5,25))

#rekurencyjnie
def nwd2(liczba1, liczba2):
    liczba1 = int(liczba1)
    liczba2 = int(liczba2)
    while liczba2 != 0:
        return nwd2(liczba2, liczba1%liczba2)
    return liczba1

print(nwd2(5, 25))

#nww
def nww(liczba1, liczba2):
    return (liczba1*liczba2)//nwd2(liczba1, liczba2)    # // dzielenie całkowite

print(nww(5, 25))
