def gcd(a,b):
    if b>a:
        mn=a
    else:
        mn=b
    for i in range(1,mn+1):
        if a%i==0  and  b%i==0:
            hcf=i
    return hcf

num1=int(input("Number 1="))
num2=int(input("Number 2="))

hcf=gcd(num1,num2)
print(f"GCD of {num1} and {num2} is: {hcf}")


#   PSEUDOCODE
#   Step 1: Find minimum, store it to a variable
#   Step2: for i in range(1, mn+1):
#               if num1%i==0  and  num2%i==0:
#                   hcf=i
#          return hcf


#   Number 1=4
#   Number 2=28
#   GCD of 4 and 28 is: 4