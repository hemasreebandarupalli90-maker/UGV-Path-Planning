import random
import heapq
import time

SIZE = 15

def move_obstacles(grid):
    for _ in range(5):
        x = random.randint(0, SIZE-1)
        y = random.randint(0, SIZE-1)
        grid[x][y] = 1 if grid[x][y] == 0 else 0


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
    grid = [[0]*SIZE for _ in range(SIZE)]

    current = (0,0)
    goal = (SIZE-1, SIZE-1)

    while current != goal:
        move_obstacles(grid)

        path = dijkstra(grid, current, goal)

        if len(path) < 2:
            print("No path!")
            break

        current = path[1]
        print("Moved to:", current)

        time.sleep(0.3)

    print("Goal reached!")
