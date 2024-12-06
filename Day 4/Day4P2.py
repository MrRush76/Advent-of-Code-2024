with open('input.txt') as f:
    lines = [line.strip() for line in f.readlines()]
    lines = [list(line) for line in lines]
    print(lines[0])

def mas_check(lines):
    mas_count = 0 
    for i in range(len(lines)):
        for j in range(len(lines[i])):
            if lines[i][j] == 'A':
                try:
                    if (lines[i+1][j+1] == 'S' and lines[i-1][j-1] == 'M') or (lines[i+1][j+1] == 'M' and lines[i-1][j-1] == 'S'):
                        if (lines[i+1][j-1] == 'M' and lines[i-1][j+1] == 'S') or (lines[i+1][j-1] == 'S' and lines[i-1][j+1] == 'M'):
                            mas_count += 1
                except IndexError:
                    continue
    return mas_count
print(mas_check(lines))