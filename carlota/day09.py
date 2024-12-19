#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec 11 21:16:47 2024

@author: ccorbella@giub.local
"""

with open('/scratch2/ccorbella/code/adventcode2024/carlota/day09_input.txt') as file:
    data = file.read().strip()
    
#%%

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

#%%
str_data = str()
start_with = 0
for i, letter in enumerate(data):
    if i%2 != 0: # odd positions are points
        str_data += '.'*int(letter)
    else:
        str_data += str(start_with)*int(letter)
        start_with += 1
        
with open('/scratch2/ccorbella/code/adventcode2024/carlota/day09_str.txt', 'w') as file:
    file.write(str_data)

# new_data = str_data.copy()

pos_now = 0
end_pos = -1
while(str_data):
    if str_data[pos_now] == '.':
        while(str_data[end_pos] == '.'):
            end_pos -= 1
        
        str_data[pos_now] = str_data[end_pos]
        str_data = str_data[:-1]
        
with open('/scratch2/ccorbella/code/adventcode2024/carlota/day09_strfinal.txt', 'w') as file:
    file.write(str_data)