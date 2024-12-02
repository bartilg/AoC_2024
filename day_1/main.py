def read_input(path):
    # Initialize lists
    left_col = []
    right_col = []

    # Read the file and process each line
    with open(path, "r") as file:
        for line in file:
            # Split the line into columns (assuming columns are separated by spaces or tabs)
            columns = line.split()
            if len(columns) >= 2:  # Check if there are at least two columns
                left_col.append(int(columns[0]))
                right_col.append(int(columns[1]))
    return left_col, right_col
    

def part_1():
    file_path='input.txt'
    left_col, right_col = read_input(file_path)
    left_col = sorted(left_col)
    right_col = sorted(right_col)

    dist = 0
    
    for i in range(0, len(left_col)):
        dist += abs(right_col[i] - left_col[i])
    print(dist)

def part_2():
    file_path='input.txt'
    left_col, right_col = read_input(file_path)
    left_col = sorted(left_col)
    right_col = sorted(right_col)

    left_unique = list(set(left_col))
    score = 0

    for val in left_unique:
        score += right_col.count(val) * val
    print(score)

part_1()
part_2()
