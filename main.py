
def number_in_row(grid, row, number):
    if number in grid[row]:
        return True
    return False

def number_in_column(grid, column, number):
    for row in grid:
        if number == row[column]:
            return True
    return False

def number_in_box(grid, box_start, number):
    for i in range(3):
        if number in grid[i + box_start[0]][box_start[1]:box_start[1] + 3]:
            return True         
    return False

def find_empty_cell(grid):
    for row in range(len(grid)):
        for column in range(len(grid)):
            if grid[row][column] == 0:
                return row, column

def is_valid_placement(grid, row, column, number):
    box_start_row = (row // 3) * 3
    box_start_column = (column // 3) * 3
    if (number_in_row(grid, row, number)
            or number_in_column(grid, column, number)
            or number_in_box(grid, (box_start_row, box_start_column), number)):
        return False
    else:
        return True

def solve(grid):
    position = find_empty_cell(grid)
    if position is None:
        return True
    row, column = position
    for number in range(1, 10):
        if is_valid_placement(grid, row, column, number):
            grid[row][column] = number
            if solve(grid):
                return True
            grid[row][column] = 0
    return False



grid = [
    [8, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 3, 6, 0, 0, 0, 0],
    [0, 7, 0, 0, 9, 0, 2, 0, 0],
    [0, 5, 0, 0, 0, 7, 0, 0, 0],
    [0, 0, 0, 0, 4, 5, 7, 0, 0],
    [0, 0, 0, 1, 0, 0, 0, 0, 3],
    [0, 0, 1, 0, 0, 0, 0, 6, 8],
    [0, 0, 8, 5, 0, 0, 0, 1, 0],
    [0, 9, 0, 0, 0, 0, 4, 0, 0]
]
solve(grid)
for row in grid:
    print(row)


