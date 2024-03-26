from models import Checkout
from storage import Storage
from logger import Logger
import json


class CheckoutManager:
    @staticmethod
    def checkout_book(user_id, isbn):
        # Load existing checkout data from storage
        checkouts = Storage.load_data("checkouts.json")

        # Append the new checkout record to the list of checkouts
        checkouts.append(Checkout(user_id, isbn).__dict__)

        # Save the updated list of checkouts back to storage
        Storage.save_data("checkouts.json", checkouts)

        # Log the checkout operation
        Logger.log_operation("Checkout Book", f"User ID: {user_id}, ISBN: {isbn}")

    @staticmethod
    def checkin_book(user_id, isbn):
        try:
            # Try to load existing checkout data from storage
            checkouts = Storage.load_data("checkouts.json")
        except FileNotFoundError:
            # If the checkout data file does not exist, initialize an empty list
            checkouts = []

        # Filter out the checkout record corresponding to the specified user ID and ISBN
        checkouts = [
            checkout
            for checkout in checkouts
            if checkout["user_id"] != user_id or checkout["isbn"] != isbn
        ]

        # Save the updated list of checkouts back to storage
        Storage.save_data("checkouts.json", checkouts)

        # Log the checkin operation
        Logger.log_operation("Checkin Book", f"User ID: {user_id}, ISBN: {isbn}")
