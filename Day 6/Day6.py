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

map = [line.strip().split() for line in lines]
map = [[char for char in word] for sublist in map for word in sublist]
print(map)
print("\n")

for i in range(len(map)):
  if '^' in map[i]:
    pos = (i, map[i].index('^'))

direction = 'N'
out_of_map = False

while not out_of_map:
  if direction == 'N':
    if pos[0] - 1 >= 0:
      if map[pos[0] - 1][pos[1]] == '#':
        direction = 'E'
      else:
        map[pos[0]][pos[1]] = 'X'
        pos = (pos[0] - 1, pos[1])
        map[pos[0]][pos[1]] = '^'
    else:
      map[pos[0]][pos[1]] = 'X'
      out_of_map = True
  elif direction == 'S':
    if pos[0] + 1 < len(map):
      if map[pos[0] + 1][pos[1]] == '#':
        direction = 'W'
      else:
        map[pos[0]][pos[1]] = 'X'
        pos = (pos[0] + 1, pos[1])
        map[pos[0]][pos[1]] = 'v'
    else:
      map[pos[0]][pos[1]] = 'X'
      out_of_map = True
  elif direction == 'W':
    if pos[1] - 1 >= 0:
      if map[pos[0]][pos[1] - 1] == '#':
        direction = 'N'
      else:
        map[pos[0]][pos[1]] = 'X'
        pos = (pos[0], pos[1] - 1)
        map[pos[0]][pos[1]] = '<'
    else:
      map[pos[0]][pos[1]] = 'X'
      out_of_map = True
  elif direction == 'E':
    if pos[1] + 1 < len(map[0]):
      if map[pos[0]][pos[1] + 1] == '#':
        direction = 'S'
      else:
        map[pos[0]][pos[1]] = 'X'
        pos = (pos[0], pos[1] + 1)
        map[pos[0]][pos[1]] = '>'
    else:
      map[pos[0]][pos[1]] = 'X'
      out_of_map = True

x_count = 0
for i in range(len(map)):
  for j in range(len(map[i])):
    if map[i][j] == 'X':
      x_count += 1

print(f"Part 1 : {x_count}")
