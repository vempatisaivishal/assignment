class Book:
    def __init__(self, title, author, isbn):
        """
        Initialize a Book object with its attributes.

        Args:
            title (str): The title of the book.
            author (str): The author of the book.
            isbn (str): The ISBN (International Standard Book Number) of the book.
        """
        self.title = title
        self.author = author
        self.isbn = isbn
        self.checked_out = False  # Initialize as available by default


class User:
    def __init__(self, name, user_id):
        """
        Initialize a User object with its attributes.

        Args:
            name (str): The name of the user.
            user_id (str): The unique ID of the user.
        """
        self.name = name
        self.user_id = user_id


class Checkout:
    def __init__(self, user_id, isbn):
        """
        Initialize a Checkout object with its attributes.

        Args:
            user_id (str): The ID of the user who is checking out the book.
            isbn (str): The ISBN of the book being checked out.
        """
        self.user_id = user_id
        self.isbn = isbn
