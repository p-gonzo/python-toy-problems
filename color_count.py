a_grid = [
    ['g', 'g', 'g', 'g', 'b'],
    ['g', 'g', 'g', 'g', 'b'],
    ['g', 'r', 'r', 'g', 'b'],
    ['g', 'r', 'r', 'g', 'b'],
    ['g', 'r', 'b', 'b', 'b']
]

def mark_visited(grid_hash, y, x):
    grid_hash[(y, x)] = True

def have_visited(grid_hash, y, x):
    return grid_hash.get((y, x), False)

def is_in_bounds(grid, y, x):
    return y < len(grid) and y >= 0 and x < len(grid[0]) and x >= 0

def should_visit(grid, grid_hash, y, x, current_color):
    return is_in_bounds(grid, y, x) and (grid[y][x] == current_color) and not have_visited(grid_hash, y, x)

def color_count(grid):
    visited_hash = {}
    largest_so_far = {"color": None, "count": None}
    
    def traverse_colors(y, x, count_so_far=1):
        mark_visited(visited_hash, y, x)
        current_color = grid[y][x]
        if largest_so_far["count"] is None or count_so_far > largest_so_far["count"]:
            largest_so_far["color"] = current_color
            largest_so_far["count"] = count_so_far

        # If not out of bounds, same color, and not yet visited
        # Down
        if should_visit(grid, visited_hash, y + 1, x, current_color):
            count_so_far = traverse_colors(y + 1, x, count_so_far + 1)
        # Right
        if should_visit(grid, visited_hash, y, x + 1, current_color):
            count_so_far = traverse_colors(y, x + 1, count_so_far + 1)
        # Up
        if should_visit(grid, visited_hash, y - 1, x, current_color):
            count_so_far = traverse_colors(y - 1, x, count_so_far + 1)
        # Left
        if should_visit(grid, visited_hash, y, x - 1, current_color):
            count_so_far = traverse_colors(y, x - 1, count_so_far + 1)

        return count_so_far

    for y in range(len(grid)):
        for x in range(len(grid[0])):
            if not have_visited(visited_hash, y, x):
                traverse_colors(y, x)

    return largest_so_far

print(color_count(a_grid))