def ifactorial(n):
    if n == 0:
        return 1
    elif n<0:
        return 0
    i = 1
    res = 1
    while i <= n:
        res = res*i
        i = i + 1
    return res

def rfactorial(n):
    if n <= 0:
        return 1
    else:
        return n*rfactorial(n-1)

def factorial():
    n = input("Podaj liczbę naturalną: ")
    import ispeed
    print("ifactorial: ", ispeed.ispeed(ifactorial,n))
    print("rfactorial: ", ispeed.ispeed(rfactorial,n))
factorial()