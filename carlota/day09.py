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

for i, letter in enumerate(data):
    if i%2 != 0: # odd positions are points
        updated_data.append('.'*i)
    else:
        updated_data.append(str(i)*i)

updated_data = updated_data[1:]

str_data = str()
for i, letter in enumerate(data):
    if i%2 != 0: # odd positions are points
        str_data += '.'*i
    else:
        str_data += str(i)*i
        
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