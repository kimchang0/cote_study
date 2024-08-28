import sys
import heapq
input = sys.stdin.readline
print = sys.stdout.write

n = int(input())

heap = []

for _ in range(n):
    heapq.heappush(heap, int(input()))

total_comparisons = 0

while len(heap) > 1:
    first = heapq.heappop(heap)
    second = heapq.heappop(heap)
    
    combined = first + second
    
    heapq.heappush(heap, combined)
    
    total_comparisons += combined

print(str(total_comparisons))