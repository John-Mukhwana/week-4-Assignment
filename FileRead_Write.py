
def modify_file_content(file_name):
    try:
        # Attempt to open and read the file
        with open(file_name, 'r') as file:
            content = file.read()

        # Modify the content (convert to uppercase)
        modified_content = content.upper()

        # Create a new file and write the modified content
        new_file_name = "modified_" + file_name
        with open(new_file_name, 'w') as new_file:
            new_file.write(modified_content)

        print(f"Modified content has been written to {new_file_name}")

    except FileNotFoundError:
        print("Error: The file does not exist. Please check the file name and try again.")
    except PermissionError:
        print("Error: You do not have permission to read this file.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

# Main function to interact with the user
if __name__ == "__main__":
    user_file = input("Enter the filename to read: ")
    modify_file_content(user_file)
