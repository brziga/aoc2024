# Advent of Code 2025
# Day 6
# https://adventofcode.com/2024/day/6
####################################################################

# imports
import copy

# reading the puzzle input

# SET PATH HERE
####################################
file_path = "6/day6_input1.txt" # path to the input file
####################################

# PREPARE CONTENT VARS HERE
####################################
area = []
####################################

try:
    with open(file_path, 'r') as file:

        # PROCESS THE FILE CONTENTS HERE
        ########################################

        for line in file:
            area.append(list(line.strip()))

        ########################################

except FileNotFoundError:
    print(f"Error: File not found at {file_path}")
except Exception as e:
    print(f"An error occurred while reading the file: {e}")


# puzzle solution

# Part 1
area_map = copy.deepcopy(area)
m, n = len(area_map), len(area_map[0])
guard_orients = {"^", "<", "v", ">"}
initial_guard_pos = None

for y in range(m):
    for x in range(n):
        if area_map[y][x] in guard_orients:
            initial_guard_pos = (y, x)
            break
    if initial_guard_pos: break

directions = {"^": (-1, 0), "<": (0, -1), "v": (1, 0), ">": (0, 1)}
in_area = True
visited_count = 0
turns = set()
visited = set()
guard = area_map[initial_guard_pos[0]][initial_guard_pos[1]]
guard_pos = initial_guard_pos
while in_area:
    # move the guard
    y, x = guard_pos
    while 0 <= y < m and 0 <= x < n and area_map[y][x] != "#":
        if area_map[y][x] != "X": visited_count += 1
        area_map[y][x] = "X"
        visited.add((y, x))
        guard_pos = (y, x)
        y += directions[guard][0]
        x += directions[guard][1]
    if y < 0 or y >= m or x < 0 or x >= n:
        # area escaped
        in_area = False
        break
    else:
        # hit an obstacle
        turns.add((y, x))
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

# Part 2
obstructions = [] # possible positions for obstructions
visited.remove(initial_guard_pos) # remove the guard's initial position
visit_iter = iter(visited)
for ypos, xpos in visit_iter:
    # place obstruction
    obstructed_area = copy.deepcopy(area)
    obstructed_area[ypos][xpos] = "#"
    # simulate guard movement and detect a loop
    in_area = True
    new_turns = set()
    guard_pos = initial_guard_pos
    guard = area[initial_guard_pos[0]][initial_guard_pos[1]]
    while in_area:
        y, x = guard_pos
        while 0 <= y < m and 0 <= x < n and obstructed_area[y][x] != "#":
            obstructed_area[y][x] = "X"
            guard_pos = (y, x)
            y += directions[guard][0]
            x += directions[guard][1]
        if y < 0 or y >= m or x < 0 or x >= n:
            # area escaped
            in_area = False
            break
        else:
            # hit an obstacle
            if (guard_pos[0], guard_pos[1], guard) in new_turns:
                # loop detected
                break
            else:
                new_turns.add((guard_pos[0], guard_pos[1], guard))
            match guard:
                case "^":
                    guard = ">"
                case ">":
                    guard = "v"
                case "v":
                    guard = "<"
                case "<":
                    guard = "^"
    if in_area:
        obstructions.append((ypos, xpos))

print(f"{len(obstructions)} positions can be chosen for the obstruction")