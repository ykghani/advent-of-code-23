'''Advent of Code 2023 Day 5 - If you give a seed a fertilizer'''
from pathlib import Path

script_dir = Path(__file__).parent
file_path = script_dir / 'd5_test.txt'

with open(file_path, 'r') as f:
    seeds = f.readline().strip()
    
    for line in f: 
        pass 

print(seeds)
print(inp)
