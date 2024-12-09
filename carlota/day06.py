with open('/scratch2/ccorbella/code/adventcode2024/carlota/day06_input.txt', 'r') as file:
    data = file.read().splitlines()
    
# populate the grid
n_rows, n_cols = len(data), len(data[0])
grid = []
for row in data:
  grid.append(["o"] + list(row) + ["o"])
  
# add "o"s at the edges (quoting Heinrich's idea @hheinzer)
grid.insert(0, ["o"] * len(grid[0]))
grid.append(["o"] * len(grid[0]))  
  
# find starting pos
for row_index, row in enumerate(grid):
    for col_index, cell in enumerate(row):
        if cell =="^":
            start_pos_x, start_pos_y = row_index, col_index
            
#%% part 1: visited cells

visited_cells = list()

x_now, y_now = start_pos_x, start_pos_y # 45, 42
directions = [(-1,0), (0,1), (1,0), (0,-1)] # up, right, down, left
direction_now = 0

while grid[x_now][y_now] != 'o':
    if (x_now, y_now) not in visited_cells:
        visited_cells.append((x_now, y_now))
       # grid[x_now][y_now]="X"
        
    dx, dy = directions[direction_now]
    x_next, y_next = x_now + dx, y_now + dy

    if grid[x_next][y_next] != "#":
        x_now, y_now = x_next, y_next # pos update
    else: # encounted a "#"
        direction_now = (direction_now + 1) % 4 # move a quarter CW
                
print(len(visited_cells))

#%% part 2
from copy import deepcopy

num_loops = 0

for cell in visited_cells[1:]:          # starting cell doesn't count bc guard is there now
    gridcopy = deepcopy(grid)           # deepcopy so as not to modify original grid as well
    gridcopy[cell[0]][cell[1]] = "#"    # try putting an object there
    
    # reset direction and num of steps
    x_now, y_now = start_pos_x, start_pos_y # 45, 42 or 46, 43 with edges
    steps = 0
    direction_now = 0
    
    while gridcopy[x_now][y_now] != 'o' and steps < 6000: # use 6000 as threshold value
            
        dx, dy = directions[direction_now]
        x_next, y_next = x_now + dx, y_now + dy

        if gridcopy[x_next][y_next] != "#":
            x_now, y_now = x_next, y_next # pos update
        else: # encounted a "#"
            direction_now = (direction_now + 1) % 4 # move a quarter CW
            
        steps += 1
    
    if steps == 6000: num_loops += 1 # the guard is stuck in a loop

print(num_loops)

#%%
import numpy as np
np.savetxt('/scratch2/ccorbella/code/adventcode2024/carlota/day06_visited.txt', grid, fmt='%s')  
    