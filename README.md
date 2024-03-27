

---

# Library Management System

The Library Management System is a Python-based console application designed to manage a library's operations, including adding and listing books, managing users, and handling book checkouts and check-ins.

## Project Structure

The project consists of the following files and directories:

- `main.py`: This file contains the main entry point of the application. It instantiates the `LibraryManagementSystem` class and runs its `main` method to start the application.
- `book.py`: This module defines the `BookManager` class, which handles operations related to books, such as adding, listing, updating, and deleting books.
- `user.py`: This module defines the `UserManager` class, which handles operations related to users, such as adding, listing, updating, and deleting users.
- `check.py`: This module defines the `CheckoutManager` class, which handles book checkout and check-in operations.
- `models.py`: This module contains the definitions of the `Book`, `User`, and `Checkout` classes representing the data entities used in the application.
- `storage.py`: This module provides functionality for loading and saving data to JSON files.
- `logger.py`: This module contains the `Logger` class, which logs operations performed in the system to a text file.
- `documentation.docx`: Comprehensive documentation covering project structure, classes, methods, and usage instructions.

## Setup Instructions

To set up and run the Library Management System on your local machine, follow these steps:

1. **Clone the Repository**: Clone this repository to your local machine using the following command:

   ```
   git clone https://github.com/your-username/library-management-system.git
   ```

2. **Navigate to the Project Directory**: Change your current directory to the root of the project:

   ```
   cd library-management-system
   ```

3. **Run the Application**: Run the `main.py` file to start the Library Management System:

   ```
   python main.py
   ```

4. **Interact with the Application**: Once the application is running, follow the prompts on the console to perform various library management operations, such as adding books, managing users, and checking out books.

## New Features

- **Preventing Duplicate User IDs and Names**: Implemented functionality to ensure that there are no duplicate user IDs or names when adding a new user. If a duplicate is detected, the system notifies the user that the user already exists.
  
- **Book Availability Tracking**: Enhanced book management by implementing book availability tracking. Before allowing a checkout operation, the system checks the availability of the book to prevent multiple users from checking out the same book simultaneously.
  
- **User-Specific Check-in**: Implemented user-specific check-in functionality, allowing only the user who has checked out a book to check it back in. Other users cannot perform the check-in operation for books that they have not checked out.

## Documentation

Refer to the `documentation.docx` file for comprehensive documentation covering project structure, classes, methods, and usage instructions. It also highlights improvements made in the latest version, including better usage of exception handling (`try-except` blocks), clearer comments throughout the code, and ensuring file names and class names match for consistency and clarity.

---
