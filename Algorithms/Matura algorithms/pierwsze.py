def pierwsze(liczba):
    liczba = int(liczba)
    if liczba == 2:
        return True
    if liczba%2 == 0 or liczba <2:
        return False

    do = int(liczba/2)+1
    for i in range(3,do, 2):
        if liczba%i == 0:
            return False
    return True

if pierwsze(5):
    print("Liczba pierwsza")
else:
    print("Nie jest to liczba pierwsza")