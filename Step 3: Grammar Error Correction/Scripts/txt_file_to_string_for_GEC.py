file_path = 'final_text.txt'

try:
    with open(file_path, 'r') as file:
        file_contents = file.read()
        print("File content stored:")
        print(file_contents)
except FileNotFoundError:
    print(f"The file '{file_path}' was not found.")
except Exception as e:
    print(f"An error occurred: {e}")
