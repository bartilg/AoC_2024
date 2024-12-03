def read_file(file_path):
    matrix = []
    with open(file_path, 'r') as file:
        for line in file:
            # Split the line by whitespace and convert each item to an integer
            row = list(map(int, line.split()))
            matrix.append(row)
    return matrix

def is_row_safe(row):
    prev = row[1] - row[0]
    if prev == 0 or not -3 <= prev <= 3:
        return False
    for j in range(1, len(row) - 1):
        cur = row[j + 1] - row[j]
        if prev < 0 and not -3 <= cur < 0:
            return False
        if prev > 0 and not 0 < cur <= 3:
            return False
        prev = cur
    return True

def is_row_safe_exclude(row):
    if is_row_safe(row):
        return True
    for j in range(len(row)):
        new_row = row[:j] + row[j+1:]
        if is_row_safe(new_row):
            return True
    return False

def part_2():
    file_path = 'input.txt'
    mat = read_file(file_path)

    safe = sum(is_row_safe_exclude(row) for row in mat)
    print(safe)


def part_1():
    file_path = 'input.txt'
    mat = read_file(file_path)

    safe = sum(is_row_safe(row) for row in mat)
    print(safe)

part_1()
part_2()
