#Write a program that prints numbers from 1 to 10
#but skips the number 5 
#and stops if the number is greater than 8.

def print_numbers():
    for number in range(1, 11):
        if number == 5:
            continue
        if number > 8:
            break
        print(number)
print_numbers()

#1
#2
#3
#4
#6
#7
#8