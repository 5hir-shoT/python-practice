def sum_list(lst):
    return sum(lst)

# Taking input from the user
input_list = [int(x) for x in input("Enter a list of numbers separated by spaces: ").split()]

# Calculating the sum
result = sum_list(input_list)

# Printing the output
print("The sum of the numbers is:", result)




# Output:
#Enter a list of numbers separated by spaces: 2 5 9 7
#The sum of the numbers is: 23