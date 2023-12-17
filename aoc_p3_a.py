#Advent of Code 2023 - Day 3

def get_num(start_ind, row):
    num_str = row[start_ind]

    for j in range(start_ind + 1, len(row)):
        if row[j].isdigit():
            num_str += row[j]
        else:
            return (int(num_str), j - 1) #j - 1 is the index of the last digit of the number

def is_symbol(pos):
    return pos in {'@', '#', '$', '%', '&', '*', '+', '='}

def symbol_in_proximity(start_j, end_j, i, grid):
    symbol_found = False 
    #only need to check below and to the right
    for j in range(start_j, end_j + 1):
        if j == start_j:
            if j != 0:
                if is_symbol(grid[i][j - 1]):
                    symbol_found = True
                
                if i < len(grid) - 1: #case where you're not at the bottom of grid
                    if is_symbol(grid[i + 1][j]) or is_symbol(grid[i + 1][j-1]):
                        symbol_found = True
                
                if i != 0: 
                    if is_symbol(grid[i - 1][j]) or is_symbol(grid[i - 1][j - 1]):
                        symbol_found = True
            
            else: #j == 0
                if i != len(grid):
                    if is_symbol(grid[i + 1][j]): 
                        symbol_found = True

                if i != 0:
                    if is_symbol(grid[i - 1][j]):
                        symbol_found = True
        
        elif j == end_j:
            if j == len(grid[0]):
                if i != len(grid): 
                    if is_symbol(grid[i + 1][j]):
                        symbol_found = True

                if i != 0: 
                    if is_symbol(grid[i -1][j]):
                        symbol_found = True
                    
            else:
                if i < len(grid) - 1:
                    if is_symbol(grid[i + 1][j]) or is_symbol(grid[i + 1][j + 1]):
                        symbol_found = True
                    
                    if is_symbol(grid[i][j + 1]):
                        symbol_found = True
                
                if i != 0:
                    if is_symbol(grid[i - 1][j]) or is_symbol(grid[i - 1][j]):
                        symbol_found = True
                    
                    if j < len(grid[0]) - 1:
                        if is_symbol(grid[i - 1][j + 1]):
                            symbol_found = True 

        else:
            if i < len(grid) - 1:
                if is_symbol(grid[i + 1][j]):
                    symbol_found = True
            
            if i != 0:
                if is_symbol(grid[i -1][j]):
                    symbol_found = True
    
    return symbol_found


grid_sum = 0

file_name = 'd3_input.txt'

with open(file_name, 'r') as file:
    grid = file.readlines()
    grid = [line.strip() for line in grid]

    file.close()

height = len(grid) #corresponds to the i 
width = len(grid[0]) # corresponds to the j 

i,j = 0, 0
while i < height:
    j = 0
    while j < width: 
        if grid[i][j].isdigit():
            number, end_j = get_num(j, grid[i])
            if symbol_in_proximity(j, end_j, i, grid):
                grid_sum += number
                print(f'Current coord: {i}, {j}, with grid_sum              {grid_sum}')
                j = end_j + 1
            else:
                j += 1
        else:
            j += 1
    
    i += 1

print(grid_sum)