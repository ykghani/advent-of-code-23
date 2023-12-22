#AOC 2023 Day 8
'''Use the provided map to go left or right to get from starting point (AAA) to ending point (ZZZ)'''

from collections import namedtuple
import math 

Position = namedtuple('Position', ['left', 'right'])

test_file_path = './d8/aoc_d8_test2_input.txt'
file_path = './d8/aoc_d8_input.txt'
part2_test_file_path = './d8/aoc_d8_part2_test_input.txt'

def generate_position(line_str):
    line_str.strip()
    pos = line_str[0:3]
    open_paren_index = line_str.index('(')
    close_paren_index = line_str.index(')')

    left = line_str[open_paren_index + 1 : open_paren_index + 4]
    right = line_str[close_paren_index - 3: close_paren_index]

    return (pos, left, right)

location_map = dict()
ghost_nodes = []

#Read puzzle input 
with open(file_path, 'r') as file:
    direction_str = file.readline().strip()

    for line in file:
        
        if not line or line == '\n':
            continue

        values = generate_position(line)
        if values[0][2] == 'A':
            ghost_nodes.append(values[0])
        location_map[values[0]] = Position(left= values[1], right= values[2])

file.close()


def part_one(location_map, direction_str):
    
    current_loc = 'AAA'
    turn_count = 0
    i = 0
    
    while current_loc != 'ZZZ':
        if direction_str[i] == 'L':
            current_loc = location_map[current_loc].left
        else:
            current_loc = location_map[current_loc].right
        
        turn_count += 1

        if i == len(direction_str) - 1:
            i = 0
        else:
            i += 1
    
    return turn_count

def part_two(location_map, direction_str, ghost_nodes):
    
    current_locs = ghost_nodes
    cycles = []

    for loc in current_locs:
        current_loc = loc
        turn_count, i = 0, 0
        
        while current_loc[2] != 'Z':
            if direction_str[i] == 'L':
                current_loc = location_map[current_loc].left
            else:
                current_loc = location_map[current_loc].right
            
            turn_count += 1

            if current_loc[2] == 'Z':
                cycles.append(turn_count)
                break
            else: 
                if i == len(direction_str) - 1:
                    i = 0
                else:
                    i += 1
    
    return math.lcm(*cycles)
 

print(f'Part 1 turn count is: {part_one(location_map, direction_str)}')
print(f'Part 2 turn count is: {part_two(location_map, direction_str, ghost_nodes)}')