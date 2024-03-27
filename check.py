# check.py

from storage import Storage
from logger import Logger
from book import Book


class Check:
    @staticmethod
    def checkout_book(user_id, isbn):
        try:
            checkouts = Storage.load_data("checkouts.json")
            checkouts.append({"user_id": user_id, "isbn": isbn})
            Storage.save_data("checkouts.json", checkouts)
            Logger.log_operation("Checkout Book", f"User ID: {user_id}, ISBN: {isbn}")
            print("Book checked out.")
        except Exception as e:
            print(f"An error occurred while checking out a book: {e}")

    @staticmethod
    def checkin_book(user_id, isbn):
        try:
            checkouts = Storage.load_data("checkouts.json")
            # Find the checkout record for the given user_id and isbn
            checkout_record = next(
                (
                    checkout
                    for checkout in checkouts
                    if checkout["user_id"] == user_id and checkout["isbn"] == isbn
                ),
                None,
            )
            if checkout_record:
                # Remove the checkout record from the list
                checkouts.remove(checkout_record)
                Storage.save_data("checkouts.json", checkouts)
                Logger.log_operation(
                    "Checkin Book", f"User ID: {user_id}, ISBN: {isbn}"
                )
                print("Book checked in.")
            else:
                print("You cannot check in this book as you haven't checked it out.")
        except Exception as e:
            print(f"An error occurred while checking in a book: {e}")
