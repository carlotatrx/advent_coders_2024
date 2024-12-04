with open('day04_input.txt', 'r') as file:
  data = file.read().splitlines()

# populate the grid
n_rows, n_cols = len(data), len(data[0])
grid = []
for row in data:
  grid.append(list(row))

#%% part 1: find XMAS

directions = [
    (0,1),
    (1,0),
    (0,-1),
    (-1,0),
    (-1,-1),
    (1,1),
    (1,-1),
    (-1,1)
]
count = 0

# iterate through the grid
for j in range(n_cols):
  for i in range(n_rows):
    if grid[i][j] == 'X': # if there's not an X there it's not worth looking around
      for drow, dcol in directions:
        is_match = True # True by default

        for char in range(len("XMAS")):
          new_row, new_col = i + drow * char, j + dcol * char

          # don't go out of bounds ( beq / leq bc python starts at 0 )
          if new_row < 0 or new_row >= n_rows or new_col < 0 or new_col >= n_cols or grid[new_row][new_col] != "XMAS"[char]:
            is_match = False
            break # break iteration through word "XMAS" loop
        
        if is_match: # the loop through the word didn't break
          count += 1

print(count)

#%% part 2: find X-MAS

count = 0

for j in range(1, n_cols-1):
  for i in range(1, n_rows-1):
    if grid[i][j] == "A":
      # only four options, iterate through each
      diag_1 = grid[i - 1][j - 1] + grid[i + 1][j + 1]
      diag_2 = grid[i + 1][j - 1] + grid[i - 1][j + 1]

      if ((diag_1 == "SM" or diag_1 == "MS") and (diag_2 == "SM" or diag_2 == "MS")): count += 1

print(count)

