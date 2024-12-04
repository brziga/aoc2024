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
count_xmas = 0
xs = []
for y in range(m):
    for x in range(n):
        if text[y][x] == "X":
            xs.append((y, x))

for y, x in xs:
    if x + 3 < n and text[y][x:x+4] == xmas: count_xmas += 1 # l -> r
    if x - 3 >= 0 and text[y][x-3:x+1][::-1] == xmas: count_xmas += 1 # r -> l
    if y + 3 < m and text[y][x] + text[y+1][x] + text[y+2][x] + text[y+3][x] == xmas: count_xmas += 1 # t -> b
    if y - 3 >= 0 and text[y][x] + text[y-1][x] + text[y-2][x] + text[y-3][x] == xmas: count_xmas += 1 # b -> t
    if x + 3 < n and y + 3 < m and text[y][x] + text[y+1][x+1] + text[y+2][x+2] + text[y+3][x+3] == xmas: count_xmas += 1 # tl -> br
    if x + 3 < n and y - 3 >= 0 and text[y][x] + text[y-1][x+1] + text[y-2][x+2] + text[y-3][x+3] == xmas: count_xmas += 1 # bl -> tr
    if x - 3 >= 0 and y + 3 < m and text[y][x] + text[y+1][x-1] + text[y+2][x-2] + text[y+3][x-3] == xmas: count_xmas += 1 # tr -> bl
    if x - 3 >= 0 and y - 3 >= 0 and text[y][x] + text[y-1][x-1] + text[y-2][x-2] + text[y-3][x-3] == xmas: count_xmas += 1 # br -> tl

print(f"XMAS appears {count_xmas} times")

# Part 2
def pattern_match(square, pattern):
    for i in range(len(square)):
        for j in range(len(square[0])):
            if pattern[i][j] != "." and square[i][j] != pattern[i][j]:
                return False
    return True

count_mas = 0
patterns = [
    [["M", ".", "S"], [".", "A", "."], ["M", ".", "S"]],
    [["S", ".", "S"], [".", "A", "."], ["M", ".", "M"]],
    [["M", ".", "M"], [".", "A", "."], ["S", ".", "S"]],
    [["S", ".", "M"], [".", "A", "."], ["S", ".", "M"]],
]
for y in range(m - 2):
    for x in range(n - 2):
        square = [text[y][x:x+3], text[y+1][x:x+3], text[y+2][x:x+3]]
        for p in patterns:
            if pattern_match(square, p):
                count_mas += 1
                break

print(f"An X-MAS appears {count_mas} times")
