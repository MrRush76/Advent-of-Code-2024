def inc_or_dec(lst1):
  if not lst1:
    return False
  lst1_srt = sorted(lst1)
  lst1_srt_rev = lst1_srt[::-1]
  if lst1_srt == lst1 or lst1_srt_rev == lst1:
    return True
  for i in range(len(lst1)-1):
    lst_new = lst1[:i] + lst1[i+1:]
    if lst_new == sorted(lst_new) or lst_new == sorted(lst_new, reverse=True):
      return True
  return False

def adj_lvls(lst1):
  if not lst1:
    return False
  counts = 0
  for i in range(len(lst1)-1):
    diff = abs(lst1[i+1] - lst1[i])
    if diff > 3 or diff < 1:
      counts += 1
  return counts <= 1

def main():
  with open("input.txt") as f:
    data = f.readlines()
    safe_rep = 0  
    for i in range(len(data)):
      data[i] = list(map(int, data[i].strip().split()))
    for i in range(len(data)):
      is_safe = inc_or_dec(list(data[i])) and adj_lvls(list(data[i]))
      print(is_safe)
      if is_safe:
        safe_rep = safe_rep + 1
        print(f"Number of safe reports is : {safe_rep}")

main()

