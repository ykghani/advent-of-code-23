#AOC 2023 Day 6 (SOLVED)
'''Goal: figure out the number of ways you can win the boat race and multiply all of the results together'''

margin_of_error = 1

file_name = 'aoc_d6_input.txt'

def calc_margin(target_dist, race_time):
    counter = 0
    v0 = 0

    for button_time in range(1, race_time):

        v = button_time
        time_left = race_time - button_time

        dist = v * time_left

        if dist > target_dist:
            counter += 1
    
    return counter

with open(file_name, 'r') as file: 
            
    times_str = file.readline()
    dst_str = file.readline()

    times_str = times_str.strip()
    line = times_str.split(":")
    time_str = line[1].strip()
    times = time_str.split()
    times = [int(i) for i in times]

    dst_str = dst_str.strip()
    line = dst_str.split(":")
    dst_str = line[1].strip()
    distances = dst_str.split()
    distances = [int(i) for i in distances]

file.close()

def part_one(times, distances):
    margin_of_error = 1
    for i in range(len(times)):
        margin_of_error *= calc_margin(distances[i], times[i])
    
    return margin_of_error

def part_two(times, distances):
    times = [str(i) for i in times]
    distances = [str(i) for i in distances]

    time = ''.join(times)
    distance = ''.join(distances)

    return calc_margin(int(distance), int(time))

print(f'The margin of error in part 1 is: {part_one(times, distances)}')
print(f'The margin or error in part 2 is: {part_two(times, distances)}')