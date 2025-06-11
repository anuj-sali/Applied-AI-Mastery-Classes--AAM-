# create folders inside 1.Core Python Mastery folder:
# with names as follows:
# 1. Variables & Data Types.
# 2. Strings in Python.
# 3. Booleans & Operators.
# 4. Control Flow
# 5. Loops in Python.
# 6. Python Data Structures.
# 7. Functions.
# 8. Modules & Packages.
# import os
# def create_folders(base_path):
#     folders = [
#         "1. Variables & Data Types",
#         "2. Strings in Python",
#         "3. Booleans & Operators",
#         "4. Control Flow",
#         "5. Loops in Python",
#         "6. Python Data Structures",
#         "7. Functions",
#         "8. Modules & Packages"
#     ]
    
#     for folder in folders:
#         os.makedirs(os.path.join(base_path, folder), exist_ok=True)
<<<<<<< HEAD
# Usage:
=======
# # Usage:
>>>>>>> 224a89c570a26cc8c6ad9b67b6f2e0f3c6615718
# base_path = "1.Core Python Mastery"
# create_folders(base_path)

# Inside each of these folders (1.Variables & Data Types, 2. Strings in Python etc) folders, create the following folders:
# 1.1 Course Files
# 1.2 Exercise Files

# similarly for other folders:
# 2.1 Course Files
# 2.2 Exercise Files

<<<<<<< HEAD
print("Folders created successfully.")
=======
# 9. OOP in Python (May 26, 2025 - Monday)
# 9.1. Classes & Objects
# 9.2. Special Methods: __init__, __str__, __eq__, etc.
# 9.3. Instance, Class, Static Methods
# 9.4. Inheritance, super(), MRO
# 9.5. Multiple Inheritance
# 9.6. Encapsulation, Name Mangling
# 9.7. Abstraction with ABC
# 9.8. Duck Typing

# 10. File Handling (May 28, 2025 - Wednesday)
# 10.1. Open, Read, Write, Append
# 10.2. File Modes & Pointers
# 10.3. File Context Manager
# 10.4. CSV: csv.reader, DictWriter
# 10.5. JSON: json.load, json.dumps
# 10.6. Pickle: Usage & Security

# 11. Exception Handling & Debugging (May 30, 2025 - Friday)
# 11.1. try-except, else, finally
# 11.2. Custom Exceptions
# 11.3. raise, assert
# 11.4. Debugging: pdb, breakpoint(), traceback
# 11.5. Logging

# 12. Iterators & Generators (June 2, 2025 - Monday)
# 12.1. Iterator Protocol
# 12.2. Creating Custom Iterators
# 12.3. Generator Functions, yield
# 12.4. Generator Expressions

# 13. Functional Programming (June 4, 2025 - Wednesday)
# 13.1. map(), filter(), reduce()
# 13.2. zip(), sorted()
# 13.3. any(), all()

#using python make 9 to 13 folders like 9. OOP in Python, 10. File Handling, 11. Exception Handling & Debugging, 12. Iterators & Generators, 13. Functional Programming
import os

def create_subfolders(base_path):
    main_folders = [
        "9. OOP in Python",
        "10. File Handling",
        "11. Exception Handling & Debugging",
        "12. Iterators & Generators",
        "13. Functional Programming"
    ]
    
    for folder in main_folders:
        folder_path = os.path.join(base_path, folder)
        
        # Create subfolders in each main folder
        course_files = os.path.join(folder_path, "9.1 Course Files" if folder.startswith("9") else 
                                              "10.1 Course Files" if folder.startswith("10") else
                                              "11.1 Course Files" if folder.startswith("11") else
                                              "12.1 Course Files" if folder.startswith("12") else
                                              "13.1 Course Files")
        
        exercise_files = os.path.join(folder_path, "9.2 Exercise Files" if folder.startswith("9") else
                                                "10.2 Exercise Files" if folder.startswith("10") else
                                                "11.2 Exercise Files" if folder.startswith("11") else
                                                "12.2 Exercise Files" if folder.startswith("12") else
                                                "13.2 Exercise Files")
        
        os.makedirs(course_files, exist_ok=True)
        os.makedirs(exercise_files, exist_ok=True)

# Usage:
base_path = "1. Core Python Mastery"
create_subfolders(base_path)

# under each of these folders make 9.1 Course Files and 9.2 Exercise Files, 10.1 Course Files and 10.2 Exercise Files, 11.1 Course Files and 11.2 Exercise Files, 12.1 Course Files and 12.2 Exercise Files, 13.1 Course Files and 13.2 Exercise Files

>>>>>>> 224a89c570a26cc8c6ad9b67b6f2e0f3c6615718
