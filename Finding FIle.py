import os

def find_file():
    if os.path.exists(file_path):    #returns a boolean value
        print("File found.")
    else:
        print("File not found.")
        create = input("Do you want to create the file? (y/n): ")
        if create.lower() == 'y':
            with open(file_path, 'w') as file:    # "x" is used to create if does not exist
                print("File created successfully.")  # "r" is used to extract the data from a file into a displayable outnput
        
file_path = input("Enter the file path: ")     #Both relative and absolute path are acceptable
find_file()
