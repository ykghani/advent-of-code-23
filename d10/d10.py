#AOC 2023 Day 10 - Pipe Maze

file_path = './d10/d10_input.txt'
test_file_path = './d10/d10_test1_input.txt'

grid = []
with open(test_file_path, 'r') as file: 
    for line in file: 
        line = line.strip()
        grid.append(line)

file.close()

height = len(grid)
width = len(grid[0])

def find_S(grid):
    x, y = 0, 0
    for i in range(height):
        for j in range(width):
            if grid[i][j] == 'S':
                return (i, j)
    
    return 'SOMETHING HAS GONE HORRIBLY WRONG'

#Check coordinate above and below to see which direction to go 
def vert_pipe(grid, coord): 
    x, y = *coord
    loopers = ['|', 'L', 'J', '7', 'J']

    if x == 0: 
        x += 1
        if grid[x][y] in loopers:
            return (x, y)

    elif x == height - 1: 
        x -= 1
        if grid[x][y] in loopers:
            return (x, y)

    else:
        if grid[x + 1][y] in loopers: 
            return (x + 1, y)
        elif grid[x - 1][y] in loopers:
            return (x - 1, y)
    
    return 'no_loop'


def hor_pipe(grid, coord):
    x, y = *coord
    loopers = ['-', 'L', 'J', '7', 'F']

    if y == 0:
        if grid[x][y + 1] in loopers:
            return (x, y)
    
    elif y == width - 1: 
        if grid[x][y - 1] in loopers: 
            return (x, y - 1)
    
    else:
        if grid[x][y + 1] in loopers:
            return (x, y + 1)
        elif grid[x][y - 1] in loopers:
            return (x, y - 1)
    
    return 'no_loop'
        
def L_pipe(grid, coord):
    x, y = *coord
    loopers = ['|', ]




print(find_S(grid))
