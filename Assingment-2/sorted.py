books = [
    {"title": "Feluda", "author": "Satyajit Ray", "year": 1970},
    {"title": "48 Laws of Power", "author": "Robert Greene", "year": 2011},
    {"title": "The Road", "author": "Cormac McCarthy", "year": 2006},
    {"title": "Harry Potter and the Sorcerer's Stone", "author": "J.K. Rowling", "year": 1997},
    {"title": "The Da Vinci Code", "author": "Dan Brown", "year": 2003}
]

sorted_books = sorted(books, key=lambda x: x["year"])

print("Sorted list of books by year:")
for book in sorted_books:
    print(book)

titles_after_2000 = [book["title"] for book in books if book["year"] > 2000]

print("\nBook titles published after the year 2000:")
print(titles_after_2000)