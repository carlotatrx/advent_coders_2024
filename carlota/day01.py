# -*- coding: utf-8 -*-

import numpy as np
data = np.loadtxt('/scratch2/ccorbella/code/adventcode2024/carlota/day01_input.txt',
                  dtype=int)

#%% part 1
a1 = np.sort(data[:,0])
a2 = np.sort(data[:,1])

result = np.sum(abs(a1 - a2))

#%% part 2: similarity score
a1 = data[:,0]
a2 = data[:,1]

result = 0
for num in a1:
    count = len(np.where(num==a2)[0])
    result += count * num