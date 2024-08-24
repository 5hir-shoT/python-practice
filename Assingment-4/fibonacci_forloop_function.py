def fibonacci(n):
    fib_sequence = []
    a, b = 0, 1
    for _ in range(n):
        fib_sequence.append(a)
        a, b = b, a + b
    return fib_sequence

n = int(input("Enter the number of Fibonacci sequence elements: "))
result = fibonacci(n)
print(f"The first {n} numbers in the Fibonacci sequence are:", result)


#   Output:
#   Enter the number of Fibonacci sequence elements: 5
#   The first 5 numbers in the Fibonacci sequence are: [0, 1, 1, 2, 3]