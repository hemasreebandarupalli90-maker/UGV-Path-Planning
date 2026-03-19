import heapq
import random

SIZE = 20  # (use 70 for full scale)
OBSTACLE_DENSITY = 0.2  # change: 0.1, 0.2, 0.3


def generate_grid():
    grid = [[0 for _ in range(SIZE)] for _ in range(SIZE)]

    for i in range(SIZE):
        for j in range(SIZE):
            if random.random() < OBSTACLE_DENSITY:
                grid[i][j] = 1  # obstacle

    return grid


def get_neighbors(x, y):
    moves = [(1,0), (-1,0), (0,1), (0,-1)]
    return [(x+dx, y+dy) for dx, dy in moves]


def dijkstra_grid(grid, start, goal):
    pq = [(0, start)]
    visited = set()
    parent = {}

    while pq:
        cost, (x, y) = heapq.heappop(pq)

        if (x, y) in visited:
            continue

        visited.add((x, y))

        if (x, y) == goal:
            break

        for nx, ny in get_neighbors(x, y):
            if 0 <= nx < SIZE and 0 <= ny < SIZE:
                if grid[nx][ny] == 0:
                    heapq.heappush(pq, (cost + 1, (nx, ny)))
                    parent[(nx, ny)] = (x, y)

    # reconstruct path
    path = []
    node = goal

    while node in parent:
        path.append(node)
        node = parent[node]

    path.append(start)
    path.reverse()

    return path


def print_grid(grid, path):
    for i in range(SIZE):
        for j in range(SIZE):
            if (i, j) in path:
                print("P", end=" ")
            elif grid[i][j] == 1:
                print("X", end=" ")
            else:
                print(".", end=" ")
        print()


if __name__ == "__main__":
    grid = generate_grid()

    start = (0, 0)
    goal = (SIZE-1, SIZE-1)

    grid[0][0] = 0
    grid[goal[0]][goal[1]] = 0

    path = dijkstra_grid(grid, start, goal)

    print("Path Length:", len(path))
    print_grid(grid, path)
