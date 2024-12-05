with open("input.txt") as f:
  lines = f.readlines()
  lines = [x.strip() for x in lines]

def horizontal_check(lines):
  xmas_count = 0 
  for i in range(len(lines)):
    for j in range(len(lines[i])):
      if lines[i][j] == "X":
        if j + 3 < len(lines[i]) and lines[i][j+1] == "M" and lines[i][j+2] == "A" and lines[i][j+3] == "S":
          xmas_count += 1
        if j - 3 >= 0 and lines[i][j-1] == "M" and lines[i][j-2] == "A" and lines[i][j-3] == "S":
          xmas_count += 1
  print(f"Horizontal check count: {xmas_count}")
  return xmas_count

def vertical_check(lines):
  xmas_count = 0
  for i in range(len(lines)):
    for j in range(len(lines[i])):
      if lines[i][j] == "X":
        if i + 3 < len(lines) and lines[i+1][j] == "M" and lines[i+2][j] == "A" and lines[i+3][j] == "S":
          xmas_count += 1
        if i - 3 >= 0 and lines[i-1][j] == "M" and lines[i-2][j] == "A" and lines[i-3][j] == "S":
          xmas_count += 1
  print(f"Vertical check count: {xmas_count}")
  return xmas_count

def diagonal_check(lines):
  xmas_count = 0 
  for i in range(len(lines)):
    for j in range(len(lines[i])):
      if lines[i][j] == "X":
        if i + 3 < len(lines) and j + 3 < len(lines[i]):
          if lines[i+1][j+1] == "M" and lines[i+2][j+2] == "A" and lines[i+3][j+3] == "S":
            xmas_count += 1
        if i - 3 >= 0 and j - 3 >= 0:
          if lines[i-1][j-1] == "M" and lines[i-2][j-2] == "A" and lines[i-3][j-3] == "S":
            xmas_count += 1
  print(f"Diagonal check count: {xmas_count}")
  return xmas_count

def diagonal_check2(lines):
  xmas_count = 0 
  for i in range(len(lines)):
    for j in range(len(lines[i])):
      if lines[i][j] == "X":
        if i - 3 >= 0 and j + 3 < len(lines[i]):
          if lines[i-1][j+1] == "M" and lines[i-2][j+2] == "A" and lines[i-3][j+3] == "S":
            xmas_count += 1
        if i + 3 < len(lines[i]) and j - 3 >= 0:
          if lines[i+1][j-1] == "M" and lines[i+2][j-2] == "A" and lines[i+3][j-3] == "S":
            xmas_count += 1
  print(f"Diagonal check 2 count: {xmas_count}")
  return xmas_count



xmas_count = (
    horizontal_check(lines) +
    vertical_check(lines) +
    diagonal_check(lines) +
    diagonal_check2(lines)
)
print(f"Total XMAS count: {xmas_count}")