'''
def fibonacci(n):
    fibonacci = [1, 1]
    for i in range(2, n+1):
        f_n = fibonacci[n-2] + fibonacci[n-1]
        fibonacci.append(f_n)


test = fibonacci(5)
print(test)'''

def fibonacci_2(n):
    fib_n = [1, 1, 2]
    if n > 2:
        fib_n.append(fibonacci_2(n-1) + fibonacci_2(n-2))

    print(fib_n)

fibonacci_2(5)