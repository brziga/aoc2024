# Advent of Code 2025
# Day 1
# https://adventofcode.com/2024/day/1
####################################################################

# imports


# reading the puzzle input

# SET PATH HERE
####################################
file_path = "1/day1_input1.txt" # path to the input file
####################################

# PREPARE CONTENT VARS HERE
####################################
col1 = []
col2 = []
####################################

try:
    with open(file_path, 'r') as file:

        # PROCESS THE FILE CONTENTS HERE
        ########################################

        for line in file:
            arr = line.split("   ")
            col1.append(int(arr[0]))
            col2.append(int(arr[1]))

        ########################################

except FileNotFoundError:
    print(f"Error: File not found at {file_path}")
except Exception as e:
    print(f"An error occurred while reading the file: {e}")


# puzzle solution

# Part 1
n = len(col1)
diff = 0
col1.sort()
col2.sort()
for i in range(n):
    diff += abs(col1[i] - col2[i])

print(f"Part 1: The total distance between the lists is {diff}")

# Part 2
rigth_occs = {}
for i in range(n):
    rigth_occs[col2[i]] = rigth_occs.get(col2[i], 0) + 1
similarity = 0
for i in range(n):
    similarity += col1[i] * (rigth_occs[col1[i]] if col1[i] in rigth_occs.keys() else 0)

print(f"Part 2: The similarity between the lists is {similarity}")