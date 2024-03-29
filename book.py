# book.py

from storage import Storage
from logger import Logger


class Book:
    def __init__(self, title, author, isbn):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.checked_out = False  # Initialize as available by default

    @staticmethod
    def add_book(title, author, isbn):
        try:
            # Load existing books data from storage
            books = Storage.load_data("books.json")
            # Create a new Book object and append its dictionary representation to the list of books
            books.append(Book(title, author, isbn).__dict__)
            # Save the updated list of books back to storage
            Storage.save_data("books.json", books)
            # Log the operation
            Logger.log_operation(
                "Add Book", f"Title: {title}, Author: {author}, ISBN: {isbn}"
            )
        except Exception as e:
            print(f"An error occurred while adding a book: {e}")

    @staticmethod
    def update_book(isbn, new_title=None, new_author=None):
        try:
            # Load existing books data from storage
            books = Storage.load_data("books.json")
            # Update the details of the book with the given ISBN
            for book in books:
                if book["isbn"] == isbn:
                    if new_title:
                        book["title"] = new_title
                    if new_author:
                        book["author"] = new_author
                    break
            # Save the updated list of books back to storage
            Storage.save_data("books.json", books)
        except Exception as e:
            print(f"An error occurred while updating book details: {e}")

    @staticmethod
    def delete_book(isbn):
        try:
            # Load existing books data from storage
            books = Storage.load_data("books.json")
            # Remove the book with the given ISBN from the list of books
            books = [book for book in books if book["isbn"] != isbn]
            # Save the updated list of books back to storage
            Storage.save_data("books.json", books)
        except Exception as e:
            print(f"An error occurred while deleting a book: {e}")
    @staticmethod
    def list_books():
        try:
            # Load existing books data from storage
            books = Storage.load_data("books.json")
            # Print details of each book
            for book in books:
                print(book)
        except Exception as e:
            print(f"An error occurred while listing books: {e}")
    @staticmethod
    def search_book(attribute, value):
        try:
            # Load existing books data from storage
            books = Storage.load_data("books.json")
            # Search for books based on the given attribute and value
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
            # Load existing books data from storage
            books = Storage.load_data("books.json")
            # Check if the book with the given ISBN is available for checkout
            for book in books:
                if book["isbn"] == isbn:
                    return not book["checked_out"]
            return False
        except Exception as e:
            print(f"An error occurred while checking book availability: {e}")
            return False

    @staticmethod
    def update_book_status(isbn, checked_out):
        try:
            # Load existing books data from storage
            books = Storage.load_data("books.json")
            # Update the status of the book with the given ISBN
            for book in books:
                if book["isbn"] == isbn:
                    book["checked_out"] = checked_out
                    break
            # Save the updated list of books back to storage
            Storage.save_data("books.json", books)
        except Exception as e:
            print(f"An error occurred while updating book status: {e}")
