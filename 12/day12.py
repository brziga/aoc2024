# Advent of Code 2025
# Day 12
# https://adventofcode.com/2024/day/12
####################################################################

# imports


# globals
####################################

####################################

# reading the puzzle input

# SET PATH HERE
####################################
file_path = "12\day12_input1.txt" # path to the input file
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
            area_map.append([char for char in list(line.strip())])

        ########################################

except FileNotFoundError:
    print(f"Error: File not found at {file_path}")
except Exception as e:
    print(f"An error occurred while reading the file: {e}")


# puzzle solution

# Part 1
m, n = len(area_map), len(area_map[0])
region_data = {}
visited = set()

for iy in range(m):
    for ix in range(n):
        if (iy, ix) in visited: continue
        
        visited.add((iy, ix))
        queue = [(iy, ix)]
        reg_area, reg_peri = 0, 0

        while queue:
            qy, qx = queue.pop()
            plant_type = area_map[qy][qx]

            neigh_temp = ((qy, qx+1), (qy+1, qx), (qy, qx-1), (qy-1, qx))
            curr_peri = 0
            for nt in neigh_temp:
                if 0 <= nt[0] < m and 0 <= nt[1] < n: 
                    if area_map[nt[0]][nt[1]] != plant_type: curr_peri += 1
                    else:
                        if nt not in visited:
                            visited.add(nt)
                            queue.append(nt)
                else: curr_peri += 1 # edge of the map also needs a fence

            reg_area += 1
            reg_peri += curr_peri
        
        region_data[plant_type] = region_data.get(plant_type, []) + [{
            "area": reg_area,
            "perimeter": reg_peri
        }]

total_price = 0
for plant_type, regions in region_data.items():
    for region in regions:
        total_price += region["area"] * region["perimeter"]

print(f"The total price of fencing all regions on my map is {total_price}")