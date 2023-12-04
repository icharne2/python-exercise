def czy_anagram(slowo1, slowo2):
    lista1 = list(slowo1.lower())
    lista1.sort()
    lista2 = list(slowo2.lower())
    lista2.sort()
    if lista1 != lista2:
        return False
    return True

print("Podaj dwa slowa")
slowo1 = input()
slowo2 = input()

if czy_anagram(slowo1, slowo2):
    print("Są to anagramy")
else:
    print("Nie są to anagramy :<")
