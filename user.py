from models import User  # Import the User class
from storage import Storage  # Import the Storage class for data handling
from logger import Logger  # Import the Logger class for logging operations


class UserManager:
    @staticmethod
    def add_user(name, user_id):
        """
        Add a new user to the system.

        Args:
            name (str): The name of the user.
            user_id (str): The unique identifier for the user.
        """
        users = Storage.load_data("users.json")  # Load existing user data
        users.append(
            User(name, user_id).__dict__
        )  # Create a new user instance and add to the list
        Storage.save_data("users.json", users)  # Save the updated user data to file
        Logger.log_operation(
            "Add User", f"Name: {name}, User ID: {user_id}"
        )  # Log the operation

    @staticmethod
    def list_users():
        """
        List all users in the system.
        """
        users = Storage.load_data("users.json")  # Load user data
        for user in users:
            print(user)  # Print each user's details

    @staticmethod
    def update_user(user_id, new_name=None):
        """
        Update the details of an existing user.

        Args:
            user_id (str): The unique identifier of the user to update.
            new_name (str, optional): The new name for the user (if provided).
        """
        users = Storage.load_data("users.json")  # Load existing user data
        for user in users:
            if user["user_id"] == user_id:  # Find the user to update
                if new_name:  # Update the name if provided
                    user["name"] = new_name
                break  # Stop searching once the user is found and updated
        Storage.save_data("users.json", users)  # Save the updated user data to file

    @staticmethod
    def delete_user(user_id):
        """
        Delete a user from the system.

        Args:
            user_id (str): The unique identifier of the user to delete.
        """
        users = Storage.load_data("users.json")  # Load existing user data
        users = [
            user for user in users if user["user_id"] != user_id
        ]  # Remove the user with matching ID
        Storage.save_data("users.json", users)  # Save the updated user data to file

    @staticmethod
    def search_user(attribute, value):
        """
        Search for users based on a specified attribute and value.

        Args:
            attribute (str): The attribute to search by (e.g., "name" or "user_id").
            value (str): The value to search for within the specified attribute.

        Returns:
            list: A list of users matching the search criteria.
        """
        users = Storage.load_data("users.json")  # Load user data
        found_users = []  # Initialize an empty list to store found users
        for user in users:
            if (
                user.get(attribute) == value
            ):  # Check if the user matches the search criteria
                found_users.append(user)  # Add the user to the list of found users
        return found_users  # Return the list of found users
