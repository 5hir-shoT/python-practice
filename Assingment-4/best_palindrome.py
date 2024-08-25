def is_palindrome(s):
    return s == s[::-1]

s = input("Enter a string: ")
if is_palindrome(s):
    print(f'"{s}" is a palindrome.')
else:
    print(f'"{s}" is not a palindrome.')



#   Output:
#   Enter a string: malayalam
#   "malayalam" is a palindrome.

#   Enter a string: cat
#   "cat" is not a palindrome.