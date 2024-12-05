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

#%% Function to detect cycles
from collections import defaultdict

def find_cycle(pairs):
    graph = defaultdict(list)
    visited = set()
    stack = []
    in_stack = set()

    # Build the graph
    for a, b in pairs:
        graph[a].append(b)

    def visit(node):
        if node in in_stack:  # Cycle detected
            return stack[stack.index(node):]  # Return the cycle
        if node in visited:  # Already processed
            return None

        visited.add(node)
        stack.append(node)
        in_stack.add(node)
        for neighbor in graph[node]:
            cycle = visit(neighbor)
            if cycle:
                return cycle
        stack.pop()
        in_stack.remove(node)
        return None

    for node in graph:
        cycle = visit(node)
        if cycle:
            return cycle
    return None

cycle = find_cycle(pairs)

# Check if there are numbers not part of the cycle
all_nodes = {a for a, b in pairs}.union({b for a, b in pairs})
cycle_set = set(cycle) if cycle else set()
non_cycle_nodes = all_nodes - cycle_set