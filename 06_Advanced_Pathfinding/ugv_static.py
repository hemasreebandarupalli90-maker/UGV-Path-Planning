import heapq
import random

SIZE = 15
DENSITY = 0.2

def generate_grid():
    grid = [[0 for _ in range(SIZE)] for _ in range(SIZE)]
    for i in range(SIZE):
        for j in range(SIZE):
            if random.random() < DENSITY:
                grid[i][j] = 1
    return grid


def neighbors(x, y):
    return [(x+1,y),(x-1,y),(x,y+1),(x,y-1)]


def dijkstra(grid, start, goal):
    pq = [(0, start)]
    parent = {}
    visited = set()

    while pq:
        cost, node = heapq.heappop(pq)

        if node in visited:
            continue

        visited.add(node)

        if node == goal:
            break

        for nx, ny in neighbors(*node):
            if 0 <= nx < SIZE and 0 <= ny < SIZE:
                if grid[nx][ny] == 0:
                    heapq.heappush(pq, (cost+1, (nx,ny)))
                    parent[(nx,ny)] = node

    path = []
    node = goal
    while node in parent:
        path.append(node)
        node = parent[node]

    path.append(start)
    path.reverse()
    return path


if __name__ == "__main__":
    grid = generate_grid()
    start = (0,0)
    goal = (SIZE-1, SIZE-1)

    grid[0][0] = 0
    grid[goal[0]][goal[1]] = 0

    path = dijkstra(grid, start, goal)

    print("Path Length:", len(path))
