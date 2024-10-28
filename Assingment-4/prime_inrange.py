# def prime(a,b):
    # for i in range(a,b+1):
        # flag=0
        # for j in range(2,i):
            # if(i%j==0):
                # flag=1
                # break
        # if(flag==0):
            # print(i)
    # return i
# 
# start=int(input("Starting range="))
# end=int(input("Ending range="))
# primenos=prime(start,end)
# 
# print(f"These are the Prime numbers between {start} and {end}")

# This code accepts 1 as a Prime Number, therefore its wrong

def prime(a, b):
    for i in range(a, b + 1):
        if i == 1:
            continue  
        flag = 0
        for j in range(2, int(i ** 0.5) + 1):
            if i % j == 0:
                flag = 1
                break
        if flag == 0:
            print(i)

start = int(input("Starting range = "))
end = int(input("Ending range = "))

prime(start, end)

print(f"These are the prime numbers between {start} and {end}")
