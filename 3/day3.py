# Advent of Code 2025
# Day 3
# https://adventofcode.com/2024/day/3
####################################################################

# imports


# reading the puzzle input

# SET PATH HERE
####################################
file_path = "3/day3_input1.txt" # path to the input file
####################################

# PREPARE CONTENT VARS HERE
####################################
memory = None
####################################

try:
    with open(file_path, 'r') as file:

        # PROCESS THE FILE CONTENTS HERE
        ########################################

        memory = "".join(line for line in file)

        ########################################

except FileNotFoundError:
    print(f"Error: File not found at {file_path}")
except Exception as e:
    print(f"An error occurred while reading the file: {e}")


# puzzle solution

# Part 1
ints = set(("0", "1", "2", "3", "4", "5", "6", "7", "8", "9"))
default_states = [")", "int", ",", "int", "(", "l", "u", "m"]
states = default_states.copy()
instructions = []
curr_instr = []
parsing = False
start = 0
i = 0
while i < len(memory):
    c = memory[i]
    if not parsing and c == "m":
        parsing = True
        states = default_states.copy()
        states.pop()
        curr_instr = []
    elif parsing:
        if c == states[-1]:
            states.pop()
            if not states:
                parsing = False
                instructions.append(curr_instr)
        elif states.pop() == "int":
            start = i
            while c in ints:
                i += 1
                c = memory[i]
            if i - start > 0:
                curr_instr.append(int(memory[start:i]))
            continue
        else:
            parsing = False
    i += 1

result = 0
for ins in instructions:
    result += ins[0] * ins[1]
print(f"If you add up all the results of the multiplications, you get {result}")

# Part 2
ints = set(("0", "1", "2", "3", "4", "5", "6", "7", "8", "9"))
mul_default_states = [")", "int", ",", "int", "(", "l", "u", "m"]
mul_states = mul_default_states.copy()
instructions = []
curr_instr = []
parsing_mul = False
enabled = True
start = 0
i = 0
while i < len(memory):
    c = memory[i]
    if memory[i:i+4] == "do()":
        i += 3
        enabled = True
    elif memory[i:i+7] == "don't()":
        i += 6
        enabled = False
    elif enabled:
        if not parsing_mul and c == "m":
            parsing_mul = True
            mul_states = mul_default_states.copy()
            mul_states.pop()
            curr_instr = []
        elif parsing_mul:
            if c == mul_states[-1]:
                mul_states.pop()
                if not mul_states:
                    parsing_mul = False
                    instructions.append(curr_instr)
            elif mul_states.pop() == "int":
                start = i
                while c in ints:
                    i += 1
                    c = memory[i]
                if i - start > 0:
                    curr_instr.append(int(memory[start:i]))
                continue
            else:
                parsing_mul = False
    i += 1

result = 0
for ins in instructions:
    result += ins[0] * ins[1]
print(f"If you add up all the results of just the enabled multiplications, you get {result}")