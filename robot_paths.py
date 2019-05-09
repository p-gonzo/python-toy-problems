from copy import deepcopy

def make_grid(x, y):
    return [[0 for i in range(x)] for j in range(y)]

def print_grid(grid):
    if grid is None:
        print(None)
        return
    for row in [[str(item) for item in row] for row in grid]:
        print(row)

def toggle_piece(grid, y, x, val):
        if grid[y][x] == 0:
            grid[y][x] = val
        else:
            grid[y][x] = 0

def solve_grid(grid):

    shortest_path = None

    def traverse(y, x, counter):

        # Base case 1, found solution:
        if y == len(grid) -1 and x == len(grid[0]) -1:
            grid[y][x] = counter
            nonlocal shortest_path
            if shortest_path is None:
                shortest_path = deepcopy(grid)
            elif shortest_path[-1][-1] > grid[-1][-1]:
                shortest_path = deepcopy(grid)
            grid[y][x] = 0
            return

        # Base Case 2, only continue if the counter is less than the shortest path.
        if shortest_path is not None and shortest_path[-1][-1] < counter:
            return
        
        toggle_piece(grid, y, x, counter)

        # Down:
        if y + 1 < len(grid) and grid[y + 1][x] == 0:
            traverse(y + 1, x, counter + 1)
        # Right:
        if x + 1 < len(grid[0]) and grid[y][x + 1] == 0:
            traverse(y, x + 1, counter + 1)
        # Left:
        if x - 1 >= 0 and grid[y][x - 1] == 0:
            traverse(y, x - 1, counter + 1)
        # Up:
        if y - 1 >= 0 and grid[y - 1][x] == 0:
            traverse(y - 1, x, counter + 1)

        toggle_piece(grid, y, x, counter)

    traverse(0, 0, 1)
    return shortest_path


grid =  [
    [0, 'x', 0, 0, 0],
    [0, 'x', 0, 'x', 0],
    [0, 'x', 0, 'x', 0],
    [0, 'x', 0, 0, 0],
    [0, 'x', 0, 'x', 0],
    [0, 'x', 0, 'x', 0],
    [0, 0, 0, 'x', 0],
]
print_grid(solve_grid(grid))

