def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

n = int(input("Enter an integer: "))
if is_prime(n):
    print(f"{n} is a prime number.")
else:
    print(f"{n} is not a prime number.")



#   Output:
#   Enter an integer: 4
#   4 is not a prime number.

#   Enter an integer: 2
#   2 is a prime number.