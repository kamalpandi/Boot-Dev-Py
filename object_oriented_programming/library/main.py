class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author


class Library:
    def __init__(self, name):
        self.name = name
        self.books = []

    def add_book(self, book):
        self.books.append(book)

    def remove_book(self, book_to_remove):
        for book in self.books:
            if book.title == book_to_remove.title and book.author == book_to_remove.author:
                self.books.remove(book)
                return
        print("Book not found")

    def search_books(self, search_string):
        search_string = search_string.lower()
        searched_books = []
        for book in self.books:
            if search_string in book.title.lower() or search_string in book.author.lower():
                searched_books.append(book)
        return searched_books

                
                
