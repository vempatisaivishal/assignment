import json


class Storage:
    @staticmethod
    def load_data(filename):
        """
        Load data from a JSON file.

        Args:
            filename (str): The name of the JSON file to load data from.

        Returns:
            list: The data loaded from the file, or an empty list if the file does not exist or is empty.
        """
        try:
            with open(filename, "r") as file:
                data = json.load(file)
        except (FileNotFoundError, json.JSONDecodeError):
            data = []  # If the file doesn't exist or is empty, return an empty list
        return data

    @staticmethod
    def save_data(filename, data):
        """
        Save data to a JSON file.

        Args:
            filename (str): The name of the JSON file to save data to.
            data (list): The data to be saved to the file.
        """
        with open(filename, "w") as file:
            json.dump(data, file)
