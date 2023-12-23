#AOC 2023 Day 9 
'''Predicting future values based on readings from the Oasis and Sand Instability Sensor'''
#Works for the test case, not fast enough for the actual input. Requires optimization =((((((
'''I tried optimizing calculations using numpy but that didn't work. Answer attribution: 
https://github.com/Domyy95/Challenges/blob/master/2023-12-Advent-of-code/9.py'''

from line_profiler import LineProfiler
import numpy as np 

file_path = './d9/aoc_d9_input.txt'
test_file_path = './d9/aoc_d9_test_input.txt'

def zero_out_list(data):
    
    lists = [data]
    list_sum = 100
    i = 0

    while list_sum != 0:
        l1 = lists[i][: -1]
        l2 = lists[i][1 : ]

        delta = [second - first for first, second in zip(l1, l2)]
        lists.append(delta)
    
        list_val = np.sum(delta)
        list_val = sum(delta)
        
        if list_val < list_sum:
            list_sum = list_val
        
        i += 1
    
    return lists

def zero_out_array(data):
    
    lists = [np.array(data)]
    list_sum = np.sum(data)

    while list_sum != 0:
        delta = np.diff(data)
        list_val = np.sum(delta)
        lists.append(delta)
        data = delta

        if list_val < list_sum:
            list_sum = list_val

    return lists 

def extrapolate(list_of_lists):

    num_lists = len(list_of_lists)
    num_sum = 0
    for i in range(num_lists, 1, -1):
        val = list_of_lists[i - 2][-1]
        num_sum += val
    
    return num_sum

def extrap_arrays(list_of_arrays):
    overall_len = len(list_of_arrays)
    num_sum = 0 
    for arr in list_of_arrays:
        num_sum += arr[-1]
    
    return num_sum

def get_next_val(data):
    if all(n == 0 for n in data):
        return 0
    else:
        diff = [data[i + 1] - data[i] for i in range(len(data) - 1)]
        return data[-1] + get_next_val(diff)

def get_prev_val(data):
    if all(n == 0 for n in data):
        return 0
    else:
        diff = [data[i + 1] - data[i] for i in range(len(data) - 1)]
        return data[0] - get_prev_val(diff)

data = []
with open(file_path, 'r') as file:

    for line in file:
        line = line.strip().split()
        val = [int(i) for i in line]
        data.append(val)

file.close()

def part_one(data): 

    extrap_sum = 0
    for readings in data: 
        list_of_arrs = zero_out_array(readings)
        extrap = extrap_arrays(list_of_arrs)
        extrap_sum += extrap
    
    return extrap_sum

def part_one_alt(data):
    result1 = 0
    for readings in data: 
        result1 += get_next_val(readings)
    
    return result1

def part_two(data):
    result2 = 0
    for readings in data:
        result2 += get_prev_val(readings)
    
    return result2



print(f'Part 1 answer: {part_one_alt(data)}')
print(f'Part 2 answer: {part_two(data)}')