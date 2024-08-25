def second_largest(lst):
    lst = list(set(lst))  # Remove duplicates
    lst.sort()  # Sort the list
    return lst[-2] if len(lst) >= 2 else None

lst = [int(x) for x in input("Enter numbers separated by spaces: ").split()]
result = second_largest(lst)
if result is not None:
    print("The second largest number is:", result)
else:
    print("The list doesn't have a second largest number.")
    
    

#   Output:
#   Enter numbers separated by spaces: 34 56 12 234 
#   The second largest number is: 56