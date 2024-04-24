def create_file():
    try:
        with open("my_file.txt", "w") as file:
            file.write("File handling is a fundamental aspect of programming that involves working with files stored on a computer's storage system. It allows a program to read data from files, write data to files, create new files, delete files, and perform various operations on files.\n")
            file.write("12345\n")
            file.write("Exceptions are raised when the program encounters an error during its execution.\n")
    except FileNotFoundError:
        print("FileNotFoundError: The file path is incorrect or does not exist.")
    except PermissionError:
        print("PermissionError: You don't have permission to create the file.")
    else:
        print("File created successfully.")


def read_file():
    try:
        with open("my_file.txt", "r") as file:
            print("Contents of my_file.txt:")
            for line in file:
                print(line.strip())
    except FileNotFoundError:
        print("FileNotFoundError: The file does not exist.")
    except PermissionError:
        print("PermissionError: You don't have permission to read the file.")


def append_file():
    try:
        with open("my_file.txt", "a") as file:
            file.write("Appending line 1\n")
            file.write("Appending line 2\n")
            file.write("Appending line 3\n")
    except FileNotFoundError:
        print("FileNotFoundError: The file does not exist.")
    except PermissionError:
        print("PermissionError: You don't have permission to append to the file.")
    else:
        print("File appended successfully.")


if __name__ == "__main__":
    create_file()
    read_file()
    append_file()
    read_file()  
