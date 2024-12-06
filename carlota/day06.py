with open('/scratch2/ccorbella/code/adventcode2024/carlota/day06_input.txt', 'r') as file:
    data = file.read().splitlines()
    
# populate the grid
n_rows, n_cols = len(data), len(data[0])
grid = []
for row in data:
  grid.append(list(row))
  
# find starting pos
for row_index, row in enumerate(grid):
    for col_index, cell in enumerate(row):
        if cell =="^":
            start_pos_x, start_pos_y = row_index, col_index
            
#%% part 1: visited cells

is_ingrid = True
visited_cells = list()

x_now, y_now = start_pos_x, start_pos_y # 45, 42
directions = [(-1,0), (0,1), (1,0), (0,-1)] # up, right, down, left
direction_now = 0

while is_ingrid:
    if (x_now, y_now) not in visited_cells:
        visited_cells.append((x_now, y_now))
        grid[x_now][y_now]="O"
        
    dx, dy = directions[direction_now]
    x_next, y_next = x_now + dx, y_now + dy

    if 0 <= x_next < len(grid) and 0 <= y_next < len(grid[0]) and grid[x_next][y_next] != "#":
        x_now, y_now = x_next, y_next # pos update
    else: # encounted a "#"
        direction_now = (direction_now + 1) % 4 # move a quarter CW
                
    # check boundaries of grid
    if not (0 <= x_now < len(grid) and 0 <= y_now < len(grid[0])):
        is_ingrid = False # exit if new pos not in boundaries
        
print(len(visited_cells))
    