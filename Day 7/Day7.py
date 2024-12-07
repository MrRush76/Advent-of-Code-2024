with open("input.txt", "r") as f:
  data = f.read().split("\n")
  for i in range(len(data)):
    data[i] = data[i].split(":")
    data[i][1] = list(filter(None, data[i][1].split(" ")))

def evaluate(numbers, current=None, expression="", results=None):
  if results is None:
    results = []

  if not numbers:
    results.append(current)
    return results

  next_num = numbers[0]
  remaining_numbers = numbers[1:]

  results = evaluate(remaining_numbers, current + next_num, f"{expression} + {next_num}", results)
  results = evaluate(remaining_numbers, current * next_num, f"{expression} * {next_num}", results)
  # uncomment the following lines for part 2 
  # concatenated_num = int(f"{current}{next_num}")
  # results = evaluate(remaining_numbers, concatenated_num, f"{expression} concatenated with {next_num}", results)

  return results

def check(data):
  add_vals = []
  for i in range(len(data)):
    nums = data[i][1]
    nums = list(map(int, nums))
    results = evaluate(nums[1:], int(nums[0]), "1")
    if int(data[i][0]) in results:
      add_vals.append(data[i][0])
  print(f"Total is: {sum(map(int, add_vals))}")

check(data)
