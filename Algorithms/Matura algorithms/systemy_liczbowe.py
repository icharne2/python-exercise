#Z 10 na inny, max 16:
def zamiana(liczba, system):
    liczba = int(liczba)
    system = int(system)
    wynik = []
    while liczba:
        if liczba%system == 0:
            wynik.insert(0,0)
        else:
            if liczba%system >= 10:
                if liczba%system == 10:
                    wynik.insert(0, 'A')
                elif liczba%system == 11:
                    wynik.insert(0, 'B')
                elif liczba%system == 12:
                    wynik.insert(0, 'C')
                elif liczba%system == 13:
                    wynik.insert(0, 'D')
                elif liczba%system == 14:
                    wynik.insert(0, 'E')
                elif liczba%system == 15:
                    wynik.insert(0, 'F')
            else:
                wynik.insert(0,liczba%system)
        liczba = int(liczba/system)
    return wynik

print(zamiana(8,2))

#Na bin:

def bin(liczba, system):
    liczba = int(liczba)
    lista = list(str(liczba))
    system = int(system)
    i = len(lista)-1
    wynik = 0
    for value in lista:
        if system < 10:
            wynik += int(value)*(system**i)
        else:
            if value == 'A':
                wynik = 10 * (system ** i)
            elif value == 'B':
                wynik = 11 * (system ** i)
            elif value == 'C':
                wynik = 12 * (system ** i)
            elif value == 'D':
                wynik = 13 * (system ** i)
            elif value == 'E':
                wynik = 14 * (system ** i)
            elif value == 'F':
                wynik = 15 * (system ** i)
        i-=1
    return wynik

print(bin('011',2))