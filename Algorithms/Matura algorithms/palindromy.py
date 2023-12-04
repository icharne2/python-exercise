def czy_palindrom(slowo):
    slowo = slowo.lower()
    do = int(len(slowo)/2)
    for i in range(0, do):
        if slowo[i] != slowo[i]:
            return False
    return True

if czy_palindrom('Ala'):
    print("Jest to palindrom")
else:
    print("Nie jest to palindrom :<")