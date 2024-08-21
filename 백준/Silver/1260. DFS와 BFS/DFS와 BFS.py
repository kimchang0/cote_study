from collections import deque, defaultdict
import sys
input = sys.stdin.readline

def dfs(graph, start, visited):
    visited.append(start)
    for node in sorted(graph[start]):
        if node not in visited:
            dfs(graph, node, visited)
    return visited

def bfs(graph, start):
    visited = []
    queue = deque([start])
    
    while queue:
        node = queue.popleft()
        if node not in visited:
            visited.append(node)
            queue.extend(sorted(graph[node]))
    
    return visited

def main():
    n, m, v = map(int, input().split())
    
    graph = defaultdict(list)
    
    for _ in range(m):
        a, b = map(int, input().split())
        graph[a].append(b)
        graph[b].append(a)

    
    dfs_result = dfs(graph, v, [])
    bfs_result = bfs(graph, v)
    
    print(" ".join(map(str, dfs_result)))
    print(" ".join(map(str, bfs_result)))

if __name__ == "__main__":
    main()