# -*- coding: utf-8 -*-

import re

with open('/scratch2/ccorbella/code/adventcode2024/carlota/day03_input.txt', 'r') as file:
    data = file.read()
    
#%% part 1: find pairs of mul(int,int)

# slow
matches = re.findall(r"mul\(\d+,\d+\)", data)
result = 0

for muls in matches:
    is_match = re.search(r"mul\((\d+),(\d+)\)", muls)
    if is_match:
        a,b = map(int, is_match.groups())
        result += a*b

# fast 
matches = re.findall(r"mul\((\d+),(\d+)\)", data)
result = sum(int(a) * int(b) for a, b in matches)

print(result)

#%% part 2: enabling pairs with do() and don't()

start_pos  = [mystart.start() for mystart in re.finditer(r"mul\(\d+,\d+\)", data)]
start_do   = [mystart.start() for mystart in re.finditer(r"do\(\)", data)]
start_dont = [mystart.start() for mystart in re.finditer(r"don't\(\)", data)]

is_do = True
valid_starts = list()

for i in range(len(data)):
    if i in start_do: is_do = True
    elif i in start_dont: is_do = False
    
    if (i in start_pos) and is_do: valid_starts.append(i)

result = 0
for muls, start_pt in zip(matches, start_pos):
    if start_pt in valid_starts:
        is_match = re.search(r"mul\((\d+),(\d+)\)", muls)
        if is_match:
            a,b = map(int, is_match.groups())
            result += a*b
            
print(result)

