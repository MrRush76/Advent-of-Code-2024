import re 

def mul(x,y):
    return x*y


def total(line):
  line = re.findall("mul\(\s*\d+\s*,\s*\d+\s*\)", line)
  total = 0
  for i in range(len(line)):
      total += eval(line[i])
  return total

input_total = 0
with open("input.txt") as f:
  input = f.read()
  input = "".join(input.splitlines())
  broken = input.split("don't")
  input_total += total(broken[0])
  x = re.findall("mul\(\s*\d+\s*,\s*\d+\s*\)", input)
  for i in broken[1:]:
    tmp = i.split("do()")
    tmp = "".join(tmp[1:])
    input_total += total(tmp)
  
  # Extract the numbers from the found mul function calls

# Initialize total to accumulate the results
total = 0

# Process each pair of numbers
for i in range(len(x)):
    total += eval(x[i])

# Print the final total
print(input_total)