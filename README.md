# File Handling Script

This Python script demonstrates basic file handling operations such as creating, reading, and appending to a text file.

## Description

File handling is a fundamental aspect of programming that involves working with files stored on a computer's storage system. It allows a program to interact with external files, enabling tasks such as reading data from files, writing data to files and appending data to existing files.

## Functions
   
   ### create_file()
   This function creates a new text file named "my_file.txt" and writes initial content to it. It demonstrates how to handle file creation and writing operations.

   ### read_file()
   The read_file() function reads the contents of the "my_file.txt" file and displays them on the console. It showcases reading from a file and printing its contents.

   ### append_file()
   The append_file() function opens "my_file.txt" in append mode and appends additional lines of text to the existing content. It demonstrates how to add new data to an existing file without overwriting its contents.

## Error Handling
The script implements error handling using try-except blocks to manage potential file-related exceptions, such as FileNotFoundError and PermissionError. This ensures that the script handles errors gracefully and provides informative messages to the user.
