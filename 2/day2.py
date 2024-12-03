# Advent of Code 2025
# Day 2
# https://adventofcode.com/2024/day/2
####################################################################

# imports


# reading the puzzle input

# SET PATH HERE
####################################
file_path = "2/day2_input1.txt" # path to the input file
####################################

# PREPARE CONTENT VARS HERE
####################################
reports = []
####################################

try:
    with open(file_path, 'r') as file:

        # PROCESS THE FILE CONTENTS HERE
        ########################################

        for line in file:
            reports.append([int(x) for x in line.strip().split(" ")])

        ########################################

except FileNotFoundError:
    print(f"Error: File not found at {file_path}")
except Exception as e:
    print(f"An error occurred while reading the file: {e}")


# puzzle solution

# Part 1
safe = 0
for r in reports:
    increasing = all(r[i] < r[i + 1] for i in range(len(r) - 1))
    decreasing = all(r[i] > r[i + 1] for i in range(len(r) - 1))
    diff = all(1 <= abs(r[i] - r[i + 1]) <= 3 for i in range(len(r) - 1))
    if (increasing or decreasing) and diff:
        safe += 1

print(f"{safe} reports are safe")

# Part 2
safe = 0
for r in reports:
    for j in range(len(r)):
        rc = r.copy()
        del rc[j]
        increasing = all(rc[i] < rc[i + 1] for i in range(len(rc) - 1))
        decreasing = all(rc[i] > rc[i + 1] for i in range(len(rc) - 1))
        diff = all(1 <= abs(rc[i] - rc[i + 1]) <= 3 for i in range(len(rc) - 1))
        if (increasing or decreasing) and diff:
            safe += 1
            break

print(f"{safe} reports are actually safe")