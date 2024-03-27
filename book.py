# book.py

from storage import Storage
from logger import Logger


class Book:
    def __init__(self, title, author, isbn):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.checked_out = False

    @staticmethod
    def add_book(title, author, isbn):
        try:
            books = Storage.load_data("books.json")
            books.append(
                {"title": title, "author": author, "isbn": isbn, "checked_out": False}
            )
            Storage.save_data("books.json", books)
            Logger.log_operation(
                "Add Book", f"Title: {title}, Author: {author}, ISBN: {isbn}"
            )
        except Exception as e:
            print(f"An error occurred while adding a book: {e}")

    @staticmethod
    def list_books():
        try:
            books = Storage.load_data("books.json")
            for book in books:
                print(book)
        except Exception as e:
            print(f"An error occurred while listing books: {e}")

    @staticmethod
    def update_book(isbn, new_title=None, new_author=None):
        try:
            books = Storage.load_data("books.json")
            for book in books:
                if book["isbn"] == isbn:
                    if new_title:
                        book["title"] = new_title
                    if new_author:
                        book["author"] = new_author
                    break
            Storage.save_data("books.json", books)
        except Exception as e:
            print(f"An error occurred while updating book details: {e}")

    @staticmethod
    def delete_book(isbn):
        try:
            books = Storage.load_data("books.json")
            books = [book for book in books if book["isbn"] != isbn]
            Storage.save_data("books.json", books)
        except Exception as e:
            print(f"An error occurred while deleting a book: {e}")

    @staticmethod
    def search_book(attribute, value):
        try:
            books = Storage.load_data("books.json")
            found_books = []
            for book in books:
                if book.get(attribute) == value:
                    found_books.append(book)
            return found_books
        except Exception as e:
            print(f"An error occurred while searching for books: {e}")
            return []

    @staticmethod
    def check_availability(isbn):
        try:
            books = Storage.load_data("books.json")
            for book in books:
                if book["isbn"] == isbn:
                    return not book["checked_out"]
            return False
        except Exception as e:
            print(f"An error occurred while checking book availability: {e}")
            return False

    @staticmethod
    def update_book_status(isbn, status):
        try:
            books = Storage.load_data("books.json")
            for book in books:
                if book["isbn"] == isbn:
                    book["checked_out"] = status  # Update the book status
                    break
            Storage.save_data("books.json", books)
        except Exception as e:
            print(f"An error occurred while updating book status: {e}")
