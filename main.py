from book import Book  # Import the BookManager class for managing books
from user import User  # Import the UserManager class for managing users
from check import (
    Check,
)  # Import the CheckoutManager class for managing checkouts


class Main:
    def __init__(self):
        """
        Initialize the LibraryManagementSystem with instances of BookManager, UserManager, and CheckoutManager.
        """
        self.book_manager = Book  # Create an instance of BookManager
        self.user_manager = User  # Create an instance of UserManager
        self.checkout_manager = Check  # Create an instance of CheckoutManager

    def main_menu(self):
        """
        Display the main menu options for the LibraryManagementSystem.

        Returns:
            str: The user's selected choice.
        """
        print("\nLibrary Management System")
        print("1. Add Book")
        print("2. List Books")
        print("3. Update Book")
        print("4. Delete Book")
        print("5. Search Book")
        print("6. Add User")
        print("7. List Users")
        print("8. Update User")
        print("9. Delete User")
        print("10. Search User")
        print("11. Checkout Book")
        print("12. Checkin Book")
        print("13. Exit")
        choice = input("Enter choice: ")
        return choice

    def main(self):
        """
        Main function to run the LibraryManagementSystem.
        """
        while True:
            choice = self.main_menu()  # Get the user's choice from the main menu
            if choice == "1":
                title = input("Enter title: ")
                author = input("Enter author: ")
                isbn = input("Enter ISBN: ")
                self.book_manager.add_book(title, author, isbn)
                print("Book added.")
            elif choice == "2":
                self.book_manager.list_books()
            elif choice == "3":
                isbn = input("Enter ISBN of the book to update: ")
                new_title = input("Enter new title (leave blank to skip): ")
                new_author = input("Enter new author (leave blank to skip): ")
                self.book_manager.update_book(isbn, new_title, new_author)
                print("Book updated.")
            elif choice == "4":
                isbn = input("Enter ISBN of the book to delete: ")
                self.book_manager.delete_book(isbn)
                print("Book deleted.")
            elif choice == "5":
                attribute = input(
                    "Enter attribute to search by (title, author, or ISBN): "
                )
                value = input(f"Enter {attribute}: ")
                found_books = self.book_manager.search_book(attribute, value)
                if found_books:
                    print("Found books:")
                    for book in found_books:
                        print(book)
                else:
                    print("No books found.")
            elif choice == "6":
                name = input("Enter user name: ")
                user_id = input("Enter user ID: ")
                self.user_manager.add_user(name, user_id)
                print("User added.")
            elif choice == "7":
                self.user_manager.list_users()
            elif choice == "8":
                user_id = input("Enter user ID of the user to update: ")
                new_name = input("Enter new name (leave blank to skip): ")
                self.user_manager.update_user(user_id, new_name)
                print("User updated.")
            elif choice == "9":
                user_id = input("Enter user ID of the user to delete: ")
                self.user_manager.delete_user(user_id)
                print("User deleted.")
            elif choice == "10":
                attribute = input("Enter attribute to search by (name or user ID): ")
                value = input(f"Enter {attribute}: ")
                found_users = self.user_manager.search_user(attribute, value)
                if found_users:
                    print("Found users:")
                    for user in found_users:
                        print(user)
                else:
                    print("No users found.")
            elif choice == "11":  # Checkout Book
                user_id = input("Enter user ID: ")
                isbn = input("Enter ISBN of the book to checkout: ")
                if self.book_manager.check_availability(isbn):
                    self.checkout_manager.checkout_book(user_id, isbn)
                    print("Book checked out.")
                else:
                    print("Book is not available for checkout.")
            elif choice == "12":  # Checkin Book
                user_id = input("Enter user ID: ")
                isbn = input("Enter ISBN of the book to check in: ")
                self.checkout_manager.checkin_book(user_id, isbn)
                print("Book checked in.")
            elif choice == "13":
                print("Exiting.")
                break
            else:
                print("Invalid choice, please try again.")


if __name__ == "__main__":
    library_system = Main()  # Create an instance of LibraryManagementSystem
    library_system.main()  # Run the main function of the LibraryManagementSystem
