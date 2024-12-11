# Advent of Code 2025
# Day 10
# https://adventofcode.com/2024/day/10
####################################################################

# imports


# globals
####################################

####################################

# reading the puzzle input

# SET PATH HERE
####################################
file_path = "10\day10_input1.txt" # path to the input file
####################################

# PREPARE CONTENT VARS HERE
####################################
topo_map = []
####################################

try:
    with open(file_path, 'r') as file:

        # PROCESS THE FILE CONTENTS HERE
        ########################################

        for line in file:
            topo_map.append([int(height) for height in list(line.strip())])

        ########################################

except FileNotFoundError:
    print(f"Error: File not found at {file_path}")
except Exception as e:
    print(f"An error occurred while reading the file: {e}")


# puzzle solution

# Part 1
trailheads = set()
m, n = len(topo_map), len(topo_map[0])
for y in range(m):
    for x in range(n):
        if topo_map[y][x] == 0:
            trailheads.add((y, x))
th_scores = 0
moves = ((0, 1), (1, 0), (0, -1), (-1, 0))
for th in iter(trailheads):
    nines = set()
    queue = [(topo_map[th[0]][th[1]], th)]
    while queue:
        qval, (qy, qx) = queue.pop() # pops last, but it's O(1) and we are exploring all options anyway
        for my, mx in moves:
            new_y, new_x = qy + my, qx + mx
            if 0 <= new_y < m and 0 <= new_x < n:
                new_val = topo_map[new_y][new_x]
                if new_val == qval + 1:
                    if new_val == 9:
                        nines.add((new_y, new_x))
                    else:
                        queue.append((new_val, (new_y, new_x)))
    th_scores += len(nines)

print(f"The sum of the scores of all trailheads on my topographic map is {th_scores}")