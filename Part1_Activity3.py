import random

def generate_random_number(min_val, max_val):
    return random.randint(min_val, max_val)

# Example usage:
min_val = 1
max_val = 100
random_number = generate_random_number(min_val, max_val)
print(f"The random number between {min_val} and {max_val} is {random_number}")
