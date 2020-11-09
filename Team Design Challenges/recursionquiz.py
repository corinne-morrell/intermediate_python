def f(n):
    print("n=", n)
    if n < 2:
        c = 3
    else:
        a = f(n-3)
        b = f(n-2)
        c = a + b
    print("f(",n,") =", c)
    return c

x = f(6)
print( "RESULT:", x)