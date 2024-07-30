# Get the number of terms from the user
n = int(input("Enter the number of terms: "))

# First two terms of the Fibonacci series
a, b = 0, 1

# Check if the number of terms is valid
if n <= 0:
    print("Please enter a positive integer")
elif n == 1:
    print("Fibonacci sequence up to", n, "term is:")
    print(a)
else:
    print("Fibonacci sequence:")
    count = 0
    while count < n:
        print(a)
        # Update values
        a, b = b, a + b
        count += 1