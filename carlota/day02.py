# -*- coding: utf-8 -*-

import numpy as np
with open('/scratch2/ccorbella/code/adventcode2024/carlota/day02_input.txt', 'r') as file:
    data = [[int(num) for num in line.split()] for line in file]
    

    
#%% part 1, monotonic increase/ decrease

def safe_reports(line):
    if (len(np.unique(line)) != len(line)): return 0 # has equal numbers
    else:
        pos, neg, inrange = False, False, True
        for i in range(len(line)-1):
            num = line[i+1] - line[i]
            if num > 0: pos = True
            elif num < 0: neg = True
            
            if abs(num) > 3:
                inrange = False
                return 0
        if (pos and neg): return 0
        elif inrange: return 1
    
result = 0
for line in data:
    result+= safe_reports(line)
            
print(result)
            
#%% part 2
result = 0
for line in data:
    if safe_reports(line)==0:
        # try removing one number at a time
        for i in range(len(line)):
            new_line = line[:i]+line[i+1:]
            if safe_reports(new_line)==1:
                result+=1
                break
    else: result += 1
    
print(result)
