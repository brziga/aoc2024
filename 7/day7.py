# Advent of Code 2025
# Day 7
# https://adventofcode.com/2024/day/7
####################################################################

# imports


# reading the puzzle input

# SET PATH HERE
####################################
file_path = "7/day7_input1.txt" # path to the input file
####################################

# PREPARE CONTENT VARS HERE
####################################
values = []
numbers = []
n = 0
####################################

try:
    with open(file_path, 'r') as file:

        # PROCESS THE FILE CONTENTS HERE
        ########################################

        for line in file:
            split = line.strip().split(": ")
            values.append(int(split[0]))
            numbers.append([int(x) for x in split[1].split(" ")])
            n += 1

        ########################################

except FileNotFoundError:
    print(f"Error: File not found at {file_path}")
except Exception as e:
    print(f"An error occurred while reading the file: {e}")


# puzzle solution

# Part 1
ops = {"+": lambda x, y: x + y, "*": lambda x, y: x * y}
total_result = 0
for i in range(n):
    val = values[i]
    nums = numbers[i]
    queue = []
    possible = False
    for o in ops:
        queue.append((nums, o))
    while queue:
        curr_n, curr_op = queue.pop()
        if len(curr_n) == 2:
            if ops[curr_op](curr_n[0], curr_n[1]) == val:
                possible = True
                break
        else:
            new_n = [ops[curr_op](curr_n[0], curr_n[1])] + curr_n[2:]
            for o in ops:
                queue.append((new_n, o))
    if possible:
        total_result += val

print(f"Their total calibration result is {total_result}")

# Part 2
ops = {"+": lambda x, y: x + y, "*": lambda x, y: x * y, "||": lambda x, y: int(str(x) + str(y))}
total_result = 0
for i in range(n):
    val = values[i]
    nums = numbers[i]
    queue = []
    possible = False
    for o in ops:
        queue.append((nums, o))
    while queue:
        curr_n, curr_op = queue.pop()
        if len(curr_n) == 2:
            if ops[curr_op](curr_n[0], curr_n[1]) == val:
                possible = True
                break
        else:
            new_n = [ops[curr_op](curr_n[0], curr_n[1])] + curr_n[2:]
            for o in ops:
                queue.append((new_n, o))
    if possible:
        total_result += val

print(f"Their total calibration result is {total_result}")