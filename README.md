# Kadeem Lewis Midterm

## Demo Video: [here]()


## Instructions

1. Clone Project using ```git clone```

2. cd into the project directory ```cd repl_calculator```

3. Ensure that the .env file exists and that HISTORY_PATH is set

4. Run main.py:
```bash
python main.py
```
5. To test the code run pytest

```bash

pytest # to tests code to see results of test

pytest --cov # to additionally see code coverage
```

## Documentation

### Design Principles

*** Singleton: ***:

The History class demonstrates the singleton pattern by providing a single, globally accessible instance of the calculation history. Instead of creating multiple instances of History, this class holds its state in class-level variables (_history and file_path), accessible via class methods. This structure ensures that any part of the application interacting with History will see the same _history list and file_path, preserving a single, shared history of calculations. The singleton pattern is effectively implemented here by:

- Using class-level attributes, meaning History doesn’t need instantiation.
- Providing class methods to access and modify the _history and file_path, maintaining a single shared state across the application.

*** Factory Method ***:

The History class uses a factory method pattern in its initialize_history class method to set up the _history list by reading from a CSV file. This factory method approach allows initialize_history to control how the _history data is created and populated, abstracting away the specifics of data retrieval. Rather than requiring the calling code to manage the data source directly, initialize_history handles initialization by using the FileManager.read_from_csv() function to fetch data, transforming it into Calculation instances as needed.


*** Facade ***:

Methods like initialize_history and save_history serve as a facade by abstracting away the details of reading from and writing to CSV files. These methods interact with FileManager to manage file operations, but users of History don’t need to know how these interactions are implemented. Instead, they only call the high-level methods, which handle setup and saving seamlessly. This facade design pattern approach improves code readability and maintainability by providing a clean, straightforward interface for managing calculation history.


*** Strategy ***:


### Environment Variables

Environments variables were used to store the file path were the history data would be stored so that it could easily be changed throughout the app whenever needed


### Logging

Logging was used in various places throughout the app. 
- Any errors that might arise in the program were logged
- All results that were printed for the user were also logged
- After major operations such as reading the file were completed, a log entry was added

### Look Before You Leak / Easier to Ask for Forgiveness than Permission

- The FileManager's read_from_csv() method demonstrates the use of the "easier to ask for forgiveness than permission" (EAFP) approach by proceeding with file reading and data parsing without pre-checks. If the file is missing, a FileNotFoundError is caught and handled by returning an empty list. Similarly, errors in row parsing are caught and logged, ensuring the process continues smoothly without additional conditional checks.

-  The History class get_history_path() method checks if cls.file_path is set before proceeding to return the path, ensuring that an error is logged if the path is not defined. This way, the function verifies the necessary conditions upfront, preventing errors by confirming prerequisites are met before any further action is taken.