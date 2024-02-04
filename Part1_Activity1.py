import random

def roll_dice(num_dice, num_sides):
    total = 0
    for _ in range(num_dice):
        roll = random.randint(1, num_sides)
        total += roll
    return total

num_dice = 2
num_sides = 6


result = roll_dice(num_dice, num_sides) 
print(f"Rolling {num_dice} dice with {num_sides} sides each. Total: {result}")


