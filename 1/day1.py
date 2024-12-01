# Advent of Code 2025
# Day 
####################################################################

# imports


# reading the puzzle input

# SET PATH HERE
####################################
file_path = "1/day1_input1.txt" # path to the input file
####################################

# PREPARE CONTENT VARS HERE
####################################
col1 = []
col2 = []
####################################

try:
    with open(file_path, 'r') as file:

        # PROCESS THE FILE CONTENTS HERE
        ########################################

        for line in file:
            arr = line.split("   ")
            col1.append(int(arr[0]))
            col2.append(int(arr[1]))

        ########################################

except FileNotFoundError:
    print(f"Error: File not found at {file_path}")
except Exception as e:
    print(f"An error occurred while reading the file: {e}")


# puzzle solution

# Part 1
n = len(col1)
diff = 0
col1.sort()
col2.sort()
for i in range(n):
    diff += abs(col1[i] - col2[i])

print(f"Part 1: The total distance between the lists is {diff}")
