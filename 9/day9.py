# Advent of Code 2025
# Day 9
# https://adventofcode.com/2024/day/9
####################################################################

# imports


# globals
####################################
EMPTY = "."
####################################

# reading the puzzle input

# SET PATH HERE
####################################
file_path = "9\day9_input1.txt" # path to the input file
####################################

# PREPARE CONTENT VARS HERE
####################################
disk_map = ""
####################################

try:
    with open(file_path, 'r') as file:

        # PROCESS THE FILE CONTENTS HERE
        ########################################

        disk_map = file.read().strip()

        ########################################

except FileNotFoundError:
    print(f"Error: File not found at {file_path}")
except Exception as e:
    print(f"An error occurred while reading the file: {e}")


# puzzle solution

# Part 1
blocks = []
files = True # True for files, False for free space
for i in range(len(disk_map)):
    block_size = int(disk_map[i])
    for j in range(block_size):
        blocks.append(str(i//2) if files else EMPTY)
    files = not files
# print("".join(blocks))
# print("00...111...2...333.44.5555.6666.777.888899")

n = len(blocks)
i, j = 0, n - 1
while i < j:
    while blocks[i] != EMPTY: i += 1
    while blocks[j] == EMPTY: j -= 1
    if i >= j: break
    blocks[i], blocks[j] = blocks[j], blocks[i]
    i += 1
    j -= 1
# print("".join(blocks))
# print("0099811188827773336446555566..............")

checksum = 0
for i in range(n):
    if blocks[i] == EMPTY: break
    checksum += i * int(blocks[i])

print(f"The resulting filesystem checksum is {checksum}")