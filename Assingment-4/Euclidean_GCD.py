def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))

result = gcd(num1, num2)

print(f"GCD of {num1} and {num2} is {result}")

#   Output:
#   Enter the first number: 4
#   Enter the second number: 28
#   GCD of 4 and 28 is 4