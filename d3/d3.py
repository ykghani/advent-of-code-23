'''Advent of Code 2023 Day 3: Gear Ratios'''
from pathlib import Path

script_dir = Path(__file__).parent
file_path = script_dir / 'd3_input.txt'

grid = []
with open(file_path, 'r') as f:
    for line in f:
        grid.append(line.strip())

y_lim = len(grid)
x_lim = len(grid[0])
i = j = 0

def find_number(start_i: int, x_lim: int, row):
    '''Returns the number and associated end index in a given grid'''
    number = row[start_i]
    i = start_i + 1
    while i < x_lim and row[i].isdigit():
        number += row[i]
        i += 1
    
    return int(number), i - 1

def is_part(start_i, end_i, curr_j, x_lim, y_lim, grid) -> bool:
    '''Returns True if there are no symbols adjacent to a number'''
    
    #Figure out bounding box
    min_row = max(0, curr_j - 1)
    max_row = min(curr_j + 1, y_lim - 1)
    min_col = max(0, start_i - 1)
    max_col = min(end_i + 1, x_lim - 1)
    
    for row in range(min_row, max_row + 1):
        for col in range(min_col, max_col + 1):
            if row == curr_j and start_i <= col <= end_i: 
                continue #skip the number
            
            if not grid[row][col].isdigit() and grid[row][col] != ".":
                return True
    
    return False

part_one = 0
while j < y_lim:
    i = 0
    while i < x_lim:
        if grid[j][i].isdigit():
            number, end_idx = find_number(start_i= i, x_lim= x_lim, row= grid[j])
            if is_part(i, end_idx, j, x_lim, y_lim, grid):
                part_one += number
                
            i = end_idx + 1
        else:
            i += 1
    j += 1
    
print(f"Part One: {part_one}")

def get_parts(i, j, x_lim, y_lim, grid):
    '''Returns all numbers around a starting point'''
    parts = set()
    numbers = []
    for dj in [-1, 0, 1]:
        for di in [-1, 0, 1]:
            if di == 0 and dj == 0: #Skip center
                continue
            ni, nj = i + di, j + dj
            if 0 <= ni < x_lim and 0 <= nj < y_lim and grid[nj][ni].isdigit():
                numbers.append((nj, ni))
    
    for coord in numbers:
        part = ''
        y, x = coord[0], coord[1]
        for nx in range(x, x_lim):
            if not grid[y][nx].isdigit():
                break
            else:
                part += grid[y][nx]

        if x - 1 > 0:
            for nx in range(x - 1, -1, -1): #backwards case
                if not grid[y][nx].isdigit():
                    break
                else:
                    part = grid[y][nx] + part
        
        parts.add(int(part))
    
    return list(parts)

get_parts(3, 1, x_lim, y_lim, grid)
get_parts(5, 8,x_lim, y_lim, grid)

part_two = 0
j = 0
while j < y_lim:
    i = 0
    while i < x_lim:
        if grid[j][i] == "*":
            parts = get_parts(i, j, x_lim, y_lim, grid)
            if len(parts) == 2:
                part_two += parts[0] * parts[1]
        i += 1
    j += 1

print(f"Part two: {part_two}")