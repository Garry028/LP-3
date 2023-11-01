def fib_iterative(n):
    first = 0
    second = 1
    for i in range(1, n + 1):
        print(first, end=" ")
        next = first + second
        first = second
        second = next


fib_iterative(10)


def fibonacci(num):
    if num < 2:
        return 1
    else:
        return fibonacci(num - 1) + fibonacci(num - 2)


n = 10
fib_series = []

for i in range(n):
    fib_series.append(fibonacci(i))

print(fib_series)
