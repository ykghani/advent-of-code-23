#AOC 2023 Day 11 - Cosmic Expansion 
#Part 1 SOLVED, part 2 is meh

file_path = './d11/d11_input.txt'
test_file_path = './d11/d11_test_input.txt'

EXPANSION_FACTOR = 1000000

grid = []
with open(test_file_path, 'r') as file: 
    for line in file:
        grid.append(line.strip())
        if '#' not in line:
            grid.append('.' * len(grid[0]))
        
    i = 0
    while i < len(grid[0]):
        if '#' not in [line[i] for line in grid]:
            for j in range(len(grid)):
                grid[j] = grid[j][: i] + '.' + grid[j][i :]
            i += 1
        i += 1


file.close()

#Doesn't really work 
def part_two(file_path):
    with open(file_path, 'r') as file: 
        for line in file: 
            grid = [(x, y) if c == '#' else None for x, c in enumerate(line.strip()) for y, line in enumerate(file)]
            empty_lines = 0
            for y, line in enumerate(grid):
                if len(set(line)) > 1: 
                    grid[y] = [(n[0], n[1] + (EXPANSION_FACTOR - 1) * empty_lines) if n is not None else None for n in line]
                else:
                    empty_lines += 1
            
            empty_lines = 0
            for x in range(len(grid[0])):
                line = [grid[y][x] for y in range(len(grid))]
                if len(set(line)) > 1: 
                    for y in range(len(grid)):
                        grid[y][x] = (grid[y][x][0] + empty_lines * (EXPANSION_FACTOR - 1), grid[y][x][1] if grid[y][x] is not None else None) 

                else:
                    empty_lines += 1
    
    file.close()
    return grid

def number_galaxies(grid):
    gal_coords = dict()
    height = len(grid)
    width = len(grid[0])

    counter = 1
    for i in range(height):
        row = list(grid[i])
        for j in range(width):
            if row[j] == '#':
                row[j] = str(counter)
                gal_coords[str(counter)] = (i, j)
                counter += 1
            
            grid[i] = ''.join(row)
    
    return (grid, counter, gal_coords) 

def gen_pairs(max_gal):
    pairs = []
    numbers = list(range(1, max_gal))
    for x in numbers:
        for y in numbers:
            if x != y and (y, x) not in pairs:
                pairs.append((x, y))
    
    return pairs 

def calc_distance(gal1, gal2):

    gal1_coords, gal2_coords = gal_coords[str(gal1)], gal_coords[str(gal2)]
    x1, y1, x2, y2 = gal1_coords[0], gal1_coords[1], gal2_coords[0], gal2_coords[1]

    distance = abs(x1 - x2) + abs(y1 - y2)

    return distance

def calc_total_dist(gal_pairs):
    total_dist = 0
    for pair in gal_pairs:
        dist = calc_distance(pair[0], pair[1])
        total_dist += dist
    
    return total_dist

grid = part_two(file_path)
new_grid, max_gal, gal_coords = number_galaxies(grid)
gal_pairs = gen_pairs(max_gal)
total_dist = calc_total_dist(gal_pairs)

print(f'Part 1 answer: {total_dist}')