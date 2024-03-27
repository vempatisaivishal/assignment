# user.py

from storage import Storage
from logger import Logger


class User:
    def __init__(self, name, user_id):
        self.name = name
        self.user_id = user_id

    @staticmethod
    def add_user(name, user_id):
        try:
            users = Storage.load_data("users.json")

            # Check for duplicate user_id
            if any(user["user_id"] == user_id for user in users):
                print("User with the same ID already exists.")
                return

            # Check for duplicate name
            if any(user["name"] == name for user in users):
                print("User with the same name already exists.")
                return

            users.append(User(name, user_id).__dict__)
            Storage.save_data("users.json", users)
            Logger.log_operation("Add User", f"Name: {name}, User ID: {user_id}")
            print("User added.")
        except Exception as e:
            print(f"An error occurred while adding a user: {e}")

    @staticmethod
    def list_users():
        try:
            users = Storage.load_data("users.json")
            for user in users:
                print(user)
        except Exception as e:
            print(f"An error occurred while listing users: {e}")

    @staticmethod
    def update_user(user_id, new_name=None):
        try:
            users = Storage.load_data("users.json")
            for user in users:
                if user["user_id"] == user_id:
                    if new_name:
                        user["name"] = new_name
                    break
            Storage.save_data("users.json", users)
            print("User updated.")
        except Exception as e:
            print(f"An error occurred while updating user details: {e}")

    @staticmethod
    def delete_user(user_id):
        try:
            users = Storage.load_data("users.json")
            users = [user for user in users if user["user_id"] != user_id]
            Storage.save_data("users.json", users)
            print("User deleted.")
        except Exception as e:
            print(f"An error occurred while deleting a user: {e}")

    @staticmethod
    def search_user(attribute, value):
        try:
            users = Storage.load_data("users.json")
            found_users = []
            for user in users:
                if user.get(attribute) == value:
                    found_users.append(user)
            return found_users
        except Exception as e:
            print(f"An error occurred while searching for users: {e}")
            return []
