class Book:
    def __init__(self, title, author, isbn, available_copies):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.available_copies = available_copies

    def __str__(self):
        return f"{self.title} by {self.author} (ISBN: {self.isbn}) - {self.available_copies} copies"
class Library:
    def __init__(self):
        self.collection = {}

    def add_book(self, book):
        self.collection[book.isbn] = book
        print(f"Added: {book}")

    def remove_book(self, isbn):
        print(f"Removed: {self.collection.pop(isbn, 'Not found')}")

    def borrow_book(self, isbn):
        book = self.collection.get(isbn)
        if book and book.available_copies > 0:
            book.available_copies -= 1
            print(f"Borrowed: {book}")
        else:
            print("Unavailable or not found.")

    def return_book(self, isbn):
        book = self.collection.get(isbn)
        if book:
            book.available_copies += 1
            print(f"Returned: {book}")
        else:
            print("Book not found.")

    def search_by_title(self, title):
        results = [book for book in self.collection.values() if title.lower() in book.title.lower()]
        print("Search Results:", *results if results else ["No matches found"], sep="\n")

    def list_books(self):
        print("Library Collection:", *self.collection.values() if self.collection else ["Empty"], sep="\n")

library = Library()
library.add_book(Book("The Great Gatsby", "F. Scott Fitzgerald", "123", 5))
library.add_book(Book("1984", "George Orwell", "124", 2))
library.list_books()
library.borrow_book("123")
library.return_book("123")
library.search_by_title("1984")
library.remove_book("124")
library.list_books()

# output
# Added: The Great Gatsby by F. Scott Fitzgerald (ISBN: 123) - 5 copies
# Added: 1984 by George Orwell (ISBN: 124) - 2 copies
# Library Collection:
# The Great Gatsby by F. Scott Fitzgerald (ISBN: 123) - 5 copies
# 1984 by George Orwell (ISBN: 124) - 2 copies
# Borrowed: The Great Gatsby by F. Scott Fitzgerald (ISBN: 123) - 4 copies
# Returned: The Great Gatsby by F. Scott Fitzgerald (ISBN: 123) - 5 copies
# Search Results:
# 1984 by George Orwell (ISBN: 124) - 2 copies
# Removed: 1984 by George Orwell (ISBN: 124) - 2 copies
# Library Collection:
# The Great Gatsby by F. Scott Fitzgerald (ISBN: 123) - 5 copies