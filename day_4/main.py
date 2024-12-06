def parse_text(file_path):
    with open(file_path) as file:
        grid = [list(line.strip()) for line in file.readlines() if line.strip()]
    
    horizontal = grid
    vertical = [''.join(grid[row][col] for row in range(len(grid))) for col in range(len(grid[0]))]
    diagonals_lr = [
        ''.join(grid[r][c] for r in range(len(grid)) for c in range(len(grid[0])) if r - c == d)
        for d in range(-(len(grid) - 1), len(grid[0]))
    ]
    diagonals_rl = [
        ''.join(grid[r][c] for r in range(len(grid)) for c in range(len(grid[0])) if r + c == d)
        for d in range(len(grid) + len(grid[0]) - 1)
    ]
    
    return horizontal, vertical, diagonals_lr, diagonals_rl

def count_xmas_in_line(line):
    count = 0
    # Forward search
    count += line.count('XMAS')
    # Backward search
    count += line.count('SAMX')
    return count

def part_1():
    horizontal, vertical, diagonals_lr, diagonals_rl = parse_text('input.txt')
    
    total_count = 0
    
    # Check horizontal lines (both forward and backward)
    for line in horizontal:
        line = ''.join(line)
        total_count += count_xmas_in_line(line)
    
    # Check vertical lines (both forward and backward)
    for line in vertical:
        total_count += count_xmas_in_line(line)
    
    # Check diagonal lines (both forward and backward)
    for line in diagonals_lr + diagonals_rl:
        total_count += count_xmas_in_line(line)
    
    print(total_count)

def check_diagonal(grid, row, col, dr, dc):
    # Get 3 characters in the diagonal direction
    chars = []
    for i in range(3):
        r, c = row + dr * i, col + dc * i
        if 0 <= r < len(grid) and 0 <= c < len(grid[0]):
            chars.append(grid[r][c])
        else:
            return False
    diagonal = ''.join(chars)
    return diagonal in ['MAS', 'SAM']

def find_x_mas(grid):
    count = 0
    rows, cols = len(grid), len(grid[0])
    
    # For each potential center point
    for row in range(1, rows - 1):  # Need space for diagonals
        for col in range(1, cols - 1):  # Need space for diagonals
            # Check upper-left to lower-right diagonal
            ul_lr = check_diagonal(grid, row-1, col-1, 1, 1)
            # Check upper-right to lower-left diagonal
            ur_ll = check_diagonal(grid, row-1, col+1, 1, -1)
            
            if ul_lr and ur_ll:
                count += 1
    
    return count

def part_2():
    with open('input.txt') as file:
        grid = [list(line.strip()) for line in file.readlines() if line.strip()]
    
    result = find_x_mas(grid)
    print(f"Number of X-MAS patterns: {result}")
    
part_1()
part_2()