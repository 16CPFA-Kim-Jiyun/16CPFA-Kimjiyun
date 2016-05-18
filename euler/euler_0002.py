def fibo(n):
    if 2 == n:
        return 2
    else:
        return n + fibo(n + n)

print(fibo(3))



