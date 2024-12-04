# Advent of Code 2025
# Day 4
# https://adventofcode.com/2024/day/4
####################################################################

# imports


# reading the puzzle input

# SET PATH HERE
####################################
file_path = "4/day4_input1.txt" # path to the input file
####################################

# PREPARE CONTENT VARS HERE
####################################
text = []
####################################

try:
    with open(file_path, 'r') as file:

        # PROCESS THE FILE CONTENTS HERE
        ########################################

        for line in file:
            text.append(line.strip())

        ########################################

except FileNotFoundError:
    print(f"Error: File not found at {file_path}")
except Exception as e:
    print(f"An error occurred while reading the file: {e}")


# puzzle solution

# Part 1
m, n = len(text), len(text[0])
xmas = "XMAS"
count = 0
xs = []
for y in range(m):
    for x in range(n):
        if text[y][x] == "X":
            xs.append((y, x))

for y, x in xs:
    if x + 3 < n and text[y][x:x+4] == xmas: count += 1 # l -> r
    if x - 3 >= 0 and text[y][x-3:x+1][::-1] == xmas: count += 1 # r -> l
    if y + 3 < m and text[y][x] + text[y+1][x] + text[y+2][x] + text[y+3][x] == xmas: count += 1 # t -> b
    if y - 3 >= 0 and text[y][x] + text[y-1][x] + text[y-2][x] + text[y-3][x] == xmas: count += 1 # b -> t
    if x + 3 < n and y + 3 < m and text[y][x] + text[y+1][x+1] + text[y+2][x+2] + text[y+3][x+3] == xmas: count += 1 # tl -> br
    if x + 3 < n and y - 3 >= 0 and text[y][x] + text[y-1][x+1] + text[y-2][x+2] + text[y-3][x+3] == xmas: count += 1 # bl -> tr
    if x - 3 >= 0 and y + 3 < m and text[y][x] + text[y+1][x-1] + text[y+2][x-2] + text[y+3][x-3] == xmas: count += 1 # tr -> bl
    if x - 3 >= 0 and y - 3 >= 0 and text[y][x] + text[y-1][x-1] + text[y-2][x-2] + text[y-3][x-3] == xmas: count += 1 # br -> tl

print(f"XMAS appears {count} times")
