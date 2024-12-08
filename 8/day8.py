# Advent of Code 2025
# Day 8
# https://adventofcode.com/2024/day/8
####################################################################

# imports


# reading the puzzle input

# SET PATH HERE
####################################
file_path = "8\day8_input1.txt" # path to the input file
####################################

# PREPARE CONTENT VARS HERE
####################################
area_map = []
####################################

try:
    with open(file_path, 'r') as file:

        # PROCESS THE FILE CONTENTS HERE
        ########################################

        for line in file:
            area_map.append(line.strip())

        ########################################

except FileNotFoundError:
    print(f"Error: File not found at {file_path}")
except Exception as e:
    print(f"An error occurred while reading the file: {e}")


# puzzle solution

# Part 1
m, n = len(area_map), len(area_map[0])
antenna_map = {}
for i in range(m):
    for j in range(n):
        if area_map[i][j] != ".":
            antenna_map[area_map[i][j]] = antenna_map.get(area_map[i][j], []) + [(i, j)]

antinodes = set()
for freq, ants in antenna_map.items():
    potential_antinodes = set()
    for i in range(len(ants)):
        for j in range(i + 1, len(ants)):
            diff_y = ants[i][0] - ants[j][0]
            diff_x = ants[i][1] - ants[j][1]
            a1 = (ants[i][0] + diff_y, ants[i][1] + diff_x)
            a2 = (ants[j][0] - diff_y, ants[j][1] - diff_x)
            for a in (a1, a2):
                if 0 <= a[0] < m and 0 <= a[1] < n:
                    antinodes.add(a)

print(f"{len(antinodes)} unique locations within the map contain an antinode")