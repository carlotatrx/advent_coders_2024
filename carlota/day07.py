#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec  9 23:44:38 2024

@author: ccorbella@giub.local
"""

with open('/scratch2/ccorbella/code/adventcode2024/carlota/day07_input.txt', 'r') as file:
    data = [line.strip().split(":") for line in file]
        
test_vals = [int(line[0]) for line in data]
equations = [[int(num) for num in line[1].split()] for line in data]

def day07(operators, test_vals=test_vals, equations=equations):
    
    true_eqns = 0

    for i in range(len(test_vals)):
        current_testval = test_vals[i]
        nums = equations[i]                        
        n_possibilities = len(equations[i])-1

        for ops in product(operators, repeat=n_possibilities): # combinatorics
            temp_result = nums[0]

            for j, symbol in enumerate(ops):
                if symbol == "+": temp_result += nums[j + 1]
                elif symbol == "*": temp_result *= nums[j + 1]
                elif symbol == '|': temp_result = int(str(temp_result) + str(nums[j + 1]))

            if temp_result == current_testval:
                true_eqns += current_testval
                break
                
    return(true_eqns)

day07(['*', '+']) # part 1
day07(['*', '+', '|']) # part 2
        
    
    
    
