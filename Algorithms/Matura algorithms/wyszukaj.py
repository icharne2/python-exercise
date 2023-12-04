def znajdz1(text, wzor):
    ile = 0
    dl1 = len(text)
    dl2 = len(wzor)

    for i in range(dl1-dl2+1):
        for x in range(dl2):
            if text[i+x] != wzor[x]:
                break
        else:
            print("Znaleziono wzór: ", wzor, "na pozycji ", i)
            ile+=1

    if ile != 0:
        print("Wzorzec ten wystąpił:", ile, "razy")
    else:
        print("Nie ma go w tekście")

znajdz1("matematyka", "mat")


def znajdz2(text, wzor):
    ile = 0
    dl1 = len(text)
    dl2 = len(wzor)

    for i in range(dl1 - dl2 + 1):
        if text[i:i+dl2] == wzor:
            print("Znaleziono wzór: ", wzor, "na pozycji ", i)
            ile += 1

    if ile != 0:
        print("Wzorzec ten wystąpił:", ile, "razy")
    else:
        print("Nie ma go w tekście")


znajdz2("matematyka", "mat")