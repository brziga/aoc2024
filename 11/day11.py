# Advent of Code 2025
# Day 11
# https://adventofcode.com/2024/day/11
####################################################################

# imports
import time
from functools import cache

# globals
####################################
BLINKS = 25
BLINKS_2 = 75
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

initial_arrangement = stone_arrangement.copy()

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

def num_stones(stone, blinks):
    # how many stones after blinks
    if blinks == 0: return 1
    if stone == 0: return num_stones(1, blinks - 1)
    elif len(stone_string := str(stone)) % 2 == 0:
        return num_stones(int(stone_string[:len(stone_string)//2]), blinks - 1) + num_stones(int(stone_string[len(stone_string)//2:]), blinks - 1)
    else:
        return num_stones(stone * 2024, blinks - 1)

# print(num_stones(125, 6))

@cache
def num_stones_cached(stone, blinks):
    # how many stones after blinks
    if blinks == 0: return 1
    if stone == 0: return num_stones_cached(1, blinks - 1)
    elif len(stone_string := str(stone)) % 2 == 0:
        return num_stones_cached(int(stone_string[:len(stone_string)//2]), blinks - 1) + num_stones_cached(int(stone_string[len(stone_string)//2:]), blinks - 1)
    else:
        return num_stones_cached(stone * 2024, blinks - 1)


# Part 2

# Let's test how long it takes for 25 blinks with both approaches
####################################
# print("\nTesting the speed of different approaches...:\n")
# test_blinks = 30

# stone_arrangement = initial_arrangement.copy()
# start_time = time.time()
# for b in range(test_blinks):
#     new_arrangement = []
#     for stone in stone_arrangement:
#         new_arrangement += change_stone(stone)
#     stone_arrangement = new_arrangement
# end_time = time.time()
# print("Approach 1 keeps all the stones in a list and simulates the blinks one by one.")
# print(f"It took {(end_time - start_time) * 1000} ms for {test_blinks} blinks. The result is {len(stone_arrangement)} stones.\n")

# stone_arrangement = initial_arrangement.copy()
# start_time = time.time()
# n_stones = 0
# for s in stone_arrangement:
#     n_stones += num_stones(s, test_blinks)
# end_time = time.time()
# print("Approach 2 uses a recursive function to calculate the number of stones that exist after the given number of blinks for each stone.")
# print(f"It took {(end_time - start_time) * 1000} ms for {test_blinks} blinks. The result is {n_stones} stones.\n")

# stone_arrangement = initial_arrangement.copy()
# start_time = time.time()
# n_stones = 0
# for s in stone_arrangement:
#     n_stones += num_stones_cached(s, test_blinks)
# end_time = time.time()
# print("Approach 3 uses the recursive function from approach 2, but WITH CACHING (i.e. memoization) to calculate the number of stones that exist after the given number of blinks for each stone.")
# print(f"It took {(end_time - start_time) * 1000} ms for {test_blinks} blinks. The result is {n_stones} stones.\n")
####################################

stone_arrangement = initial_arrangement.copy()
start_time = time.time()
n_stones = 0
for s in stone_arrangement:
    n_stones += num_stones_cached(s, BLINKS_2)
end_time = time.time()
# print(f"After blinking {BLINKS_2} times, I will have {n_stones} stones. It took {(end_time - start_time) * 1000} ms to calculate.")
print(f"After blinking {BLINKS_2} times, I will have {n_stones} stones")
