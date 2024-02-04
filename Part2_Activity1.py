import traceback

def write_to_file(filename, data):
    try:
        with open(filename, 'w') as file:
            file.write(data)
    except Exception as e:
        print(f"An error occurred while writing to the file: {filename}")
        traceback.print_exc()

# Example usage:
# This will write "Hello, world!" to a file named "example.txt".
write_to_file('example.txt', 'Hello, world!')
