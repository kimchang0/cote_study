import sys
import heapq

def main():
    import sys

    input = sys.stdin.readline

    N, M, K, X = map(int, input().split())
    graph = {}
    for _ in range(M):
        A, B = map(int, input().split())
        if A not in graph:
            graph[A] = []
        graph[A].append((B, 1))

    distance = {}
    distance[X] = 0

    queue = []
    heapq.heappush(queue, (0, X))

    while queue:
        current_dist, current_node = heapq.heappop(queue)

        if current_node in distance and distance[current_node] < current_dist:
            continue

        if current_node in graph:
            for adjacent, weight in graph[current_node]:
                new_dist = current_dist + weight
                if adjacent not in distance or new_dist < distance[adjacent]:
                    distance[adjacent] = new_dist
                    heapq.heappush(queue, (new_dist, adjacent))

    result = [node for node, dist in distance.items() if dist == K]

    if result:
        result.sort()
        for city in result:
            print(city)
    else:
        print(-1)

if __name__ == "__main__":
    main()