with open('input.txt') as f:
    lines = [line.strip() for line in f.readlines()]
    lines = [list(line) for line in lines]
    print(lines)

def mas_check(lines):
    m_indexes_l = []
    m_indexes_r = []
    mas_count = 0 
    for i in range(len(lines)):
        for j in range(len(lines[i])):
            if j + 2 < len(lines[i]) and i + 2 < len(lines) and lines[i][j] == "M" and lines[i+1][j+1] == "A" and lines[i+1][j+2] == "S":
                m_indexes_r.append((i, j))
            if j - 2 >= 0 and i + 2 < len(lines) and lines[i][j] == "M" and lines[i+1][j-1] == "A" and lines[i+1][j-2] == "S":
                m_indexes_l.append((i, j))
    for i in range(len(m_indexes_l)):
        print(m_indexes_l[i][0], m_indexes_l[i][1] + 2)
        if (m_indexes_l[i][0], m_indexes_l[i][1] + 2) in m_indexes_r:
            mas_count += 1
    return mas_count
      

print(mas_check(lines))