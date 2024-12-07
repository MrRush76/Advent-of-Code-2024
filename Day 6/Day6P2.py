def direction_checker(n):
  if n == '^':
    return 'N'
  elif n == 'v':
    return 'S'
  elif n == '<':
    return 'W'
  elif n == '>':
    return 'E'

with open('input.txt', 'r') as file:
  lines = file.readlines()

grid = [line.strip().split() for line in lines]
grid = [[char for char in word] for sublist in grid for word in sublist]

pos = None
for i in range(len(grid)):
  if '^' in grid[i]:
    pos = (i, grid[i].index('^'))
    break

if pos is None:
  raise ValueError("Starting position '^' not found in the grid")

original_pos = pos

original_g   = grid
direction = 'N'
out_of_map = False

while not out_of_map:
  if direction == 'N':
    if pos[0] - 1 >= 0:
      if grid[pos[0] - 1][pos[1]] == '#':
        direction = 'E'
      else:
        grid[pos[0]][pos[1]] = 'X'
        pos = (pos[0] - 1, pos[1])
        grid[pos[0]][pos[1]] = '^'
    else:
      grid[pos[0]][pos[1]] = 'X'
      out_of_map = True
  elif direction == 'S':
    if pos[0] + 1 < len(grid):
      if grid[pos[0] + 1][pos[1]] == '#':
        direction = 'W'
      else:
        grid[pos[0]][pos[1]] = 'X'
        pos = (pos[0] + 1, pos[1])
        grid[pos[0]][pos[1]] = 'v'
    else:
      grid[pos[0]][pos[1]] = 'X'
      out_of_map = True
  elif direction == 'W':
    if pos[1] - 1 >= 0:
      if grid[pos[0]][pos[1] - 1] == '#':
        direction = 'N'
      else:
        grid[pos[0]][pos[1]] = 'X'
        pos = (pos[0], pos[1] - 1)
        grid[pos[0]][pos[1]] = '<'
    else:
      grid[pos[0]][pos[1]] = 'X'
      out_of_map = True
  elif direction == 'E':
    if pos[1] + 1 < len(grid[0]):
      if grid[pos[0]][pos[1] + 1] == '#':
        direction = 'S'
      else:
        grid[pos[0]][pos[1]] = 'X'
        pos = (pos[0], pos[1] + 1)
        grid[pos[0]][pos[1]] = '>'
    else:
      grid[pos[0]][pos[1]] = 'X'
      out_of_map = True


def cycle_detector(grid, pos, direction):
  path = set()
  out_of_map = False
  while not out_of_map:
    if (pos[0], pos[1], direction) in path:
      return True
    path.add((pos[0], pos[1], direction))
    
    if direction == 'N':
      if pos[0] - 1 >= 0:
        if grid[pos[0] - 1][pos[1]] == '#':
          direction = 'E'
        else:
          grid[pos[0]][pos[1]] = 'X'
          pos = (pos[0] - 1, pos[1])
          grid[pos[0]][pos[1]] = '^'
      else:
        grid[pos[0]][pos[1]] = 'X'
        out_of_map = True
    elif direction == 'S':
      if pos[0] + 1 < len(grid):
        if grid[pos[0] + 1][pos[1]] == '#':
          direction = 'W'
        else:
          grid[pos[0]][pos[1]] = 'X'
          pos = (pos[0] + 1, pos[1])
          grid[pos[0]][pos[1]] = 'v'
      else:
        grid[pos[0]][pos[1]] = 'X'
        out_of_map = True
    elif direction == 'W':
      if pos[1] - 1 >= 0:
        if grid[pos[0]][pos[1] - 1] == '#':
          direction = 'N'
        else:
          grid[pos[0]][pos[1]] = 'X'
          pos = (pos[0], pos[1] - 1)
          grid[pos[0]][pos[1]] = '<'
      else:
        grid[pos[0]][pos[1]] = 'X'
        out_of_map = True
    elif direction == 'E':
      if pos[1] + 1 < len(grid[0]):
        if grid[pos[0]][pos[1] + 1] == '#':
          direction = 'S'
        else:
          grid[pos[0]][pos[1]] = 'X'
          pos = (pos[0], pos[1] + 1)
          grid[pos[0]][pos[1]] = '>'
      else:
        grid[pos[0]][pos[1]] = 'X'
        out_of_map = True
  return False


cycles = 0
for i in range(len(grid)):
  for j in range(len(grid[i])):
    if grid[i][j] == 'X':
      import copy
      grid_tmp = copy.deepcopy(grid)
      grid_tmp[i][j] = '#'
      grid_tmp[original_pos[0]][original_pos[1]] = '^'
      if cycle_detector(grid_tmp, (original_pos[0],original_pos[1]), 'N'):
        cycles += 1

print(cycles)
