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
valid_list = []

for a,b in pairs:
    if a not in valid_list:
        valid_list.append(a)
    if b not in valid_list:
        valid_list.append(b)
    
    # If 'b' is before 'a', reorder
    if valid_list.index(b) < valid_list.index(a):
        valid_list.remove(b)
        valid_list.insert(valid_list.index(a) + 1, b)

result = 0
for li in lists:
    try:
        indices = [valid_list.index(num) for num in li]
        if indices == sorted(indices): # they are in the correct order
            print(True)
            result += li[int((len(li)-1)/2)]
        else:
            print(f"Sequence {li} is not valid.")
    except ValueError as e:
        print(f"Error: {e} - Sequence {li} contains elements not in valid_list.")
print(result)


#%%


def rules_valid(update,rules) -> bool:
    for r in rules:
        if r[0] in update and r[1] in update and update.index(r[0]) > update.index(r[1]):
            return False
        else:
            continue
    return True

rules = pairs
updates = lists
valid_updates = list()
middle_pages = list()
for u in updates:
    if rules_valid(u,rules):
        valid_updates.append(u)

for u in valid_updates:
    middle = int((len(u)-1)/2)
    middle_pages.append(u[middle])
print(middle_pages)
sum([int(x) for x in middle_pages])


