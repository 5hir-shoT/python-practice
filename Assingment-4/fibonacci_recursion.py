def fibonacci(n):
    if n <= 0:
        return []
    elif n == 1:
        return [0]
    elif n == 2:
        return [0, 1]
    else:
        sequence = fibonacci(n - 1)
        sequence.append(sequence[-1] + sequence[-2])
        return sequence

n = int(input("Enter the number of Fibonacci sequence elements: "))
result = fibonacci(n)
print(f"The first {n} numbers in the Fibonacci sequence are:", result)



#   Output:
#   Enter the number of Fibonacci sequence elements: 5
#   The first 5 numbers in the Fibonacci sequence are: [0, 1, 1, 2, 3]