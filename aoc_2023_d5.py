#Advent of Code 2023 Day 5
#Works on test input BUT DOES NOT WORK FOR LARGER INPUT BECAUSE CODE IS TOO SLOW
#Ranges likely need to be optimized so that dictionaries are not completely filled out for every value 

from collections import namedtuple


file_name = 'aoc_d5_test_input.txt'

seeds = list()
mappings = {}
Values = namedtuple('data', ['dest_start', 'source_start', 'data_range'])
current_section = ''
lowest_location = 10 ** 10

with open(file_name, 'r') as file: 
    
    for line in file: 
        line = line.strip()

        if not line:
            continue

        if line.startswith('seeds:'):
            seeds = list(map(int, line.split()[1:]))
        
        elif line.startswith('seed-to-soil map:'):
            current_section = 'seed-to-soil'
            mappings[current_section] = dict()
            continue
                   
        elif line.startswith('soil-to-fertilizer map:'):
            current_section = 'soil-to-fertilizer'
            mappings[current_section] = dict()
            continue
            
        elif line.startswith('fertilizer-to-water map:'):
            current_section = 'fertilizer-to-water'
            mappings[current_section] = dict()
            continue
            
        elif line.startswith('water-to-light map:'):
            current_section = 'water-to-light'
            mappings[current_section] = dict()
            continue
            
        elif line.startswith('light-to-temperature map:'):
            current_section = 'light-to-temperature'
            mappings[current_section] = dict()
            continue
            
        elif line.startswith('temperature-to-humidity map:'):
            current_section = 'temperature-to-humidity'
            mappings[current_section] = dict()
            continue
            
        elif line.startswith('humidity-to-location map:'):
            current_section = 'humidity-to-location'
            mappings[current_section] = dict()
            continue
            

        if current_section:
            input_string = line.split()
            data = Values(dest_start= int(input_string[0]), source_start= int(input_string[1]), data_range= int(input_string[2]))        
            
            # for i in range(data.data_range):
            #     mappings[current_section][data.source_start + i] = data.dest_start + i

            mappings[current_section][data.source_start] = data.dest_start
            mappings[current_section][data.source_start + data.data_range - 1] = data.dest_start + data.data_range - 1
    
    file.close()

seed_soil_min, seed_soil_max = min(mappings['seed-to-soil'].keys())


for seed in seeds: 
    
    if seed in mappings['seed-to-soil']:
        soil = mappings['seed-to-soil'][seed]
    else:
        soil = seed
    
    if soil in mappings['soil-to-fertilizer']:
        fertilizer = mappings['soil-to-fertilizer'][soil]
    else:
        fertilizer = soil
    
    if fertilizer in mappings['fertilizer-to-water']:
        water = mappings['fertilizer-to-water'][fertilizer]
    else:
        water = fertilizer
    
    if water in mappings['water-to-light']:
        light = mappings['water-to-light'][water]
    else:
        light = water
    
    if light in mappings['light-to-temperature']:
        temperature = mappings['light-to-temperature'][light]
    else:
        temperature = light
    
    if temperature in mappings['temperature-to-humidity']:
        humidity = mappings['temperature-to-humidity'][temperature]
    else:
        humidity = temperature
    
    if humidity in mappings['humidity-to-location']:
        location = mappings['humidity-to-location'][humidity]
    else:
        location = humidity
    
    if location < lowest_location:
        lowest_location = location 
    
print(f'The lowest location value is {lowest_location}')




