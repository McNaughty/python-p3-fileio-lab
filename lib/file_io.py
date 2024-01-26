from pathlib import Path

def write_file(file_name, file_content):
    """Write content to a .txt file."""
    # Convert file_name to string and add .txt extension
    file_name_with_extension = str(file_name) + ".txt"
    
    # Open the file in write mode and write the content
    with open(file_name_with_extension, "w") as file:
        file.write(file_content)

def append_file(file_name, file_content):
    """Append content to a .txt file."""
    # Convert file_name to string and add .txt extension
    file_name_with_extension = str(file_name) + ".txt"
    
    # Open the file in append mode and append the content
    with open(file_name_with_extension, "a") as file:
        file.write(file_content)

def read_file(file_name):
    """Read content from a .txt file."""
    # Convert file_name to string and add .txt extension
    file_name_with_extension = str(file_name) + ".txt"
    
    # Open the file in read mode and read the content
    with open(file_name_with_extension, "r") as file:
        content = file.read()
    
    return content