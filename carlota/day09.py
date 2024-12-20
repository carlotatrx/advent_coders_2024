#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec 11 21:16:47 2024

@author: ccorbella@giub.local
"""

with open('/scratch2/ccorbella/code/adventcode2024/carlota/day09_input.txt') as file:
    data = file.read().strip()
    
#%% updated_data

updated_data = list()
start_with = 0
for i, letter in enumerate(data):
    if i%2 != 0: # odd positions are points
        updated_data.extend(['.']*int(letter))
    else:
        updated_data.extend([start_with]*int(letter))
        start_with += 1

def checksum(data):
    result = 0
    for pos, num in enumerate(updated_data):
        if num != '.':
            result += pos*num
    return(result)
 
#%% part 1

now = 0
last = len(updated_data)-1

while now < last:
    if updated_data[now] == '.':
        while last > now and updated_data[last] == '.':
            last -= 1 # reduce positions from the back if there's no number
        if last > now:
            updated_data[now] = updated_data[last]
            updated_data[last] = '.' # to avoid repeating
    now += 1

print(checksum(updated_data))

#%% part 2
import numpy as np


last = len(updated_data)-1

# create variable of zeros and ones depending on if it's empty (0) or full with a number (1)
filled = []
for i in updated_data:
    filled.extend([1]) if isinstance(i,int) else filled.extend([0])

while last > 0 and 0 in filled[:last]:
    if updated_data[last] != '.':
        current_num = updated_data[last]
        howmany_current_num = 0
        while updated_data[last] == current_num:
            howmany_current_num += 1
            last -= 1
        # now we have how many numbers there are
        print(last, current_num, howmany_current_num, updated_data)
        for i in range(len(filled) - howmany_current_num + 1):
            if np.array_equal(filled[i:i + howmany_current_num], [0] * howmany_current_num):
                updated_data[i:i + howmany_current_num] = [current_num] * howmany_current_num # move the blocks
                filled[i:i + howmany_current_num] = [1] * howmany_current_num # mark the position as filled
                
                updated_data[last+1: last + howmany_current_num+1] = ['.'] * howmany_current_num # remove the numbers from the data
                break
            
    else: last -= 1
    
print(checksum(updated_data))
