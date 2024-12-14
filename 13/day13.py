# Advent of Code 2025
# Day 13
# https://adventofcode.com/2024/day/13
####################################################################

# imports


# globals
####################################
COST_A = 3 # cost to push button A
COST_B = 1 # cost to push button B
####################################

# reading the puzzle input

# SET PATH HERE
####################################
file_path = "13\day13_input1.txt" # path to the input file
####################################

# PREPARE CONTENT VARS HERE
####################################
machines = []
####################################

try:
    with open(file_path, 'r') as file:

        # PROCESS THE FILE CONTENTS HERE
        ########################################

        line = file.readline()
        while line:
            button_a = line.strip().split(" ")
            line = file.readline()
            button_b = line.strip().split(" ")
            line = file.readline()
            prize = line.strip().split(" ")
            new_machine = {
                "A": [int(button_a[2][2:-1]), int(button_a[3][2:])], # X+, Y+
                "B": [int(button_b[2][2:-1]), int(button_b[3][2:])],
                "prize": [int(prize[1][2:-1]), int(prize[2][2:])]
            }
            machines.append(new_machine)

            line = file.readline()
            if line.strip() == "": line = file.readline() # skip the empty line

        ########################################

except FileNotFoundError:
    print(f"Error: File not found at {file_path}")
except Exception as e:
    print(f"An error occurred while reading the file: {e}")


# puzzle solution

# Part 1
fewest_tokens = 0

for machine in machines:
    lowest_tokens = None
    for a in range(0, 100):
        for b in range(0, 100):
            x = a * machine["A"][0] + b * machine["B"][0]
            y = a * machine["A"][1] + b * machine["B"][1]
            if x == int(machine["prize"][0]) and y == int(machine["prize"][1]):
                token_cost = a * COST_A + b * COST_B
                if not lowest_tokens: lowest_tokens = token_cost
                else: lowest_tokens =  token_cost if token_cost < lowest_tokens else lowest_tokens
    if lowest_tokens:
        fewest_tokens += lowest_tokens
    # print(f"Machine: {machine}, lowest tokens: {lowest_tokens}")

print(f"The fewest tokens I would have to spend to win all possible prizes is {fewest_tokens}")