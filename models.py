class Book:
    def __init__(self, title, author, isbn):
        """
        Initialize a Book object with its attributes.

        Args:
            title (str): The title of the book.
            author (str): The author of the book.
            isbn (str): The ISBN (International Standard Book Number) of the book.
        """
        try:
            self.title = title
            self.author = author
            self.isbn = isbn
            self.checked_out = False  # Initialize as available by default
        except Exception as e:
            print(f"An error occurred while initializing Book: {e}")


class User:
    def __init__(self, name, user_id):
        """
        Initialize a User object with its attributes.

        Args:
            name (str): The name of the user.
            user_id (str): The unique ID of the user.
        """
        try:
            self.name = name
            self.user_id = user_id
        except Exception as e:
            print(f"An error occurred while initializing User: {e}")


class Check:
    def __init__(self, user_id, isbn):
        """
        Initialize a Checkout object with its attributes.

        Args:
            user_id (str): The ID of the user who is checking out the book.
            isbn (str): The ISBN of the book being checked out.
        """
        try:
            self.user_id = user_id
            self.isbn = isbn
        except Exception as e:
            print(f"An error occurred while initializing Check: {e}")
