class Book:
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year

    def get_summary(self):
        return f"Title: {self.title}, Author: {self.author}, Year: {self.year}"

    def is_classic(self):
        current_year = 2024
        return (current_year - self.year) > 50

# Creating an instance of the Book class
book = Book("1984", "George Orwell", 1949)

# Printing the book summary
print(book.get_summary())

# Checking if the book is a classic
if book.is_classic():
    print("The book is a classic.")
else:
    print("The book is not a classic.")




#   Output:
#   Title: 1984, Author: George Orwell, Year: 1949
#   The book is a classic.