# check.py

from storage import Storage
from logger import Logger
from book import Book


class Check:
    @staticmethod
    def checkout_book(user_id, isbn):
        try:
            # Load existing checkout data from storage
            checkouts = Storage.load_data("checkouts.json")
            # Check if the book is available
            if Book.check_availability(isbn):
                # Append the new checkout record to the list of checkouts
                checkouts.append({"user_id": user_id, "isbn": isbn})
                # Save the updated list of checkouts back to storage
                Storage.save_data("checkouts.json", checkouts)
                # Update the book status to checked out
                Book.update_book_status(isbn, checked_out=True)
                # Log the checkout operation
                Logger.log_operation(
                    "Checkout Book", f"User ID: {user_id}, ISBN: {isbn}"
                )
                print("Book checked out.")
            else:
                print("Book is not available for checkout.")
        except Exception as e:
            print(f"An error occurred while checking out a book: {e}")

    @staticmethod
    def checkin_book(user_id, isbn):
        try:
            # Try to load existing checkout data from storage
            checkouts = Storage.load_data("checkouts.json")
            # Find the checkout record corresponding to the specified user ID and ISBN
            checkout_record = next(
                (
                    checkout
                    for checkout in checkouts
                    if checkout.get("user_id") == user_id
                    and checkout.get("isbn") == isbn
                ),
                None,
            )
            if checkout_record:
                # Remove the checkout record
                checkouts.remove(checkout_record)
                # Save the updated list of checkouts back to storage
                Storage.save_data("checkouts.json", checkouts)
                # Update the book status to checked in
                Book.update_book_status(isbn, checked_out=False)
                # Log the checkin operation
                Logger.log_operation(
                    "Checkin Book", f"User ID: {user_id}, ISBN: {isbn}"
                )
                print("Book checked in.")
            else:
                print(
                    "This user cannot check in this book as they did not check it out."
                )
        except Exception as e:
            print(f"An error occurred while checking in a book: {e}")
