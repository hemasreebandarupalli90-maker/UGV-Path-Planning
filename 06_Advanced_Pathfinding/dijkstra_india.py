import heapq

# Graph of cities (sample realistic subset)
graph = {
    "Delhi": {"Jaipur": 280, "Lucknow": 550},
    "Jaipur": {"Delhi": 280, "Ahmedabad": 670},
    "Lucknow": {"Delhi": 550, "Patna": 530},
    "Patna": {"Lucknow": 530, "Kolkata": 580},
    "Ahmedabad": {"Jaipur": 670, "Mumbai": 530},
    "Mumbai": {"Ahmedabad": 530, "Bangalore": 980},
    "Bangalore": {"Mumbai": 980, "Chennai": 350},
    "Chennai": {"Bangalore": 350, "Kolkata": 1650},
    "Kolkata": {"Patna": 580, "Chennai": 1650}
}

def dijkstra(graph, start, goal):
    pq = [(0, start, [])]  # (cost, node, path)
    visited = set()

    while pq:
        cost, node, path = heapq.heappop(pq)

        if node in visited:
            continue

        path = path + [node]
        visited.add(node)

        if node == goal:
            return cost, path

        for neighbor, weight in graph[node].items():
            if neighbor not in visited:
                heapq.heappush(pq, (cost + weight, neighbor, path))

    return float("inf"), []


if __name__ == "__main__":
    start = input("Enter start city: ")
    goal = input("Enter goal city: ")

    cost, path = dijkstra(graph, start, goal)

    print("Shortest Path:", " -> ".join(path))
    print("Total Distance:", cost, "km")
