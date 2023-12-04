def funkcja(x):
    #f(x) =  x^3 - 3x^2 + 2x - 6
    return x * (x * (x - 3) + 2) - 6

def zero(a,b, elipson):
    if funkcja(a) == 0.0:
        return a
    if funkcja(b) == 0.0:
        return b

    while( b-a > elipson):
        x = (a + b) / 2
        if x == 0.0:
            return x
        if funkcja(a)*funkcja(x) < 0:
            b = x
        else:
            a = x
    return (a + b) / 2

print(zero(-10, 10, 0.00001))

