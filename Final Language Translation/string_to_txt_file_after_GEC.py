file_path = 'final_text.txt'

try:
    with open(file_path, 'w') as file:
        file.write(final_string) # final_string is the GEC string output after the notebooks 
    print(f"Content successfully written to '{file_path}'.")
except Exception as e:
    print(f"An error occurred: {e}")