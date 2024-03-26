class Logger:
    @staticmethod
    def log_operation(operation, details):
        """
        Log an operation with its details to a text file.

        Args:
            operation (str): The name of the operation being logged.
            details (str): Additional details or parameters related to the operation.
        """
        try:
            # Open the log file in 'append' mode and write the operation and details to it
            with open("log.txt", "a") as file:
                file.write(f"{operation}: {details}\n")
        except Exception as e:
            print(f"An error occurred while logging operation: {e}")
