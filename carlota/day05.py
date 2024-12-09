pairs, lists = [], []

with open('/scratch2/ccorbella/code/adventcode2024/carlota/day05_input.txt', 'r') as file:
  for line in file:
      line = line.strip()
      if "|" in line:
          a,b = map(int, line.split("|"))
          pairs.append([a,b])
    
      elif "," in line:
          nums = list(map(int, line.split(",")))
          lists.append(nums)


#%% part 1

valid_lists = list()
invalid_lists = list()

for li in lists:
    li_ordered = True
    
    for pair in pairs:
        # check if any num in the pairs is in the list
        a, b = pair[0], pair[1]
        if a in li and b in li:
            # if there is only one of the two in the list we don't care
            if li.index(a) > li.index(b): # they are  NOT in the correct order
                li_ordered = False
                break
    if li_ordered:
        valid_lists.append(li)
    else:
        invalid_lists.append(li)
    
result = 0
for li in valid_lists:
    result += li[int((len(li)-1)/2)]

print(result)

#%%
result2 = 0

for li in invalid_lists:
    for pair in pairs:
        a, b = pair[0], pair[1]
        if a in li and b in li:
            if li.index(a) > li.index(b):
                li[li.index(a)] = b
                li[li.index(b)] = a
    result2 += li[int((len(li)-1)/2)]




