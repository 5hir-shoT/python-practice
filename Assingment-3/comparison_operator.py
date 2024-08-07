a=float(input("a="))
b=float(input("b="))

equal= a==b
not_equal= a!=b
greater= a>b
lesser= a<b
greater_equal= a>=b
lesser_equal= a<=b

print(f"a==b is {equal}")
print(f"a!=b is {not_equal}")
print(f"a>b is {greater}")
print(f"a<b is {lesser}")
print(f"a>=b is {greater_equal}")
print(f"a<=b is {lesser_equal}")

#output
#a=10
#b=20
#a==b is False
#a!=b is True
#a>b is False
#a<b is True
#a>=b is False
#a<=b is True