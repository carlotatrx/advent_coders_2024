# -*- coding: utf-8 -*-

import numpy as np
with open('/scratch2/ccorbella/code/adventcode2024/carlota/day02_input.txt', 'r') as file:
    data = [[int(num) for num in line.split()] for line in file]
    

    
#%% part 1, monotonic increase/ decrease

result = 0
for line in data:
    
    if (len(np.unique(line)) != len(line)): # has equal numbers
        result += 0
    else:
        pos, neg, inrange = False, False, True
        for i in range(len(line)-1):
            num = line[i+1] - line[i]
            if num > 0: pos = True
            elif num < 0: neg = True
            
            if abs(num) > 3:
                inrange = False
                break
        if (pos and neg): result += 0
        elif inrange: result += 1
            
print(result)
            
            
            
        

