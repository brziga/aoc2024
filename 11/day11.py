# Advent of Code 2025
# Day 11
# https://adventofcode.com/2024/day/11
####################################################################

# imports


# globals
####################################
BLINKS = 25
####################################

# reading the puzzle input

# SET PATH HERE
####################################
file_path = "11\day11_input1.txt" # path to the input file
####################################

# PREPARE CONTENT VARS HERE
####################################
stone_arrangement = []
####################################

try:
    with open(file_path, 'r') as file:

        # PROCESS THE FILE CONTENTS HERE
        ########################################

        [stone_arrangement.append(int(stone)) for stone in file.readline().strip().split(" ")]

        ########################################

except FileNotFoundError:
    print(f"Error: File not found at {file_path}")
except Exception as e:
    print(f"An error occurred while reading the file: {e}")


# puzzle solution

def change_stone(stone: int) -> list:
    # change the stone according to the first applicable rule
    # return new stone value
    #     since the result can be 2 stones, it always returns a list
    if stone == 0: return [1]
    elif len(stone_string := str(stone)) % 2 == 0: # yay for walrus operator
        return [int(stone_string[:len(stone_string)//2]), int(stone_string[len(stone_string)//2:])]
    else:
        return [stone * 2024]

# Part 1
for b in range(BLINKS):
    new_arrangement = []
    for stone in stone_arrangement:
        new_arrangement += change_stone(stone)
    stone_arrangement = new_arrangement
    # print(f"After {b+1} blink{'s' if b != 0 else ''}:\n{stone_arrangement}")

print(f"After blinking {BLINKS} times, I will have {len(stone_arrangement)} stones")