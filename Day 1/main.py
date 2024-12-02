def find_diff(left, right):
    left.sort()
    right.sort()
    total = 0
    for i in range(len(left)):
        diff = right[i] - left[i]
        if diff < 0:
            diff *= -1
        total += diff
    return total


def find_sim(left, right):
    sim_rating = 0
    for i in range(len(left)):
        c = right.count(left[i])
        sim_rating += left[i] * c
    return sim_rating


left = []
right = []
with open("input.txt", "r") as file:
    for line in file:
        data = list(map(int, line.strip().split()))
        if len(data) != 2:
            continue
        left.append(data[0])
        right.append(data[1])

print(f'Diff: {find_diff(left, right)}')
print(f'Sim: {find_sim(left, right)}')


