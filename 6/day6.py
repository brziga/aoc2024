# Advent of Code 2025
# Day 6
# https://adventofcode.com/2024/day/6
####################################################################

# imports


# reading the puzzle input

# SET PATH HERE
####################################
file_path = "6/day6_input1.txt" # path to the input file
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
            area_map.append(list(line.strip()))

        ########################################

except FileNotFoundError:
    print(f"Error: File not found at {file_path}")
except Exception as e:
    print(f"An error occurred while reading the file: {e}")


# puzzle solution

# Part 1
m, n = len(area_map), len(area_map[0])
# vm, hm = {}, {} # vertical and horizontal mappings
guard_orients = {"^", "<", "v", ">"}
guard_pos = None

for y in range(m):
    for x in range(n):
        if area_map[y][x] in guard_orients:
            guard_pos = (y, x)
            break
    if guard_pos: break

directions = {"^": (-1, 0), "<": (0, -1), "v": (1, 0), ">": (0, 1)}
in_area = True
visited_count = 0
guard = area_map[y][x]
while in_area:
    # move the guard
    y, x = guard_pos
    while 0 <= y < m and 0 <= x < n and area_map[y][x] != "#":
        if area_map[y][x] != "X": visited_count += 1
        area_map[y][x] = "X"
        guard_pos = (y, x)
        y += directions[guard][0]
        x += directions[guard][1]
    if y < 0 or y >= m or x < 0 or x >= n:
        # area escaped
        in_area = False
        break
    else:
        # hit an obstacle
        match guard:
            case "^":
                guard = ">"
            case ">":
                guard = "v"
            case "v":
                guard = "<"
            case "<":
                guard = "^"

print(f"The guard will visit {visited_count} distinct positions before leaving the area")