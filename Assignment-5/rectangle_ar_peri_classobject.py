class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

    def perimeter(self):
        return 2 * (self.length + self.width)

# Creating an instance of the Rectangle class
rectangle = Rectangle(5.0, 3.0)

# Calculating and printing the area and perimeter
print(f"Area: {rectangle.area()}")
print(f"Perimeter: {rectangle.perimeter()}")


# --------------------------------------------------

#   Output:
#   Area: 15.0
#   Perimeter: 16.0

# --------------------------------------------------


# In order to take input, use this...
# class Rectangle:
#     def __init__(self, length, width):
#         self.length = length
#         self.width = width

#     def area(self):
#         return self.length * self.width

#     def perimeter(self):
#         return 2 * (self.length + self.width)

# Taking input from the user for length and width
# length = float(input("Enter the length of the rectangle: "))
# width = float(input("Enter the width of the rectangle: "))

# Creating an instance of the Rectangle class with user input
# rectangle = Rectangle(length, width)

# Calculating and printing the area and perimeter
# print(f"Area: {rectangle.area()}")           # Example Output: Area: 15.0
# print(f"Perimeter: {rectangle.perimeter()}")  # Example Output: Perimeter: 16.0