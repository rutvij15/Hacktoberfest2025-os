import random

# Generate a random maze and solve it using DFS

WIDTH, HEIGHT = 10, 10  # You can increase for bigger mazes
START, END = (0, 0), (9, 9)

def generate_maze(width, height):
    maze = [[1 if random.random() < 0.25 else 0 for _ in range(width)] for _ in range(height)]
    maze[START[1]][START[0]] = 0
    maze[END[1]][END[0]] = 0
    return maze

def print_maze(maze, path=None):
    for y in range(len(maze)):
        for x in range(len(maze[0])):
            if path and (x, y) in path:
                print("●", end=" ")  # Path
            elif maze[y][x] == 1:
                print("█", end=" ")  # Wall
            else:
                print(" ", end=" ")  # Free space
        print()
    print()

def dfs(maze, x, y, visited=None, path=None):
    if visited is None: visited = set()
    if path is None: path = []

    if (x, y) == END:
        path.append((x, y))
        return path

    visited.add((x, y))
    path.append((x, y))

    for dx, dy in [(1,0),(0,1),(-1,0),(0,-1)]:  # Right, Down, Left, Up
        nx, ny = x + dx, y + dy
        if 0 <= nx < WIDTH and 0 <= ny < HEIGHT:
            if maze[ny][nx] == 0 and (nx, ny) not in visited:
                result = dfs(maze, nx, ny, visited, path)
                if result:
                    return result

    path.pop()
    return None

# Run program
maze = generate_maze(WIDTH, HEIGHT)
print("Original Maze:")
print_maze(maze)

solution = dfs(maze, *START)

if solution:
    print("Solved Maze:")
    print_maze(maze, solution)
else:
    print("No path found!")
