import os

def list_directory_contents(path="."):
    try:
        contents = os.listdir(path)
        print(f"Contents of '{path}':")
        for item in contents:
            print(item)
    except FileNotFoundError:
        print("Error: Directory not found.")
    except PermissionError:
        print("Error: Permission denied.")

# Example usage
list_directory_contents(".")  # Lists the current directory