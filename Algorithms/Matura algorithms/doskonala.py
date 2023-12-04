def czy_doskonala(liczba):
    sumDzielnikow = 1
    pol = int(liczba/2)+1
    for i in range(2, pol):
        if liczba%i == 0:
            sumDzielnikow+=i
    return sumDzielnikow

print("Podaj liczbe")
liczba  = input()
liczba = int(liczba)

if czy_doskonala(liczba) == liczba:
    print("Liczba ta jest doskonała!")
else:
    print("Nie jest doskonała :<")
