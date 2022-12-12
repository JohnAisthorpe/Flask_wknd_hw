from models.book import *

book1 = Book("Harry Potter", "J.K.Rowling", "Fiction")
book2 = Book( "To Kill a Mockingbird", "Harper Lee", "Fiction")
book3 = Book("Steve Jobs", "Walter Isaacson", "Biography")

books = [book1, book2, book3]


def add_new_book(book):
    books.append(book)

def remove_book_at_index(index):
    books.pop(index)
