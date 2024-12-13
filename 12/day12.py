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

# Part 2
region_data = {}
visited = set()

for iy in range(m):
    for ix in range(n):
        if (iy, ix) in visited: continue
        
        plant_type = area_map[iy][ix]
        
        queue = [(iy, ix)]
        reg_area, reg_peri = 0, 0

        left_verts = {} # left verticals
        right_verts = {}
        top_hors = {} # top horizontals
        bottom_hors = {}

        while queue:
            qy, qx = queue.pop()
            if (qy, qx) in visited: continue
            visited.add((qy, qx))

            # fences - True -> needs fence ; False -> no fence (same plant)
            right_fence = qx >= n-1 or area_map[qy][qx+1] != plant_type
            left_fence = qx <= 0 or area_map[qy][qx-1] != plant_type
            top_fence = qy <= 0 or area_map[qy-1][qx] != plant_type
            bottom_fence = qy >= m-1 or area_map[qy+1][qx] != plant_type

            if left_fence: 
                left_verts[qx] = left_verts.get(qx, []) + [qy]
            else: queue.append((qy, qx-1))
            if right_fence: 
                right_verts[qx] = right_verts.get(qx, []) + [qy]
            else: queue.append((qy, qx+1))
            if top_fence: 
                top_hors[qy] = top_hors.get(qy, []) + [qx]
            else: queue.append((qy-1, qx))
            if bottom_fence: 
                bottom_hors[qy] = bottom_hors.get(qy, []) + [qx]
            else: queue.append((qy+1, qx))

            reg_area += 1
        
        for side in (left_verts, right_verts, top_hors, bottom_hors):
            for k, v in side.items():
                v.sort()
                for i in range(1, len(v)):
                    if v[i] - v[i-1] > 1:
                        reg_peri += 1
                reg_peri += 1
        
        region_data[plant_type] = region_data.get(plant_type, []) + [{
            "area": reg_area,
            "perimeter": reg_peri
        }]

total_price = 0
for plant_type, regions in region_data.items():
    for region in regions:
        total_price += region["area"] * region["perimeter"]

print(f"The new total price of fencing all regions on my map is {total_price}")