with open("input.txt", "r") as file:
  # Splits the list into two lists at the index where only a new line is present
  data = file.read()
  parts = data.split("\n\n")
  # Makes parts[0] into a list of strings
  parts[0] = parts[0].split("\n")
  for i in range(len(parts[0])):
    parts[0][i] = parts[0][i].split("|")
  parts[1] = parts[1].split("\n")
  for i in range(len(parts[1])):
    parts[1][i] = parts[1][i].split(",")


def rule_checker(n, rules):
  for i in range(len(n)):
    for j in range(len(rules)):
      if n[i] in rules[j]:
        first_arg = rules[j][0]
        second_arg = rules[j][1]
        if first_arg in n and second_arg in n:
          if n.index(first_arg) < n.index(second_arg):
            continue
          else:
            return False
  return True


def rule_checker2(n, rules):
  n_changed = False
  for i in range(len(n)):
    for j in range(len(rules)):
      if n[i] in rules[j]:
        first_arg = rules[j][0]
        second_arg = rules[j][1]
        if first_arg in n and second_arg in n:
          if n.index(first_arg) < n.index(second_arg):
            continue
          else:
            n_changed = True
            n[n.index(first_arg)], n[n.index(second_arg)] = (
              n[n.index(second_arg)],
              n[n.index(first_arg)],
            )
  for i in range(len(n)):
    for j in range(len(rules)):
      if n[i] in rules[j]:
        first_arg = rules[j][0]
        second_arg = rules[j][1]
        if first_arg in n and second_arg in n:
          if n.index(first_arg) < n.index(second_arg):
            continue
          else:
            n_changed = True
            n[n.index(first_arg)], n[n.index(second_arg)] = (
              n[n.index(second_arg)],
              n[n.index(first_arg)],
            )
  if n_changed:
    return n


middle_page_total = 0
for i in range(len(parts[1])):
  good_list = rule_checker(parts[1][i], parts[0])
  if good_list:
    middle_page_total += int(parts[1][i][len(parts[1][i]) // 2])
print(f"Part 1 answer: {middle_page_total}")

incr_middle_page_total = 0
for i in range(len(parts[1])):
  l1 = rule_checker2(parts[1][i], parts[0])
  if l1 is not None:
    incr_middle_page_total += int(l1[len(l1) // 2])
print(f"Part 2 answer: {incr_middle_page_total}")
