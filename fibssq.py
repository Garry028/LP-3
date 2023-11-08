def fibonacci(num):
    if num == 0:
        return 0
    elif num == 1 or num == 2:
        return 1
    else:
        return fibonacci(num - 1) + fibonacci(num - 2)


n = 5
fib_series = []

for i in range(n):
    fib_series.append(fibonacci(i))

# Calculate the sum of squares of Fibonacci numbers up to the nth term
sum_of_squares = sum(x**2 for x in fib_series)

# Calculate the product of the nth and (n+1)th Fibonacci numbers
product = fibonacci(n) * fibonacci(n + 1)
print("Sum of squares:", sum_of_squares)
print("Product of Fibonacci numbers:", product)

# Verify the equality
if sum_of_squares == product:
    print("The equation holds for n =", n)
else:
    print("The equation does not hold for n =", n)
