#rekurencyjnie
def fib2(n):
    if n == 1 or n == 2:
        return 1
    else:
        return fib2(n-1)+fib2(n-2)

print(fib2(5))

#iteracyjnie
def fib(n):
    n = int(n)
    poprzedi = 0
    nastepny = 1
    for i in range(1, n+1):
        print(nastepny, end=" ")
        nastepny += poprzedi
        poprzedi = nastepny - poprzedi

fib(3)
