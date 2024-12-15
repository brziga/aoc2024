# Advent of Code 2025
# Day 14
# https://adventofcode.com/2024/day/14
####################################################################

# imports


# globals
####################################
TEST_SPACE = {"wide": 11, "tall": 7}
PROBLEM_SPACE = {"wide": 101, "tall": 103}
SPACE_SIZE = PROBLEM_SPACE
SECONDS = 100
####################################

# reading the puzzle input

# SET PATH HERE
####################################
file_path = "14\day14_input1.txt" # path to the input file
####################################

# PREPARE CONTENT VARS HERE
####################################
robots = []
####################################

try:
    with open(file_path, 'r') as file:

        # PROCESS THE FILE CONTENTS HERE
        ########################################

        for line in file:
            line_string = line.strip().split(" ")
            pos_str = line_string[0][2:].split(",")
            vel_str = line_string[1][2:].split(",")
            robots.append({
                "pos": {"x": int(pos_str[0]), "y": int(pos_str[1])}, # x, y
                "vel": {"x": int(vel_str[0]), "y": int(vel_str[1])}  # x, y
            })

        ########################################

except FileNotFoundError:
    print(f"Error: File not found at {file_path}")
except Exception as e:
    print(f"An error occurred while reading the file: {e}")


# puzzle solution

# Part 1
robot_placements = {}
for i in range(len(robots)):
    robot_placements[i] = [robots[i]["pos"]["x"], robots[i]["pos"]["y"]]

for s in range(SECONDS):
    for i in range(len(robots)):
        # new x
        new_x = robot_placements[i][0] + robots[i]["vel"]["x"]
        # wrap x if out of bounds
        if new_x >= SPACE_SIZE["wide"]: new_x = new_x % SPACE_SIZE["wide"]
        elif new_x < 0: new_x = SPACE_SIZE["wide"] + new_x

        # new y
        new_y = robot_placements[i][1] + robots[i]["vel"]["y"]
        # wrap y if out of bounds
        if new_y >= SPACE_SIZE["tall"]: new_y = new_y % SPACE_SIZE["tall"]
        elif new_y < 0: new_y = SPACE_SIZE["tall"] + new_y

        robot_placements[i] = [new_x, new_y]
# [print(rp) for rp in robot_placements.values()]

### debug visualization ######################################################
matrix = [[0 for _ in range(SPACE_SIZE["wide"])] for _ in range(SPACE_SIZE["tall"])]

for pos in robot_placements.values():
    x, y = pos
    matrix[y][x] += 1

for y in range(SPACE_SIZE["tall"]):
    for x in range(SPACE_SIZE["wide"]):
        if matrix[y][x] == 0:
            matrix[y][x] = "."
        else:
            matrix[y][x] = str(matrix[y][x])

for row in matrix:
    print(" ".join(row))
###############################################################################

quadrants = [[0, 0], [0, 0]]
div_w = SPACE_SIZE["wide"] // 2
div_t = SPACE_SIZE["tall"] // 2
for i in range(len(robots)):
    rx, ry = robot_placements[i]
    if rx == div_w or ry == div_t: continue
    qx = min(ry // div_t, 1)
    qy = min(rx // div_w, 1)
    quadrants[qx][qy] += 1
# print("Quadrants:", quadrants)

safety_factor = quadrants[0][0] * quadrants[0][1] * quadrants[1][0] * quadrants[1][1]

print(f"The safety factor after exactly {SECONDS} seconds have elapsed will be {safety_factor}")