import traceback

# Function to write data to a file
# Activity 1
def write_to_file(filename, data):
    try:
        with open(filename, 'w') as file:
            file.write(data)
    except Exception as e:
        print(f"An error occurred while writing to the file: {filename}")
        traceback.print_exc()

# Function to read data from a file
#Activity 2
def read_from_file(filename):
    try:
        with open(filename, 'r') as file:
            return file.read()
    except Exception as e:
        print(f"An error occurred while reading from the file: {filename}")
        traceback.print_exc()


# Function to append data to a file
#Activity 3
def append_to_file(filename, data):
    try:
        with open(filename, 'a') as file:
            file.write(data)
    except Exception as e:
        print(f"An error occurred while appending to the file: {filename}")
        traceback.print_exc()

# Demonstration of the functions
if __name__ == "__main__":
    # Writing to a file
    write_to_file('sample.txt', 'Hello, Yuchen!\n')

    # Reading from a file
    content = read_from_file('sample.txt')
    print(f"Content of the file: {content}")

    # Appending to a file
    append_to_file('sample.txt', 'Andrew Sun, World!\n')
    updated_content = read_from_file('sample.txt')
    print(f"Updated content of the file: {updated_content}")
