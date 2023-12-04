def wydaj(reszta):
    kwoty = [500, 200, 100, 50, 20, 10, 5, 2, 1]
    while reszta:
        for i in kwoty:
            if reszta-i >= 0:
                print(i)
                reszta-=i

print("Podaj reszte:")
n = input()

print("Wydane banknoty: ")
wydaj(int(n))



