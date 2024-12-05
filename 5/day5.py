# Advent of Code 2025
# Day 5
# https://adventofcode.com/2024/day/5
####################################################################

# imports


# reading the puzzle input

# SET PATH HERE
####################################
file_path = "5/day5_input1.txt" # path to the input file
####################################

# PREPARE CONTENT VARS HERE
####################################
rules = {}
updates = []
####################################

try:
    with open(file_path, 'r') as file:

        # PROCESS THE FILE CONTENTS HERE
        ########################################

        mode = True # True for rules, False for updates
        for line in file:
            if line == "\n":
                mode = False
            else:
                if mode:
                    rule = line.strip().split("|")
                    if int(rule[0]) in rules.keys():
                        rules[int(rule[0])].add(int(rule[1]))
                    else:
                        rules[int(rule[0])] = set([int(rule[1])])
                    # rules[int(rule[0])] = rules.get(int(rule[0]), []) + ([int(rule[1])])
                else:
                    updates.append([int(x) for x in line.strip().split(",")])

        ########################################

except FileNotFoundError:
    print(f"Error: File not found at {file_path}")
except Exception as e:
    print(f"An error occurred while reading the file: {e}")


# puzzle solution

# Part 1
middle_sum = 0
for update in updates:
    # find out if update is in order
    in_order = True
    seen = set()
    for i in range(1, len(update)):
        seen.add(update[i-1])
        intersect = seen & rules.get(update[i], set())
        if intersect:
            in_order = False
            break
    if in_order:
        middle_sum += update[len(update)//2]
        if len(update) % 2 == 0: print(f"even length update: {update}")

print(f"If you add up the middle page number from correctly ordered updates, you get: {middle_sum}")