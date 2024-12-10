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

frag_blocks = blocks.copy()
n = len(frag_blocks)
i, j = 0, n - 1
while i < j:
    while frag_blocks[i] != EMPTY: i += 1
    while frag_blocks[j] == EMPTY: j -= 1
    if i >= j: break
    frag_blocks[i], frag_blocks[j] = frag_blocks[j], frag_blocks[i]
    i += 1
    j -= 1
# print("".join(frag_blocks))
# print("0099811188827773336446555566..............")

frag_checksum = 0
for i in range(n):
    if frag_blocks[i] == EMPTY: break
    frag_checksum += i * int(frag_blocks[i])

print(f"The resulting filesystem checksum is {frag_checksum}")

# Part 2
defrag_blocks = blocks.copy()
n = len(defrag_blocks)
i, j = 0, n - 1
while j > 0:
    # find block of files
    while defrag_blocks[j] == EMPTY: j -= 1
    file_size, f = 0, defrag_blocks[j]
    while defrag_blocks[j - file_size] == f: file_size += 1

    # find big enough block of free space
    free_space = 0
    while i < j and free_space < file_size:
        while i < n and defrag_blocks[i] != EMPTY: i += 1
        if i >= j: break
        free_space = 0
        while i + free_space < n and defrag_blocks[i + free_space] == EMPTY: free_space += 1
        if free_space < file_size: i += free_space

    # swap the blocks
    if i < j and free_space >= file_size:
        for index in range(file_size):
            defrag_blocks[i + index], defrag_blocks[j - index] = defrag_blocks[j - index], defrag_blocks[i + index]
    
    i = 0
    j -= file_size

# print("".join(defrag_blocks))
# print("00992111777.44.333....5555.6666.....8888..")

defrag_checksum = 0
for i in range(n):
    if defrag_blocks[i] == EMPTY: continue
    defrag_checksum += i * int(defrag_blocks[i])

print(f"The resulting filesystem checksum is {defrag_checksum}")
# TODO: could be sped up by keeping track of the free spaces instead of iterating over the entire thing every time in search of them (... but not tonight i'm too tired)
#       ...can probably apply the same to track the files, but those are only iterated over once so whether this would speed it up is questionable