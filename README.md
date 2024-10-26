# Kadeem Lewis Midterm

[*** Demo Video ***]()


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